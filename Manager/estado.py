from PyQt4 import QtCore

class Estado(QtCore.QState):

    def __init__(self):
        QtCore.QState.__init__(self)

    def into(self):
        pass

    def leave(self):
        pass

class Pelicula(Estado):

    def __init__(self):
        Estado.__init__()

    def into(self):
        pass

    def leave(self):
        pass

class Dia(Estado):

    def __init__(self):
        Estado.__init__()

    def into(self):
        pass

    def leave(self):
        pass

class Horario(Estado):

    def __init__(self):
        Estado.__init__()

    def into(self):
        pass

    def leave(self):
        pass

class Confirmar(Estado):

    def __init__(self):
        Estado.__init__()

    def into(self):
        pass

    def leave(self):
        pass