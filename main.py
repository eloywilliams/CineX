from PyQt4 import QtGui

from Manager import *
from GUI import Ui_form_principal
from drawAF import *

class Main(QtGui.QWidget, Ui_form_principal):

    ok = QtCore.pyqtSignal()

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.machine = QtCore.QStateMachine()

        self.inicial = Estado(self.ok)
        self.pelicula = Pelicula(self.ok)
        self.dia = Dia(self.ok)
        self.horario = Horario(self.ok)
        self.final = Confirmar(self.ok)

        self.inicial.addTransition(self.boton_rec.clicked, self.pelicula)
        self.pelicula.addTransition(self.ok, self.dia)
        self.dia.addTransition(self.ok, self.horario)
        self.horario.addTransition(self.ok, self.final)

        self.machine.addState(self.inicial)
        self.machine.addState(self.pelicula)
        self.machine.addState(self.dia)
        self.machine.addState(self.horario)
        self.machine.addState(self.final)

        self.machine.setInitialState(self.inicial)

        self.pelicula.entered.connect(self.pelicula.into)
        self.pelicula.exited.connect(self.pelicula.leave)
        self.dia.entered.connect(self.dia.into)
        self.dia.exited.connect(self.dia.leave)
        self.horario.entered.connect(self.horario.into)
        self.horario.exited.connect(self.horario.leave)
        self.final.entered.connect(self.final.into)
        self.final.exited.connect(self.final.leave)

        self.machine.start()

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    drawAf = DrawAF()

    drawAf.draw()

    window = Main()
    window.show()

    sys.exit(app.exec_())
