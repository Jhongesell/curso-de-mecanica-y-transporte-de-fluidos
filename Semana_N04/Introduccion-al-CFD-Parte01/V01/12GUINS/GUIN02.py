# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUIN02.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(924, 484)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.radio01lineal = QtWidgets.QRadioButton(Dialog)
        self.radio01lineal.setAcceptDrops(False)
        self.radio01lineal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radio01lineal.setObjectName("radio01lineal")
        self.verticalLayout.addWidget(self.radio01lineal)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.radio02nolineal = QtWidgets.QRadioButton(Dialog)
        self.radio02nolineal.setObjectName("radio02nolineal")
        self.verticalLayout_2.addWidget(self.radio02nolineal)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line01nx = QtWidgets.QLineEdit(self.groupBox)
        self.line01nx.setObjectName("line01nx")
        self.verticalLayout_4.addWidget(self.line01nx)
        self.line02x = QtWidgets.QLineEdit(self.groupBox)
        self.line02x.setObjectName("line02x")
        self.verticalLayout_4.addWidget(self.line02x)
        self.line03nt = QtWidgets.QLineEdit(self.groupBox)
        self.line03nt.setObjectName("line03nt")
        self.verticalLayout_4.addWidget(self.line03nt)
        self.line04dt = QtWidgets.QLineEdit(self.groupBox)
        self.line04dt.setObjectName("line04dt")
        self.verticalLayout_4.addWidget(self.line04dt)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.line05c = QtWidgets.QLineEdit(self.groupBox_2)
        self.line05c.setObjectName("line05c")
        self.horizontalLayout_3.addWidget(self.line05c)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.line06c_variable = QtWidgets.QLineEdit(self.groupBox_2)
        self.line06c_variable.setObjectName("line06c_variable")
        self.horizontalLayout_4.addWidget(self.line06c_variable)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.line07u = QtWidgets.QLineEdit(self.groupBox_2)
        self.line07u.setObjectName("line07u")
        self.horizontalLayout_9.addWidget(self.line07u)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.line08x1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.line08x1.setObjectName("line08x1")
        self.horizontalLayout_5.addWidget(self.line08x1)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.line09x2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.line09x2.setObjectName("line09x2")
        self.horizontalLayout_6.addWidget(self.line09x2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_10.addWidget(self.groupBox_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.pushSolver = QtWidgets.QPushButton(Dialog)
        self.pushSolver.setObjectName("pushSolver")
        self.verticalLayout_7.addWidget(self.pushSolver)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelResponse01 = QtWidgets.QLabel(self.groupBox_3)
        self.labelResponse01.setStyleSheet("background-color: rgb(138, 226, 52);")
        self.labelResponse01.setText("")
        self.labelResponse01.setObjectName("labelResponse01")
        self.verticalLayout_6.addWidget(self.labelResponse01)
        self.labelResponse02 = QtWidgets.QLabel(self.groupBox_3)
        self.labelResponse02.setStyleSheet("background-color: rgb(252, 175, 62);")
        self.labelResponse02.setText("")
        self.labelResponse02.setObjectName("labelResponse02")
        self.verticalLayout_6.addWidget(self.labelResponse02)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Solver 1-D Convection Equation "))
        self.label.setText(_translate("Dialog", "Ecuación de Convección 1-D"))
        self.label_2.setText(_translate("Dialog", "u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])"))
        self.radio01lineal.setText(_translate("Dialog", "Lineal"))
        self.label_3.setText(_translate("Dialog", "u[i] = un[i]-un[i]*dt/dx*(un[i]-un[i-1])"))
        self.radio02nolineal.setText(_translate("Dialog", "No líneal"))
        self.groupBox.setTitle(_translate("Dialog", "Variables que parametrizan:"))
        self.label_4.setText(_translate("Dialog", "nx ="))
        self.label_5.setText(_translate("Dialog", "x ="))
        self.label_6.setText(_translate("Dialog", "nt ="))
        self.label_7.setText(_translate("Dialog", "dt ="))
        self.groupBox_2.setTitle(_translate("Dialog", "Condiciones iniciales:"))
        self.label_8.setText(_translate("Dialog", "c ="))
        self.label_9.setText(_translate("Dialog", "c_variable = u ="))
        self.label_10.setText(_translate("Dialog", "u ="))
        self.label_11.setText(_translate("Dialog", "x1 ="))
        self.label_12.setText(_translate("Dialog", "x2 ="))
        self.pushSolver.setText(_translate("Dialog", "Resolver y Graficar"))
        self.groupBox_3.setTitle(_translate("Dialog", "Resultados:"))
