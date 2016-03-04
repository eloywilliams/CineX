
from PyQt4 import QtGui, QtCore
import graphviz as gv

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

    estados = ["A","B","C","E","F"]
    trans = [("A","B", 1),("A","E",0),("A","E",1),("A","A",1),("A","D",1),("F","F",1),("D","C",1),("B","A",0), ("E","C",0),("F","D",0), ("C","A",0), ("B","B", 1)]
    inicial = ["A"]
    alf = [0,1]
    terminal = ("C",)

    draw(alf, estados, inicial, trans, terminal)

"""

class Window(QtGui.QWidget):

    customSignal = QtCore.pyqtSignal()

    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.machine = QtCore.QStateMachine()

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    window.setGeometry(500, 300, 100, 100)
    sys.exit(app.exec_())






#JSGF V1.0;
grammar pepe;
<hora> = QUINCE | DOCE | NUEVE;
<minutos> = TREINTA | CERO | VEINTE;
public <pepe> = <hora> <minutos>;
    """