from PyQt4 import QtCore

from ASR import Reconocedor

class Estado(QtCore.QState):

    def __init__(self, ok):
        QtCore.QState.__init__(self)
        self.ok = ok
        self.cadena = ""
        self.reconocedor = Reconocedor(self.ok)

    def into(self):
        pass

    def leave(self):
        pass

class Pelicula(Estado):

    def __init__(self, ok):
        Estado.__init__(self, ok)

    def into(self):
        print "pelicula"
        self.cadena = self.reconocedor.obtenerEntrada()

    def leave(self):
        archivo = open("Manager/ticket.txt", "w")
        archivo.write(self.cadena + "\n")
        archivo.close()

class Dia(Estado):

    def __init__(self, ok):
        Estado.__init__(self, ok)

    def into(self):
        print "dia"
        self.reconocedor.GRAMM = '/home/waldo/Documentos/Universidad/ProcVoz/asr-pocketsphinx-spanish/pruebas/dias'
        self.cadena = self.reconocedor.obtenerEntrada()

    def leave(self):
        archivo = open("Manager/ticket.txt", "a")
        archivo.write(self.cadena + "\n")
        archivo.close()

class Horario(Estado):

    def __init__(self, ok):
        Estado.__init__(self, ok)

    def into(self):
        print "horario"
        self.reconocedor.GRAMM = '/home/waldo/Documentos/Universidad/ProcVoz/asr-pocketsphinx-spanish/pruebas/horarios'
        self.cadena = self.reconocedor.obtenerEntrada()

    def leave(self):
        archivo = open("Manager/ticket.txt", "a")
        archivo.write(self.cadena + "\n")
        archivo.close()

class Confirmar(Estado):

    def __init__(self, ok):
        Estado.__init__(self, ok)

    def into(self):
        print "confirmar"

    def leave(self):
        pass