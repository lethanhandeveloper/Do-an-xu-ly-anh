# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editvalueform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    type
    # spinBox = None
    def __init__(self, main, type):
        self.type = type
        self.main = main
    def setupUi(self, Form):
        self.tmp_gaussianBlurValue = self.main.gaussianBlurValue

        self.Form = Form
        Form.setObjectName('Form')
        Form.resize(373, 108)

        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(30, 11, 51, 41))
        self.spinBox.setObjectName("spinBox")

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 70, 211, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged['int'].connect(self.changeValue)

        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(270, 10, 93, 28))
        self.btn_ok.setObjectName("pushButton")
        self.btn_ok.clicked.connect(self.btnOkEvt)
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(270, 50, 93, 28))
        self.btn_cancel.setObjectName("pushButton_2")
        self.btn_cancel.clicked.connect(self.cancelBtnEvt)

        self.updateSpinBoxandSliderValue()

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def updateSpinBoxandSliderValue(self):
        if(self.type == 1):
            self.spinBox.setProperty('value', self.main.gaussianBlurValue)
            self.horizontalSlider.setValue(self.main.gaussianBlurValue)
        elif(self.type == 2):
            self.spinBox.setProperty('value', self.main.boxBlurValue)
            self.horizontalSlider.setValue(self.main.boxBlurValue)
        elif(self.type == 3):
            self.spinBox.setProperty('value', self.main.medianBlurValue)
            self.horizontalSlider.setValue(self.main.medianBlurValue)
        elif(self.type == 10):
            self.spinBox.setProperty('value', self.main.c)
            self.horizontalSlider.setValue(self.main.medianBlurValue)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        if(self.type == 1):
            Form.setWindowTitle(_translate('Gaussian Blur', 'Gaussian Blur'))
        elif(self.type == 2):
            Form.setWindowTitle(_translate('Box Blur', 'Box Blur'))
        elif(self.type == 3):
            Form.setWindowTitle(_translate('Median Blur', 'Median Blur'))
        elif(self.type == 10):
            Form.setWindowTitle(_translate('Logarit', 'Logarit'))
        self.btn_ok.setText(_translate("Form", "OK"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Size"))
    def changeValue(self, value):
        if(self.type == 1):
            self.main.gaussianBlurValue = value
        elif(self.type == 2):
            self.main.boxBlurValue = value
        elif(self.type == 3):
            self.main.medianBlurValue = value
        elif(self.type == 4):
            self.main.changeGammaValue = value
        elif(self.type == 5):
            self.main.averageBlurValue = value
        elif(self.type == 10):
            self.main.c += 1
            self.main.gamma += 1

        self.spinBox.setProperty('value', value)
        self.main.showImage()
    def btnOkEvt(self):
        self.Form.close()
    def cancelBtnEvt(self):
        self.main.gaussianBlurValue = self.tmp_gaussianBlurValue
        self.main.showImage()
        self.Form.close()