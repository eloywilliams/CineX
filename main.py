from PyQt4 import QtGui
import graphviz as gv

from Manager import *
from GUI import Ui_form_principal


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

def draw(alfabeto, estados, inicio, trans, final):
    print("inicio:", str(inicio))
    g = gv.Digraph(format='png')
    g.graph_attr['rankdir'] = 'LR'
    g.node('ini', shape="point")
    for e in estados:
        if e in final:
            g.node(e, shape="doublecircle")
        else:
            g.node(e)
        if e in inicio:
            g.edge('ini', e)

    for t in trans:
        if t[2] not in alfabeto:
            return 0
        g.edge(t[0], t[1], label=str(t[2]))
    g.render()


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    estados = ["Inicio", "Pelicula", "Dia", "Horario", "Final"]
    trans = [("Inicio", "Pelicula", 0), ("Pelicula", "Dia", 0), ("Pelicula", "Pelicula", 1),
             ("Dia", "Horario", 1), ("Horario", "Final", 1)]
    inicial = ["Inicio"]
    alf = [0, 1]
    terminal = ("Final",)

    draw(alf, estados, inicial, trans, terminal)

    window = Main()
    window.show()

    sys.exit(app.exec_())
