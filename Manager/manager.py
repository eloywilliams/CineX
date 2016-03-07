# -*- coding:utf-8 -*-
from PyQt4.QtCore import pyqtSignal


class Manager(object):
    """
        Clase que modela el Administrador de Dialogo
    """

    #Definiciones de señales para transicionar entre eventos
    ok = pyqtSignal()
    cancel = pyqtSignal()

    def __init__(self):
        fsm = None
        reconocedor = None