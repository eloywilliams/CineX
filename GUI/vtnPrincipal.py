# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnPrincipal.ui'
#
# Created: Fri Mar  4 17:20:33 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_form_principal(object):
    def setupUi(self, form_principal):
        form_principal.setObjectName(_fromUtf8("form_principal"))
        form_principal.resize(669, 447)
        self.verticalLayout = QtGui.QVBoxLayout(form_principal)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabla_info = QtGui.QTableWidget(form_principal)
        self.tabla_info.setEnabled(True)
        self.tabla_info.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabla_info.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_info.setObjectName(_fromUtf8("tabla_info"))
        self.tabla_info.setColumnCount(1)
        self.tabla_info.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabla_info.setHorizontalHeaderItem(0, item)
        self.tabla_info.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_info.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tabla_info)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.boton_rec = QtGui.QPushButton(form_principal)
        self.boton_rec.setObjectName(_fromUtf8("boton_rec"))
        self.horizontalLayout.addWidget(self.boton_rec)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(form_principal)
        QtCore.QMetaObject.connectSlotsByName(form_principal)

    def retranslateUi(self, form_principal):
        form_principal.setWindowTitle(_translate("form_principal", "CineX", None))
        item = self.tabla_info.horizontalHeaderItem(0)
        item.setText(_translate("form_principal", "Información", None))
        self.boton_rec.setText(_translate("form_principal", "Rec", None))

