__author__ = 'leandro'

from pocketsphinx.pocketsphinx import *
import pyaudio
import sys


class Reconocedor(object):

    def __init__(self):
        """
            Constructor de la clase Reconocedor
        :return:
        """

        self._ACOU = '/home/leandro/Descargas/voxforge-es-0.1/model_parameters/voxforge_es_sphinx.cd_cont_1500/'
        self._DICT = '/home/leandro/Descargas/voxforge-es-0.1/etc/voxforge_es_sphinx.dic'
        self._GRAMM = '/home/leandro/Descargas/asr-pocketsphinx-spanish/pruebas/peliculas'

    def generarDecoder(self):
        """
            Genera el decoder necesario para reconocer la
            entrada por microfono
        :return:
        """
        config = Decoder.default_config()
        config.set_string('-hmm', self._ACOU)
        config.set_string('-dict', self._DICT)
        config.set_string('-jsgf', self._GRAMM)
        return Decoder(config)

    def obtenerEntrada(self):
        """
            Devuelve la entrada reconocida desde el microfono
        :return:
        """

        p = pyaudio.PyAudio()
        decoder = self.generarDecoder()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
        stream.start_stream()
        in_speech_bf = True
        decoder.start_utt()
        while True:
            buf = stream.read(1024)
            if buf:
                decoder.process_raw(buf, False, False)
                try:
                    if  decoder.hyp().hypstr != '':
                        pass
                        #print 'Partial decoding result:', decoder.hyp().hypstr
                except AttributeError:
                    pass
                if decoder.get_in_speech():
                    sys.stdout.write('.')
                    sys.stdout.flush()
                if decoder.get_in_speech() != in_speech_bf:
                    in_speech_bf = decoder.get_in_speech()
                    if not in_speech_bf:
                        decoder.end_utt()
                        try:
                            if  decoder.hyp().hypstr != '':
                                return str(decoder.hyp().hypstr)
                        except AttributeError:
                            pass
                        decoder.start_utt()

    @property
    def ACOU(self):
        return self._ACOU

    @ACOU.setter
    def ACOU(self,value):
        self._ACOU = value