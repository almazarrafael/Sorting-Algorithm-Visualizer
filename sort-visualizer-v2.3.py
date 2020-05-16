from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time
import random

numMS = 0.01

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(25, 30, 16, 441))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(40, 30, 16, 441))
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_2.setProperty("value", 95)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(55, 30, 16, 441))
        self.progressBar_3.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_3.setProperty("value", 90)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(70, 30, 16, 441))
        self.progressBar_4.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_4.setProperty("value", 85)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(85, 30, 16, 441))
        self.progressBar_5.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_5.setProperty("value", 80)
        self.progressBar_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_5.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(100, 30, 16, 441))
        self.progressBar_6.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_6.setProperty("value", 75)
        self.progressBar_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_6.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_6.setObjectName("progressBar_6")
        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(115, 30, 16, 441))
        self.progressBar_7.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_7.setProperty("value", 70)
        self.progressBar_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_7.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_7.setObjectName("progressBar_7")
        self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_8.setGeometry(QtCore.QRect(130, 30, 16, 441))
        self.progressBar_8.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_8.setProperty("value", 65)
        self.progressBar_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_8.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_8.setObjectName("progressBar_8")
        self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_9.setGeometry(QtCore.QRect(145, 30, 16, 441))
        self.progressBar_9.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_9.setProperty("value", 60)
        self.progressBar_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_9.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_9.setObjectName("progressBar_9")
        self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_10.setGeometry(QtCore.QRect(160, 30, 16, 441))
        self.progressBar_10.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_10.setProperty("value", 55)
        self.progressBar_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_10.setTextVisible(False)
        self.progressBar_10.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_10.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_10.setObjectName("progressBar_10")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 5, 311, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 475, 311, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(320, 10, 20, 471))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 10, 20, 471))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 430, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 30, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 100, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 170, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(350, 470, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 468, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(350, 340, 121, 20))
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(100)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 310, 61, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 10, 47, 13))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 240, 121, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 360, 47, 13))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.progressBar_11 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_11.setGeometry(QtCore.QRect(175, 30, 16, 441))
        self.progressBar_11.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_11.setProperty("value", 50)
        self.progressBar_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_11.setTextVisible(False)
        self.progressBar_11.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_11.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_11.setObjectName("progressBar_11")
        self.progressBar_12 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_12.setGeometry(QtCore.QRect(190, 30, 16, 441))
        self.progressBar_12.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_12.setProperty("value", 45)
        self.progressBar_12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_12.setTextVisible(False)
        self.progressBar_12.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_12.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_12.setObjectName("progressBar_12")
        self.progressBar_13 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_13.setGeometry(QtCore.QRect(205, 30, 16, 441))
        self.progressBar_13.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_13.setProperty("value", 40)
        self.progressBar_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_13.setTextVisible(False)
        self.progressBar_13.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_13.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_13.setObjectName("progressBar_13")
        self.progressBar_14 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_14.setGeometry(QtCore.QRect(220, 30, 16, 441))
        self.progressBar_14.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_14.setProperty("value", 35)
        self.progressBar_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_14.setTextVisible(False)
        self.progressBar_14.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_14.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_14.setObjectName("progressBar_14")
        self.progressBar_15 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_15.setGeometry(QtCore.QRect(235, 30, 16, 441))
        self.progressBar_15.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_15.setProperty("value", 30)
        self.progressBar_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_15.setTextVisible(False)
        self.progressBar_15.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_15.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_15.setObjectName("progressBar_15")
        self.progressBar_16 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_16.setGeometry(QtCore.QRect(250, 30, 16, 441))
        self.progressBar_16.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_16.setProperty("value", 25)
        self.progressBar_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_16.setTextVisible(False)
        self.progressBar_16.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_16.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_16.setObjectName("progressBar_16")
        self.progressBar_17 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_17.setGeometry(QtCore.QRect(265, 30, 16, 441))
        self.progressBar_17.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_17.setProperty("value", 20)
        self.progressBar_17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_17.setTextVisible(False)
        self.progressBar_17.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_17.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_17.setObjectName("progressBar_17")
        self.progressBar_18 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_18.setGeometry(QtCore.QRect(280, 30, 16, 441))
        self.progressBar_18.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_18.setProperty("value", 15)
        self.progressBar_18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_18.setTextVisible(False)
        self.progressBar_18.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_18.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_18.setObjectName("progressBar_18")
        self.progressBar_19 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_19.setGeometry(QtCore.QRect(295, 30, 16, 441))
        self.progressBar_19.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_19.setProperty("value", 10)
        self.progressBar_19.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_19.setTextVisible(False)
        self.progressBar_19.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_19.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_19.setObjectName("progressBar_19")
        self.progressBar_20 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_20.setGeometry(QtCore.QRect(310, 30, 16, 441))
        self.progressBar_20.setStyleSheet("QProgressBar {\n"
"    background-color : rgba(0, 0, 0, 0);\n"
"    border : 1px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    \n"
"    \n"
"    background-color: rgb(85, 255, 0);\n"
"    border: 1px solid black;\n"
"}")
        self.progressBar_20.setProperty("value", 5)
        self.progressBar_20.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_20.setTextVisible(False)
        self.progressBar_20.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_20.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_20.setObjectName("progressBar_20")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 395, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 486, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.horizontalSlider.valueChanged.connect(self.updateSpeed)
        self.pushButton.clicked.connect(self.generateRandom)
        self.pushButton_2.clicked.connect(self.bubbleSort)
        self.pushButton_3.clicked.connect(self.insertionSort)
        self.pushButton_4.clicked.connect(self.selectionSort)
        self.pushButton_5.clicked.connect(self.shellSort)
        self.pushButton_6.clicked.connect(self.generateDescending)

    def updateSpeed(self):
        global numMS
        numMS = self.horizontalSlider.value() * 0.001
        self.label_5.setText(str(self.horizontalSlider.value()))

    def bubbleSort(self):
        global numMS
        self.label_2.setText("Bubble Sorting...")
        arr = [self.progressBar.value(), self.progressBar_2.value(), self.progressBar_3.value(), self.progressBar_4.value(), self.progressBar_5.value(), self.progressBar_6.value(), self.progressBar_7.value(), self.progressBar_8.value(), self.progressBar_9.value(), self.progressBar_10.value(), self.progressBar_11.value(), self.progressBar_12.value(), self.progressBar_13.value(), self.progressBar_14.value(), self.progressBar_15.value(), self.progressBar_16.value(), self.progressBar_17.value(), self.progressBar_18.value(), self.progressBar_19.value(), self.progressBar_20.value()]
        arr1 = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4, self.progressBar_5, self.progressBar_6, self.progressBar_7, self.progressBar_8, self.progressBar_9, self.progressBar_10, self.progressBar_11, self.progressBar_12, self.progressBar_13, self.progressBar_14, self.progressBar_15, self.progressBar_16, self.progressBar_17, self.progressBar_18, self.progressBar_19, self.progressBar_20]
        
        n = len(arr)
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                    if arr[j] > arr[j+1] : 
                        time.sleep(numMS)
                        arr1[j].setValue(arr[j+1])
                        arr1[j+1].setValue(arr[j])
                        arr[j], arr[j+1] = arr[j+1], arr[j]

        self.label_2.setText("Idle")

    def insertionSort(self):
        global numMS
        self.label_2.setText("Insertion Sorting...")
        arr = [self.progressBar.value(), self.progressBar_2.value(), self.progressBar_3.value(), self.progressBar_4.value(), self.progressBar_5.value(), self.progressBar_6.value(), self.progressBar_7.value(), self.progressBar_8.value(), self.progressBar_9.value(), self.progressBar_10.value(), self.progressBar_11.value(), self.progressBar_12.value(), self.progressBar_13.value(), self.progressBar_14.value(), self.progressBar_15.value(), self.progressBar_16.value(), self.progressBar_17.value(), self.progressBar_18.value(), self.progressBar_19.value(), self.progressBar_20.value()]
        arr1 = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4, self.progressBar_5, self.progressBar_6, self.progressBar_7, self.progressBar_8, self.progressBar_9, self.progressBar_10, self.progressBar_11, self.progressBar_12, self.progressBar_13, self.progressBar_14, self.progressBar_15, self.progressBar_16, self.progressBar_17, self.progressBar_18, self.progressBar_19, self.progressBar_20]
        
        for i in range(1, len(arr)): 
            key = arr[i]  
            j = i-1
            while j >=0 and key < arr[j]:
                    arr[j+1] = arr[j]
                    arr1[j+1].setValue(arr[j])
                    time.sleep(numMS)
                    j -= 1
            arr[j+1] = key
            arr1[j+1].setValue(key)
        
        self.label_2.setText("Idle")

    def selectionSort(self):
        global numMS
        self.label_2.setText("Selection Sorting...")
        arr = [self.progressBar.value(), self.progressBar_2.value(), self.progressBar_3.value(), self.progressBar_4.value(), self.progressBar_5.value(), self.progressBar_6.value(), self.progressBar_7.value(), self.progressBar_8.value(), self.progressBar_9.value(), self.progressBar_10.value(), self.progressBar_11.value(), self.progressBar_12.value(), self.progressBar_13.value(), self.progressBar_14.value(), self.progressBar_15.value(), self.progressBar_16.value(), self.progressBar_17.value(), self.progressBar_18.value(), self.progressBar_19.value(), self.progressBar_20.value()]
        arr1 = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4, self.progressBar_5, self.progressBar_6, self.progressBar_7, self.progressBar_8, self.progressBar_9, self.progressBar_10, self.progressBar_11, self.progressBar_12, self.progressBar_13, self.progressBar_14, self.progressBar_15, self.progressBar_16, self.progressBar_17, self.progressBar_18, self.progressBar_19, self.progressBar_20]
        
        for i in range(len(arr)): 
            min_idx = i 
            for j in range(i+1, len(arr)): 
                if arr[min_idx] > arr[j]: 
                    min_idx = j
            arr1[i].setValue(arr[min_idx])
            arr1[min_idx].setValue(arr[i])   
            arr[i], arr[min_idx] = arr[min_idx], arr[i] 
            time.sleep(numMS)
        
        self.label_2.setText("Idle")

    def shellSort(self):
        global numMS
        self.label_2.setText("Shell Sorting...")
        arr = [self.progressBar.value(), self.progressBar_2.value(), self.progressBar_3.value(), self.progressBar_4.value(), self.progressBar_5.value(), self.progressBar_6.value(), self.progressBar_7.value(), self.progressBar_8.value(), self.progressBar_9.value(), self.progressBar_10.value(), self.progressBar_11.value(), self.progressBar_12.value(), self.progressBar_13.value(), self.progressBar_14.value(), self.progressBar_15.value(), self.progressBar_16.value(), self.progressBar_17.value(), self.progressBar_18.value(), self.progressBar_19.value(), self.progressBar_20.value()]
        arr1 = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4, self.progressBar_5, self.progressBar_6, self.progressBar_7, self.progressBar_8, self.progressBar_9, self.progressBar_10, self.progressBar_11, self.progressBar_12, self.progressBar_13, self.progressBar_14, self.progressBar_15, self.progressBar_16, self.progressBar_17, self.progressBar_18, self.progressBar_19, self.progressBar_20]
        
        n = len(arr) 
        gap = n//2

        while gap > 0: 
            for i in range(gap,n): 
                temp = arr[i] 
                j = i 
                while  j >= gap and arr[j-gap] >temp:
                    time.sleep(numMS)
                    arr1[j].setValue(arr[j-gap])
                    arr[j] = arr[j-gap] 
                    j -= gap 
                time.sleep(numMS)
                arr1[j].setValue(temp)
                arr[j] = temp 
            gap //= 2

        self.label_2.setText("Idle")

    def generateDescending(self):
        global numMS
        self.label_2.setText("Generating...")
        arr1 = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4, self.progressBar_5, self.progressBar_6, self.progressBar_7, self.progressBar_8, self.progressBar_9, self.progressBar_10, self.progressBar_11, self.progressBar_12, self.progressBar_13, self.progressBar_14, self.progressBar_15, self.progressBar_16, self.progressBar_17, self.progressBar_18, self.progressBar_19, self.progressBar_20]
        curr = 100
        for i in range(len(arr1)):
            time.sleep(numMS)
            arr1[i].setValue(curr - (5*i))
        self.label_2.setText("Idle")

    def generateRandom(self):
        global numMS
        self.label_2.setText("Generating...")
        arr1 = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4, self.progressBar_5, self.progressBar_6, self.progressBar_7, self.progressBar_8, self.progressBar_9, self.progressBar_10, self.progressBar_11, self.progressBar_12, self.progressBar_13, self.progressBar_14, self.progressBar_15, self.progressBar_16, self.progressBar_17, self.progressBar_18, self.progressBar_19, self.progressBar_20]
        for i in range(len(arr1)):
            time.sleep(numMS)
            arr1[i].setValue(random.randint(0, 101))
        self.label_2.setText("Idle")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sort Visualizer - Rafael Almazar"))
        self.progressBar.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_2.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_3.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_4.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_5.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_6.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_7.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_8.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_9.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_10.setFormat(_translate("MainWindow", "%p"))
        self.pushButton.setText(_translate("MainWindow", "Generate Random"))
        self.pushButton_2.setText(_translate("MainWindow", "Bubble Sort"))
        self.pushButton_3.setText(_translate("MainWindow", "Insertion Sort"))
        self.pushButton_4.setText(_translate("MainWindow", "Selection Sort"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.label_2.setText(_translate("MainWindow", "Idle"))
        self.label_3.setText(_translate("MainWindow", "Speed (ms):"))
        self.label_4.setText(_translate("MainWindow", "Sorts:"))
        self.pushButton_5.setText(_translate("MainWindow", "Shell Sort"))
        self.label_5.setText(_translate("MainWindow", "100"))
        self.progressBar_11.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_12.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_13.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_14.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_15.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_16.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_17.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_18.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_19.setFormat(_translate("MainWindow", "%p"))
        self.progressBar_20.setFormat(_translate("MainWindow", "%p"))
        self.pushButton_6.setText(_translate("MainWindow", "Generate Descending"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
