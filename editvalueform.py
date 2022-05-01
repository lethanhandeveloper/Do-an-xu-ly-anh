from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets

from modules.filter_module import BlurFunction

class Ui_Form(object):
    title = ''
    spinBox = None


    def __init__(self, main, type):
        self.type = type
        self.blur_function = BlurFunction()
        self.main = main
        self.tmp_gaussianValue = main.gaussianValue
    def setupUi(self, Form):
        self.Form = Form
        Form.setObjectName('Form')
        Form.resize(373, 108)

        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(30, 11, 51, 41))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setProperty('value', self.main.gaussianValue)

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 70, 211, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged['int'].connect(self.changeValue)
        self.horizontalSlider.setValue(self.main.gaussianValue)
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(270, 10, 93, 28))
        self.btn_ok.setObjectName("pushButton")
        self.btn_ok.clicked.connect(self.btnOkEvt)
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(270, 50, 93, 28))
        self.btn_cancel.setObjectName("pushButton_2")
        self.btn_cancel.clicked.connect(self.cancelBtnEvt)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        if(self.type == 1):
            self.title = 'Gaussian value'
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate(self.title , self.title ))
        self.btn_ok.setText(_translate("Form", "OK"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
        self.label.setText(_translate("Form", "Size"))
    def changeValue(self, value):
        if(self.type == 1):
            self.main.gaussianValue = value
        elif(self.type == 2):
            self.main.gaussianValue = value
        self.spinBox.setProperty('value', self.main.gaussianValue)
        self.main.showImage()
    def btnOkEvt(self):
        self.Form.close()
    def cancelBtnEvt(self):
        self.main.gaussianValue = self.tmp_gaussianValue
        self.main.showImage()
        self.Form.close()