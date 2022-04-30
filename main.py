import sys, cv2

import numpy
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from numpy import random
import numpy as np
from scipy import ndimage

import blur, image_module
from editvalueform import Ui_Form

from giaodien import Ui_MainWindow

class MainWindow:
    image = None
    new_image = None

    brightValue = 0;
    thresholdValue = 0;
    selectedImage = False
    rotateValue = 0
    gaussianValue = 0
    isHistogram_Equal = False
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.slider_brighness.valueChanged['int'].connect(self.changeBrightnessValue)
        # self.uic.slider_blur.valueChanged['int'].connect(self.blurEvt)
        self.uic.slider_threshold.valueChanged['int'].connect(self.changeThretholdValue)
        self.uic.actionOpen.triggered.connect(self.openImageEvt)
        self.uic.actionGaussian.triggered.connect(self.openGaussianForm)
        # self.uic.cbb_edge_dectection.addItems(["Java", "C#", "Python"])
        self.uic.actionSave.triggered.connect(self.saveImageEvt)
        self.uic.actionRotation.triggered.connect(self.changeRotateValue)
        self.uic.checkBox_grayImage.stateChanged.connect(self.grayImageEvt)
        self.uic.checkbox_invertImage.stateChanged.connect(self.invertImageEvt)
        self.uic.checkBox_sharpen_image.stateChanged.connect(self.sharpenImageEvt)
        # self.uic.rd_btn_medium.toggled.connect(self.changeblurMode)
        # self.uic.rd_btn_gaussian.toggled.connect(self.changeblurMode)
        self.uic.slider_imgscale.valueChanged['int'].connect(self.scaleImage)
        self.uic.checkBox_edge_detection.stateChanged.connect(self.checkBox_edgeDetectionEvt)
        # self.uic.checkBox.stateChanged.connect(self.checkboxEvt)
        self.uic.actionHistogram_equal.triggered.connect(self.turnHistogramEqual)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.uic.histogramWidget.addWidget(self.canvas)

        self.new_image = None
        self.tmp_image = None
    def changeRotateValue(self):
        if(self.rotateValue == 0):
            self.rotateValue = 90
        elif(self.rotateValue == 90):
            self.rotateValue = 180
        elif(self.rotateValue == 270):
            self.rotateValue = 360
        else:
            self.rotateValue = 0

        self.showImage()
    def turnHistogramEqual(self):
        self.isHistogram_Equal = True

        self.showImage()
    def histogramEqual(self):
        img_yuv = cv2.cvtColor(self.new_image, cv2.COLOR_RGB2YUV)
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
        self.new_image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)


    def scaleImage(self, value):
        self.new_image = cv2.resize(self.new_image, None, fx=value+1, fy=value+1, interpolation=cv2.INTER_CUBIC)
        self.showImage()
    def sharpenImageEvt(self):
        print('')
    def Tich_chap(self, mask):
        self.new_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        print('cscscscsxs', self.image)
        m, n, c = self.new_image.shape
        img_new = np.zeros([m, n])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                temp = self.new_image[i - 1, j - 1] * mask[0, 0] \
                       + self.new_image[i, j - 1] * mask[0, 1] \
                       + self.new_image[i + 1, j - 1] * mask[0, 2] \
                       + self.new_image[i - 1, j] * mask[1, 0] \
                       + self.new_image[i, j] * mask[1, 1] \
                       + self.new_image[i + 1, j] * mask[1, 2] \
                       + self.new_image[i - 1, j + 1] * mask[2, 0] \
                       + self.new_image[i, j + 1] * mask[2, 1] \
                       + self.new_image[i + 1, j + 1] * mask[2, 2]
                print('temp', temp)
                img_new[i, j] = temp
        img_new = img_new.astype(np.uint8)
        return img_new
    def checkBox_edgeDetectionEvt(self):
        # roberts_cross_v = np.array([[1, 0],
        #                             [0, -1]])
        #
        # roberts_cross_h = np.array([[0, 1],
        #                             [-1, 0]])
        # self.new_image = self.new_image.astype('float64')
        # self.new_image /= 255.0
        # vertical = ndimage.convolve(self.new_image, roberts_cross_v)
        # horizontal = ndimage.convolve(self.new_image, roberts_cross_h)
        #
        # self.new_image = np.sqrt(np.square(horizontal) + np.square(vertical))
        # self.new_image *= 255
        # # print(self.new_image)
        # self.showImage()
        # Định nghĩa Sobel theo hướng X

        # locSobelX = np.array(([-1, -2, -1],
        #                       [0, 0, 0],
        #                       [1, 2, 1]), dtype="float")
        #
        # # Định nghĩa bộ lọc Sobel theo hướng Y
        # locSobelY = np.array(([-1, 0, 1],
        #                       [-2, 0, 2],
        #                       [1, 0, 1]), dtype="float")
        # imgSobelX = self.Tich_chap(self.new_image, locSobelX)
        #
        # imgSobelY = self.Tich_chap(self.new_image, locSobelY)
        #
        # imgSobelXY = imgSobelX + imgSobelY
        #
        # self.new_image = imgSobelXY
        # self.showImage()
        # self.new_image = cv2.Canny(self.new_image, cv2.CV_64F, dx=0, dy=1, ksize=5)
        # cv2.imshow("ddđ", self.new_image)
        # self.showImage()
        # locSobelX = np.array(([-1, -2, -1],
        #                       [0, 0, 0],
        #                       [1, 2, 1]), dtype="float")

        # Định nghĩa bộ lọc Sobel theo hướng Y
        # locSobelY = np.array(([-1, 0, 1],
        #                       [-2, 0, 2],
        #                       [1, 0, 1]), dtype="float")
        # locGaussian3x3 = np.array(([0.0751 / 4.8976, 0.1238 / 4.8976, 0.0751 / 4.8976],
        #                            [0.1238 / 4.8976, 0.2042 / 4.8976, 0.1238 / 4.8976],
        #                            [0.0751 / 4.8976, 0.1238 / 4.8976, 0.0751 / 4.8976]), dtype="float")
        # image = self.Tich_chap(locGaussian3x3)
        #
        # imgSobelX = self.Tich_chap(locSobelX)
        #
        # imgSobelY = self.Tich_chap(locSobelY)
        #
        # imgSobelXY = imgSobelX + imgSobelY
        #
        # self.new_image = image + imgSobelXY
        # cv2.imshow('ddd', self.new_image)
        gray = cv2.cvtColor(self.new_image, cv2.COLOR_BGR2GRAY)
        img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)

        # sobel
        img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=3)
        img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=3)

        img_sobel = (img_sobelx + img_sobely) / 2
        for i in range(img_sobel.shape[0]):
            for j in range(img_sobel.shape[1]):
                if img_sobel[i][j] < 20:
                    img_sobel[i][j] = 0
                else:
                    img_sobel[i][j] = 255
        self.new_image = img_sobel
        fig = plt.figure(figsize=(16, 9))  # Tạo vùng vẽ tỷ lệ 16:9
        ax1= fig.subplots(1, 1)  # Tạo 6 vùng vẽ con
        ax1.imshow(self.new_image, cmap='gray')
        ax1.set_title("Ảnh gốc")
        plt.show()
        # cv2.imshow('dddd', self.new_image)
        self.showImage()
    def grayImageEvt(self):
        self.new_image = cv2.cvtColor(self.new_image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('ssdsds', self.new_image)
        self.showImage()
    def invertImageEvt(self):
        self.new_image = self.image
        self.new_image  = 255 - self.new_image
        self.showImage()
    def changeThretholdValue(self, value):
        self.thresholdValue = value

        self.showImage()
    def updateThrehold(self):
        # if value == 0:
        #     value = 1;
        # if value % 2 == 0:
        #     value += 1
        self.new_image = cv2.threshold(self.new_image, self.thresholdValue, 255, cv2.THRESH_BINARY)
        self.new_image = self.new_image[1]
    def openGaussianForm(self, value):
        # self.changeGaussianValue = value

        # self.editvalueWindow = MainWindow()
        # self.ui = Ui_Form()
        # self.ui.setupUi(self.editvalueWindow)
        # self.editvalueWindow.show()
        self.edt_window = QtWidgets.QMainWindow()

        self.ui = Ui_Form()
        self.ui.setupUi(self, self.edt_window , 'Gaussian filter')

        self.edt_window.show()
    def changeblurMode(self, text):
        if(self.uic.rd_btn_medium.isChecked()):
            blur.mode = 0
        elif(self.uic.rd_btn_gaussian.isChecked()):
            blur.mode = 1
            blur.mode = 1
        print(blur.mode)
    def convertImagetoDisplay(self, image):
        if(len(image.shape) == 2):
            h, w = self.new_image.shape
            bytesPerLine = 3 * w
            cv2.imshow('sssss', self.new_image)
            image = QtGui.QImage(image.data, w, h, bytesPerLine, QtGui.QImage.Format_Grayscale8).rgbSwapped()
        else:
            h, w, c = image.shape
            bytesPerLine = 3 * w
            image = QtGui.QImage(image.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888).rgbSwapped()
        return image
    def show(self):
        self.main_win.show()
    def changeBrightnessValue(self, value):
        self.brightValue = value

        self.showImage()
    def updateBrighness(self):
        hsv = cv2.cvtColor(self.new_image, cv2.COLOR_BGR2HSV)
        # print(self.new_image)
        h, s, v = cv2.split(hsv)
        # distance = abs(value-self.brightValue)
        lim = 255 - self.brightValue
        v[v > lim] = 255
        v[v <= lim] += self.brightValue
        final_hsv = cv2.merge((h, s, v))
        self.new_image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        # print("H",h,"S :", s, "V:", v)
    # def gau(self, value):
    #     # self.new_image = self.image
    #     # if value == 0:
    #     #     value = 1
    #     # if value % 2 == 0:
    #     #     value+= 1
    #     # kernel_size = (value, value)  # +1 is to avoid 0
    #     # self.new_image = cv2.GaussianBlur(self.new_image, kernel_size, 0)
    #     # self.showImage()
    # # def checkboxEvt(self, state):
    # #     if (QtCore.Qt.Checked == state):
    # #         self.new_image = self.image
    # #         self.new_image = cv2.cvtColor(self.new_image, cv2.COLOR_BGR2GRAY)
    # #
    # #         self.showImage()
    # #     print(blur.mode)
    #     if(blur.mode == 0):
    #         blur.mediumBlur(self, value)
    #     elif(blur.mode == 1):
    #         blur.gaussianBlur(self, value)

    def saveImageEvt(self):
        f = QFileDialog.getSaveFileName(None, 'Save image', '',
                                           'Image Files (*.png *.jpg *.bmp *.tif)')
        # print(f[0])
        if f[0] != '':
            cv2.imwrite(f[0], self.new_image)
    def openImageEvt(self):
        f = QFileDialog.getOpenFileName(None, 'Open a file', '',
                                           'Image Files (*.png *.jpg *.bmp *.tif)')
        if f[0] != '':
            self.image = cv2.imread(f[0], cv2.COLOR_HSV2BGR)
            print('so chieu', len(self.image.shape))
            print('imageeeeeeeee', self.image)
            self.new_image =  self.image

            self.brightValue = 0
            self.uic.slider_brighness.setValue(self.brightValue)

            self.selectedImage = True
            self.showImage()
    def showImage(self):
        self.updateChange()

        self.uic.lbl_photo.setPixmap(QtGui.QPixmap.fromImage(self.convertImagetoDisplay(self.image)))
        self.uic.lbl_newPhoto.setPixmap(QtGui.QPixmap.fromImage(self.convertImagetoDisplay(self.new_image)))
        self.updateHistogram()
    def updateChange(self):
        self.new_image = self.image

        #update brighness
        if(self.brightValue != 0):
            self.updateBrighness()
        if(self.thresholdValue != 0):
            self.updateThrehold()
        if(self.rotateValue >= 0):
            image_module.rotateImage(self)
        if(self.gaussianValue > 0):
            if self.gaussianValue % 2 == 0:
                self.gaussianValue += 1
            self.new_image = cv2.GaussianBlur(self.new_image, (self.gaussianValue, self.gaussianValue), 0)
        if(self.isHistogram_Equal == True):
            self.histogramEqual()
    # rows, cols, steps = self.new_image.shape
    # M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)  # thay đổi chiều của ảnh
    # self.new_image = cv2.warpAffine(self.new_image, M, (cols, rows))
    #
    # self.showImage()
    def updateHistogram(self):
        # random data
        # data = [random.random() for i in range(10)]
        self.figure.clear()
        # clearing old figure
        chanel = len(self.new_image.shape)
        if(chanel == 2):
            ax = self.figure.add_subplot(111)
            histr = cv2.calcHist([self.new_image], 0, None, [256], [0, 256])
            ax.plot(histr, color='yellow', linewidth=3.0)
            ax.set_ylabel('Y', color='blue')
            ax.set_xlabel('X', color='blue')
            ax.set_title('Histogram')
            ax.set_facecolor('xkcd:wheat')
            ax.grid()
            self.canvas.draw()
        else:
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
            self.canvas.draw()
        # plot data
        # ax.plot(data, '*-')

        # refresh canvas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())