import sys, cv2

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from numpy import random
import numpy as np
import blur

from giaodien import Ui_MainWindow

class MainWindow:
    image = None
    new_image = None
    brightValue = 0;
    selectedImage = False

    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.horizontalSlider.valueChanged['int'].connect(self.changeBrightness)
        self.uic.horizontalSlider_2.valueChanged['int'].connect(self.blurEvt)
        self.uic.slider_threshold.valueChanged['int'].connect(self.change_thresholdEvt)
        self.uic.btn_openFIle.clicked.connect(self.clickEvt)
        self.uic.checkbox_invertImage.stateChanged.connect(self.invertImageEvt)
        self.uic.rd_btn_medium.toggled.connect(self.changeblurMode)
        self.uic.rd_btn_gaussian.toggled.connect(self.changeblurMode)

        # self.uic.checkBox.stateChanged.connect(self.checkboxEvt)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.uic.histogramWidget.addWidget(self.canvas)

        self.new_image = None
        self.tmp_image = None
    def invertImageEvt(self):
        self.new_image = self.image
        self.new_image  = 255 - self.new_image
        self.updateImage()
    def change_thresholdEvt(self, value):
        blur.threshsold(self, value)
    def changeblurMode(self, text):
        if(self.uic.rd_btn_medium.isChecked()):
            blur.mode = 0
        elif(self.uic.rd_btn_gaussian.isChecked()):
            blur.mode = 1
        print(blur.mode)
    def convertImagetoDisplay(self, image):
        h, w, c = image.shape
        bytesPerLine = 3* w
        image = QtGui.QImage(image.data, w, h , bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()

        return image
    def show(self):
        self.main_win.show()
    def changeBrightness(self, value):
        self.new_image = self.image
        hsv = cv2.cvtColor(self.new_image, cv2.COLOR_BGR2HSV)
        # print(self.new_image)
        h, s, v = cv2.split(hsv)
        distance = abs(value-self.brightValue)
        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value
        final_hsv = cv2.merge((h, s, v))
        self.new_image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        self.updateImage()
        self.brightValue = value

        print("H",h,"S :", s, "V:", v)
    def blurEvt(self, value):
        # self.new_image = self.image
        # if value == 0:
        #     value = 1
        # if value % 2 == 0:
        #     value+= 1
        # kernel_size = (value, value)  # +1 is to avoid 0
        # self.new_image = cv2.GaussianBlur(self.new_image, kernel_size, 0)
        # self.updateImage()
    # def checkboxEvt(self, state):
    #     if (QtCore.Qt.Checked == state):
    #         self.new_image = self.image
    #         self.new_image = cv2.cvtColor(self.new_image, cv2.COLOR_BGR2GRAY)
    #
    #         self.updateImage()
        print(blur.mode)
        if(blur.mode == 0):
            blur.mediumBlur(self, value)
        elif(blur.mode == 1):
            blur.gaussianBlur(self, value)
    def clickEvt(self):
        f = QFileDialog.getOpenFileName(None, 'Open a file', '',
                                           'Image Files (*.png *.jpg *.bmp *.tif)')

        self.image = cv2.imread(f[0], cv2.COLOR_BGR2RGB)
        self.new_image =  self.image

        self.brightValue = 0
        self.uic.horizontalSlider.setValue(self.brightValue)

        self.updateImage()
        self.selectedImage = True
    def updateImage(self):
        self.uic.lbl_photo.setPixmap(QtGui.QPixmap.fromImage(self.convertImagetoDisplay(self.image)))
        self.uic.lbl_newPhoto.setPixmap(QtGui.QPixmap.fromImage(self.convertImagetoDisplay(self.new_image)))
        self.updateHistogram()
    def updateHistogram(self):
        # random data
        data = [random.random() for i in range(10)]

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv2.calcHist([self.new_image], [i], None, [256], [0, 256])
            ax.plot(histr, color=col, linewidth=3.0)
            ax.set_ylabel('Y', color='blue')
            ax.set_xlabel('X', color='blue')
            ax.set_title('Histogram')
            ax.set_facecolor('xkcd:wheat')
            ax.grid()
        # plot data
        # ax.plot(data, '*-')

        # refresh canvas
        self.canvas.draw()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())