# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giaodien.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1465, 887)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_photo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_photo.setGeometry(QtCore.QRect(40, 50, 451, 731))
        self.lbl_photo.setStyleSheet("border: 1px solid black;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color:white\n"
"")
        self.lbl_photo.setText("")
        self.lbl_photo.setScaledContents(False)
        self.lbl_photo.setObjectName("lbl_photo")
        self.lbl_newPhoto = QtWidgets.QLabel(self.centralwidget)
        self.lbl_newPhoto.setGeometry(QtCore.QRect(560, 50, 471, 731))
        self.lbl_newPhoto.setStyleSheet("border: 1px solid black;\n"
"qproperty-alignment: AlignCenter;\n"
"background-color:white\n"
"")
        self.lbl_newPhoto.setText("")
        self.lbl_newPhoto.setScaledContents(False)
        self.lbl_newPhoto.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_newPhoto.setObjectName("lbl_newPhoto")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 501, 791))
        self.label.setStyleSheet("background-color:#282828")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 10, 521, 791))
        self.label_3.setStyleSheet("background-color:#282828")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.slider_brighness = QtWidgets.QSlider(self.centralwidget)
        self.slider_brighness.setGeometry(QtCore.QRect(1120, 430, 321, 22))
        self.slider_brighness.setMinimum(0)
        self.slider_brighness.setMaximum(100)
        self.slider_brighness.setProperty("value", 50)
        self.slider_brighness.setOrientation(QtCore.Qt.Horizontal)
        self.slider_brighness.setObjectName("slider_brighness")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1120, 410, 55, 16))
        self.label_4.setStyleSheet("color:white\n"
"")
        self.label_4.setObjectName("label_4")
        self.checkBox_grayImage = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_grayImage.setGeometry(QtCore.QRect(1120, 280, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_grayImage.setFont(font)
        self.checkBox_grayImage.setStyleSheet("color:white\n"
"\n"
"")
        self.checkBox_grayImage.setObjectName("checkBox_grayImage")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1110, 20, 331, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.histogramWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.histogramWidget.setContentsMargins(0, 0, 0, 0)
        self.histogramWidget.setObjectName("histogramWidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1120, 460, 71, 16))
        self.label_5.setStyleSheet("color:white\n"
"")
        self.label_5.setObjectName("label_5")
        self.slider_threshold = QtWidgets.QSlider(self.centralwidget)
        self.slider_threshold.setGeometry(QtCore.QRect(1120, 480, 321, 22))
        self.slider_threshold.setOrientation(QtCore.Qt.Horizontal)
        self.slider_threshold.setObjectName("slider_threshold")
        self.checkbox_invertImage = QtWidgets.QCheckBox(self.centralwidget)
        self.checkbox_invertImage.setGeometry(QtCore.QRect(1360, 280, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkbox_invertImage.setFont(font)
        self.checkbox_invertImage.setStyleSheet("color:white\n"
"\n"
"")
        self.checkbox_invertImage.setObjectName("checkbox_invertImage")
        self.slider_saturation = QtWidgets.QSlider(self.centralwidget)
        self.slider_saturation.setGeometry(QtCore.QRect(1120, 380, 321, 22))
        self.slider_saturation.setAutoFillBackground(False)
        self.slider_saturation.setMinimum(0)
        self.slider_saturation.setMaximum(100)
        self.slider_saturation.setPageStep(10)
        self.slider_saturation.setProperty("value", 50)
        self.slider_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.slider_saturation.setInvertedAppearance(False)
        self.slider_saturation.setInvertedControls(False)
        self.slider_saturation.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.slider_saturation.setTickInterval(4)
        self.slider_saturation.setObjectName("slider_saturation")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1120, 360, 71, 16))
        self.label_6.setStyleSheet("color:white\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(-10, -30, 1501, 891))
        self.label_7.setStyleSheet("background-color:#535353\n"
"\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 20, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:#FFF")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(760, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color:#FFF")
        self.label_11.setObjectName("label_11")
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(1120, 750, 321, 41))
        self.btn_reset.setStyleSheet("background-color:white\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons8-reset-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_reset.setIcon(icon)
        self.btn_reset.setObjectName("btn_reset")
        self.slider_hue = QtWidgets.QSlider(self.centralwidget)
        self.slider_hue.setGeometry(QtCore.QRect(1120, 340, 321, 22))
        self.slider_hue.setMinimum(0)
        self.slider_hue.setMaximum(360)
        self.slider_hue.setPageStep(10)
        self.slider_hue.setProperty("value", 180)
        self.slider_hue.setOrientation(QtCore.Qt.Horizontal)
        self.slider_hue.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slider_hue.setTickInterval(25)
        self.slider_hue.setObjectName("slider_hue")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1120, 310, 55, 16))
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1120, 570, 321, 161))
        self.tabWidget.setObjectName("tabWidget")
        self.Blur = QtWidgets.QWidget()
        self.Blur.setObjectName("Blur")
        self.spinBox = QtWidgets.QSpinBox(self.Blur)
        self.spinBox.setGeometry(QtCore.QRect(150, 0, 51, 31))
        self.spinBox.setSingleStep(2)
        self.spinBox.setObjectName("spinBox")
        self.label_10 = QtWidgets.QLabel(self.Blur)
        self.label_10.setGeometry(QtCore.QRect(90, -1, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.Blur)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 40, 301, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.Blur)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 70, 301, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.Blur)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 100, 301, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.Blur, "")
        self.Sharpen = QtWidgets.QWidget()
        self.Sharpen.setObjectName("Sharpen")
        self.tabWidget.addTab(self.Sharpen, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1120, 520, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:white")
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1150, 220, 101, 28))
        self.pushButton.setStyleSheet("background-color:white")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1300, 220, 101, 28))
        self.pushButton_2.setStyleSheet("background-color:white")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.lbl_photo.raise_()
        self.lbl_newPhoto.raise_()
        self.slider_brighness.raise_()
        self.label_4.raise_()
        self.checkBox_grayImage.raise_()
        self.verticalLayoutWidget.raise_()
        self.label_5.raise_()
        self.slider_threshold.raise_()
        self.checkbox_invertImage.raise_()
        self.slider_saturation.raise_()
        self.label_6.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.btn_reset.raise_()
        self.slider_hue.raise_()
        self.label_2.raise_()
        self.tabWidget.raise_()
        self.label_9.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1465, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuImage = QtWidgets.QMenu(self.menubar)
        self.menuImage.setObjectName("menuImage")
        self.menuEnhancement = QtWidgets.QMenu(self.menubar)
        self.menuEnhancement.setObjectName("menuEnhancement")
        self.menuSmoothing = QtWidgets.QMenu(self.menubar)
        self.menuSmoothing.setObjectName("menuSmoothing")
        self.menuBlur = QtWidgets.QMenu(self.menuSmoothing)
        self.menuBlur.setObjectName("menuBlur")
        self.menuNoise = QtWidgets.QMenu(self.menuSmoothing)
        self.menuNoise.setObjectName("menuNoise")
        self.menuSharpen = QtWidgets.QMenu(self.menuSmoothing)
        self.menuSharpen.setObjectName("menuSharpen")
        self.menuEdge_Detection = QtWidgets.QMenu(self.menuSmoothing)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        self.menuSobel = QtWidgets.QMenu(self.menuEdge_Detection)
        self.menuSobel.setObjectName("menuSobel")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Huyhoang/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setIcon(icon1)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Huyhoang/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Huyhoang/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Huyhoang/Quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionRotation = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons8-3d-rotate-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRotation.setIcon(icon5)
        self.actionRotation.setObjectName("actionRotation")
        self.actionShearing = QtWidgets.QAction(MainWindow)
        self.actionShearing.setObjectName("actionShearing")
        self.actionZoom_in = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/zoom_out_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_in.setIcon(icon6)
        self.actionZoom_in.setObjectName("actionZoom_in")
        self.actionZoom_out = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/zoom_in_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom_out.setIcon(icon7)
        self.actionZoom_out.setObjectName("actionZoom_out")
        self.actionBox = QtWidgets.QAction(MainWindow)
        self.actionBox.setObjectName("actionBox")
        self.actionMedian = QtWidgets.QAction(MainWindow)
        self.actionMedian.setObjectName("actionMedian")
        self.actionGaussian = QtWidgets.QAction(MainWindow)
        self.actionGaussian.setObjectName("actionGaussian")
        self.actionHistogram_equal = QtWidgets.QAction(MainWindow)
        self.actionHistogram_equal.setObjectName("actionHistogram_equal")
        self.actionAdd_Noise = QtWidgets.QAction(MainWindow)
        self.actionAdd_Noise.setObjectName("actionAdd_Noise")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setObjectName("actionLog")
        self.actionGamma = QtWidgets.QAction(MainWindow)
        self.actionGamma.setObjectName("actionGamma")
        self.actionDerivatives = QtWidgets.QAction(MainWindow)
        self.actionDerivatives.setObjectName("actionDerivatives")
        self.actionLaplace = QtWidgets.QAction(MainWindow)
        self.actionLaplace.setObjectName("actionLaplace")
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        self.actionEDSobel = QtWidgets.QAction(MainWindow)
        self.actionEDSobel.setObjectName("actionEDSobel")
        self.actionEDScharr = QtWidgets.QAction(MainWindow)
        self.actionEDScharr.setObjectName("actionEDScharr")
        self.actionEDPrewitt = QtWidgets.QAction(MainWindow)
        self.actionEDPrewitt.setObjectName("actionEDPrewitt")
        self.actionEDRoberts = QtWidgets.QAction(MainWindow)
        self.actionEDRoberts.setObjectName("actionEDRoberts")
        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setObjectName("actionScharr")
        self.actionPrewitt = QtWidgets.QAction(MainWindow)
        self.actionPrewitt.setObjectName("actionPrewitt")
        self.actionRoberts = QtWidgets.QAction(MainWindow)
        self.actionRoberts.setObjectName("actionRoberts")
        self.actionEDHorizontalSobel = QtWidgets.QAction(MainWindow)
        self.actionEDHorizontalSobel.setObjectName("actionEDHorizontalSobel")
        self.actionEDVerticalSobel = QtWidgets.QAction(MainWindow)
        self.actionEDVerticalSobel.setObjectName("actionEDVerticalSobel")
        self.actionEDLaplace_2 = QtWidgets.QAction(MainWindow)
        self.actionEDLaplace_2.setObjectName("actionEDLaplace_2")
        self.actionSobelSharpen = QtWidgets.QAction(MainWindow)
        self.actionSobelSharpen.setObjectName("actionSobelSharpen")
        self.actionLaplaceSharpen = QtWidgets.QAction(MainWindow)
        self.actionLaplaceSharpen.setObjectName("actionLaplaceSharpen")
        self.actionAverage = QtWidgets.QAction(MainWindow)
        self.actionAverage.setObjectName("actionAverage")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuImage.addAction(self.actionRotation)
        self.menuImage.addAction(self.actionShearing)
        self.menuImage.addSeparator()
        self.menuImage.addAction(self.actionZoom_in)
        self.menuImage.addAction(self.actionZoom_out)
        self.menuEnhancement.addAction(self.actionHistogram_equal)
        self.menuEnhancement.addAction(self.actionLog)
        self.menuEnhancement.addAction(self.actionGamma)
        self.menuBlur.addAction(self.actionBox)
        self.menuBlur.addAction(self.actionMedian)
        self.menuBlur.addAction(self.actionGaussian)
        self.menuBlur.addAction(self.actionAverage)
        self.menuNoise.addAction(self.actionAdd_Noise)
        self.menuSharpen.addAction(self.actionSobelSharpen)
        self.menuSharpen.addAction(self.actionLaplaceSharpen)
        self.menuSobel.addAction(self.actionEDHorizontalSobel)
        self.menuSobel.addAction(self.actionEDVerticalSobel)
        self.menuEdge_Detection.addAction(self.menuSobel.menuAction())
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.menuEdge_Detection.addAction(self.actionPrewitt)
        self.menuEdge_Detection.addAction(self.actionRoberts)
        self.menuEdge_Detection.addAction(self.actionEDLaplace_2)
        self.menuSmoothing.addAction(self.menuBlur.menuAction())
        self.menuSmoothing.addAction(self.menuNoise.menuAction())
        self.menuSmoothing.addAction(self.menuSharpen.menuAction())
        self.menuSmoothing.addAction(self.menuEdge_Detection.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menubar.addAction(self.menuEnhancement.menuAction())
        self.menubar.addAction(self.menuSmoothing.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_out)
        self.toolBar.addAction(self.actionZoom_in)
        self.toolBar.addAction(self.actionRotation)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Brighness"))
        self.checkBox_grayImage.setText(_translate("MainWindow", "Ảnh xám"))
        self.label_5.setText(_translate("MainWindow", "Threshold"))
        self.checkbox_invertImage.setText(_translate("MainWindow", "Đảo ảnh"))
        self.label_6.setText(_translate("MainWindow", "Saturation"))
        self.label_8.setText(_translate("MainWindow", "ORIGINAL"))
        self.label_11.setText(_translate("MainWindow", "CHANGE"))
        self.btn_reset.setText(_translate("MainWindow", "Reset"))
        self.label_2.setText(_translate("MainWindow", "Hue"))
        self.label_10.setText(_translate("MainWindow", "SIZE"))
        self.pushButton_3.setText(_translate("MainWindow", "Box"))
        self.pushButton_4.setText(_translate("MainWindow", "Median"))
        self.pushButton_5.setText(_translate("MainWindow", "Gaussian"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Blur), _translate("MainWindow", "Blur"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Sharpen), _translate("MainWindow", "Sharpen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Edge Detection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Segmentation"))
        self.label_9.setText(_translate("MainWindow", "                  Properties"))
        self.pushButton.setText(_translate("MainWindow", "Equalize"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuImage.setTitle(_translate("MainWindow", "Image"))
        self.menuEnhancement.setTitle(_translate("MainWindow", "Enhancement"))
        self.menuSmoothing.setTitle(_translate("MainWindow", "Filter"))
        self.menuBlur.setTitle(_translate("MainWindow", "Blur"))
        self.menuNoise.setTitle(_translate("MainWindow", "Noise"))
        self.menuSharpen.setTitle(_translate("MainWindow", "Sharpen"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuSobel.setTitle(_translate("MainWindow", "Sobel"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionRotation.setText(_translate("MainWindow", "Rotation"))
        self.actionShearing.setText(_translate("MainWindow", "Shearing"))
        self.actionZoom_in.setText(_translate("MainWindow", "Zoom in 10%"))
        self.actionZoom_out.setText(_translate("MainWindow", "Zoom out 10%"))
        self.actionBox.setText(_translate("MainWindow", "Box"))
        self.actionMedian.setText(_translate("MainWindow", "Median"))
        self.actionGaussian.setText(_translate("MainWindow", "Gaussian"))
        self.actionHistogram_equal.setText(_translate("MainWindow", "Histogram equal"))
        self.actionAdd_Noise.setText(_translate("MainWindow", "Add Noise"))
        self.actionLog.setText(_translate("MainWindow", "Logarit"))
        self.actionGamma.setText(_translate("MainWindow", "Gamma"))
        self.actionDerivatives.setText(_translate("MainWindow", "Derivatives"))
        self.actionLaplace.setText(_translate("MainWindow", "Laplace"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionEDSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionEDScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionEDPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionEDRoberts.setText(_translate("MainWindow", "Roberts"))
        self.actionScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionPrewitt.setText(_translate("MainWindow", "Prewitt"))
        self.actionRoberts.setText(_translate("MainWindow", "Roberts"))
        self.actionEDHorizontalSobel.setText(_translate("MainWindow", "Horizontal"))
        self.actionEDVerticalSobel.setText(_translate("MainWindow", "Vertical"))
        self.actionEDLaplace_2.setText(_translate("MainWindow", "Laplace"))
        self.actionSobelSharpen.setText(_translate("MainWindow", "Sobel"))
        self.actionLaplaceSharpen.setText(_translate("MainWindow", "Laplace"))
        self.actionAverage.setText(_translate("MainWindow", "Average"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
