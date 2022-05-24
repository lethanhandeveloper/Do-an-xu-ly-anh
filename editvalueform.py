from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets

from modules.filter_module import BlurFunction

class Ui_Form(object):
<<<<<<< HEAD
<<<<<<< HEAD
    title = ''
    spinBox = None


    def __init__(self, main, type):
        self.type = type
        self.blur_function = BlurFunction()
        self.main = main
        self.tmp_gaussianValue = main.gaussianValue
    def setupUi(self, Form):
=======
    type
    # spinBox = None
    def __init__(self, main, type):
        self.type = type
        self.main = main
=======
    type
    # spinBox = None
    def __init__(self, main, type):
        self.type = type
        self.main = main
>>>>>>> f15a33363e03c1e2f0e4999a76aaa245a268c809
    def setupUi(self, Form):
        self.tmp_gaussianBlurValue = self.main.gaussianBlurValue

>>>>>>> an
        self.Form = Form
        Form.setObjectName('Form')
        Form.resize(373, 108)

        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(30, 11, 51, 41))
        self.spinBox.setObjectName("spinBox")
<<<<<<< HEAD
<<<<<<< HEAD
        self.spinBox.setProperty('value', self.main.gaussianValue)
=======
>>>>>>> an
=======
>>>>>>> f15a33363e03c1e2f0e4999a76aaa245a268c809

        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 70, 211, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.valueChanged['int'].connect(self.changeValue)
<<<<<<< HEAD
<<<<<<< HEAD
        self.horizontalSlider.setValue(self.main.gaussianValue)
=======

>>>>>>> an
=======

>>>>>>> f15a33363e03c1e2f0e4999a76aaa245a268c809
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(270, 10, 93, 28))
        self.btn_ok.setObjectName("pushButton")
        self.btn_ok.clicked.connect(self.btnOkEvt)
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(270, 50, 93, 28))
        self.btn_cancel.setObjectName("pushButton_2")
        self.btn_cancel.clicked.connect(self.cancelBtnEvt)

<<<<<<< HEAD
<<<<<<< HEAD
=======
        self.updateSpinBoxandSliderValue()

>>>>>>> an
=======
        self.updateSpinBoxandSliderValue()

>>>>>>> f15a33363e03c1e2f0e4999a76aaa245a268c809
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
        if(self.type == 1):
            self.title = 'Gaussian value'
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
<<<<<<< HEAD
<<<<<<< HEAD
            self.main.gaussianValue = value
        elif(self.type == 2):
            self.main.gaussianValue = value
        self.spinBox.setProperty('value', self.main.gaussianValue)
=======
=======
>>>>>>> f15a33363e03c1e2f0e4999a76aaa245a268c809
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
<<<<<<< HEAD
>>>>>>> an
=======
>>>>>>> f15a33363e03c1e2f0e4999a76aaa245a268c809
        self.main.showImage()
    def btnOkEvt(self):
        self.Form.close()
    def cancelBtnEvt(self):
        self.main.gaussianBlurValue = self.tmp_gaussianBlurValue
        self.main.showImage()
        self.Form.close()