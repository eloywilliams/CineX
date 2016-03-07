1. Instalar sphinxbase y pocketsphinx 
   http://cmusphinx.sourceforge.net/wiki/tutorialpocketsphinx
   En Linux, instalar también el paquete alsa-dev para que funcione el
   micrófono (el nombre varía según la distro; puede ser "lib32asound2-dev"
   o "libasound2-dev", entre otros).
   
2. Download modelos para el español. Acá usamos voxforge-es-0.1.
   http://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/Spanish%20Voxforge/

3. Si es necesario, agregar las palabras faltantes al diccionario fonético
   (voxforge-es-0.1/etc/voxforge_es_sphinx.dic).
   
Manpages:
http://manpages.ubuntu.com/manpages/saucy/man1/pocketsphinx_continuous.1.html
http://manpages.ubuntu.com/manpages/saucy/man1/pocketsphinx_batch.1.html

#################################################

# Ejemplos:


# (0) Preparativos: ubicación de los modelos y directorio de salida.

ACOU=voxforge-es-0.1/model_parameters/voxforge_es_sphinx.cd_cont_1500/
DICT=voxforge-es-0.1/etc/voxforge_es_sphinx.dic
LANG=voxforge-es-0.1/etc/voxforge_es_sphinx.transcription.lm
OUTDIR=pruebas


#### Ejemplos interactivos.

# (1) Por micrófono, usando el modelo de lenguaje:
pocketsphinx_continuous -hmm $ACOU -dict $DICT -lm $LANG

# (2) Por micrófono, usando una gramática específica: 
pocketsphinx_continuous -hmm $ACOU -dict $DICT -jsgf pruebas/gramatica-hola-mundo


#### Ejemplos en modo batch.

# (3) Procesamiento batch de varios archivos wav, usando el modelo del lenguaje.
pocketsphinx_batch -adcin yes -hmm $ACOU -lm $LANG -dict $DICT -ctl pruebas/grabaciones.txt -cepext .wav -cepdir pruebas -hyp $OUTDIR/salida-con-lm.txt

# (4) Idem pero generando lattices.
pocketsphinx_batch -adcin yes -hmm $ACOU -lm $LANG -dict $DICT -ctl pruebas/grabaciones.txt -cepext .wav -cepdir pruebas -hyp $OUTDIR/salida-con-lm.txt -outlatdir $OUTDIR/lattices/

# (5) Procesamiento batch de varios archivos wav, usando el modelo del lenguaje.
pocketsphinx_batch -adcin yes -hmm $ACOU -jsgf pruebas/gramatica-hola-mundo -dict $DICT -ctl pruebas/grabaciones.txt -cepext .wav -cepdir pruebas -backtrace yes -hyp $OUTDIR/salida-con-gramatica.txt

