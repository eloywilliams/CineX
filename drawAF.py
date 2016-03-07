import graphviz as gv

class DrawAF (object):

    def __init__(self):
        """
            Constructor de la clase DrawAF
        :return:
        """
        self._estados = ["Inicio", "Pelicula", "Dia", "Horario", "Final"]
        self._trans = [("Inicio", "Pelicula", "ok", "Blue"), ("Pelicula", "Dia", "ok"), ("Pelicula", "Pelicula", "not_ok"),
                       ("Dia", "Horario", "ok"), ("Dia", "Dia", "not_ok"), ("Horario", "Final", "ok"),
                       ("Horario", "Horario", "not_ok")]
        self._inicial = ["Inicio"]
        self._alfabeto = ["ok", "not_ok"]
        self._final = ("Final",)

    def draw(self):
        g = gv.Digraph(format='png')
        g.graph_attr['rankdir'] = 'LR'
        g.node('ini', shape="point")
        for e in self._estados:
            if e in self._final:
                g.node(e, shape="doublecircle")
            else:
                g.node(e)
            if e in self._inicial:
                g.edge('ini', e)

        for t in self._trans:
            if t[2] not in self._alfabeto:
                return 0
            g.edge(t[0], t[1], label=str(t[2]))
        g.render()
