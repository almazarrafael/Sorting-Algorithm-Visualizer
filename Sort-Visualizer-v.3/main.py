from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time
import random

class Ui_MainWindow(object):
    numMS = 0.001

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1182, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bar1 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar1.setGeometry(QtCore.QRect(20, 30, 11, 441))
        self.bar1.setStyleSheet("QProgressBar {\n"
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
        self.bar1.setProperty("value", 100)
        self.bar1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar1.setTextVisible(False)
        self.bar1.setOrientation(QtCore.Qt.Vertical)
        self.bar1.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar1.setObjectName("bar1")
        self.bar2 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar2.setGeometry(QtCore.QRect(30, 30, 11, 441))
        self.bar2.setStyleSheet("QProgressBar {\n"
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
        self.bar2.setProperty("value", 99)
        self.bar2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar2.setTextVisible(False)
        self.bar2.setOrientation(QtCore.Qt.Vertical)
        self.bar2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar2.setObjectName("bar2")
        self.bar3 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar3.setGeometry(QtCore.QRect(40, 30, 11, 441))
        self.bar3.setStyleSheet("QProgressBar {\n"
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
        self.bar3.setProperty("value", 98)
        self.bar3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar3.setTextVisible(False)
        self.bar3.setOrientation(QtCore.Qt.Vertical)
        self.bar3.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar3.setObjectName("bar3")
        self.bar4 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar4.setGeometry(QtCore.QRect(50, 30, 11, 441))
        self.bar4.setStyleSheet("QProgressBar {\n"
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
        self.bar4.setProperty("value", 97)
        self.bar4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar4.setTextVisible(False)
        self.bar4.setOrientation(QtCore.Qt.Vertical)
        self.bar4.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar4.setObjectName("bar4")
        self.bar5 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar5.setGeometry(QtCore.QRect(60, 30, 11, 441))
        self.bar5.setStyleSheet("QProgressBar {\n"
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
        self.bar5.setProperty("value", 96)
        self.bar5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar5.setTextVisible(False)
        self.bar5.setOrientation(QtCore.Qt.Vertical)
        self.bar5.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar5.setObjectName("bar5")
        self.bar6 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar6.setGeometry(QtCore.QRect(70, 30, 11, 441))
        self.bar6.setStyleSheet("QProgressBar {\n"
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
        self.bar6.setProperty("value", 95)
        self.bar6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar6.setTextVisible(False)
        self.bar6.setOrientation(QtCore.Qt.Vertical)
        self.bar6.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar6.setObjectName("bar6")
        self.bar7 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar7.setGeometry(QtCore.QRect(80, 30, 11, 441))
        self.bar7.setStyleSheet("QProgressBar {\n"
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
        self.bar7.setProperty("value", 94)
        self.bar7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar7.setTextVisible(False)
        self.bar7.setOrientation(QtCore.Qt.Vertical)
        self.bar7.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar7.setObjectName("bar7")
        self.bar8 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar8.setGeometry(QtCore.QRect(90, 30, 11, 441))
        self.bar8.setStyleSheet("QProgressBar {\n"
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
        self.bar8.setProperty("value", 93)
        self.bar8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar8.setTextVisible(False)
        self.bar8.setOrientation(QtCore.Qt.Vertical)
        self.bar8.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar8.setObjectName("bar8")
        self.bar9 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar9.setGeometry(QtCore.QRect(100, 30, 11, 441))
        self.bar9.setStyleSheet("QProgressBar {\n"
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
        self.bar9.setProperty("value", 92)
        self.bar9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar9.setTextVisible(False)
        self.bar9.setOrientation(QtCore.Qt.Vertical)
        self.bar9.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar9.setObjectName("bar9")
        self.bar10 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar10.setGeometry(QtCore.QRect(110, 30, 11, 441))
        self.bar10.setStyleSheet("QProgressBar {\n"
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
        self.bar10.setProperty("value", 91)
        self.bar10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar10.setTextVisible(False)
        self.bar10.setOrientation(QtCore.Qt.Vertical)
        self.bar10.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar10.setObjectName("bar10")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1050, 415, 121, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1050, 40, 121, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1050, 70, 121, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(1050, 100, 121, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1050, 460, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1100, 458, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(1050, 330, 121, 20))
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(1000)
        self.horizontalSlider.setSingleStep(100)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1050, 300, 61, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1050, 20, 47, 13))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1050, 130, 121, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1080, 350, 47, 13))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(1050, 385, 121, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.bar11 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar11.setGeometry(QtCore.QRect(120, 30, 11, 441))
        self.bar11.setStyleSheet("QProgressBar {\n"
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
        self.bar11.setProperty("value", 90)
        self.bar11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar11.setTextVisible(False)
        self.bar11.setOrientation(QtCore.Qt.Vertical)
        self.bar11.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar11.setObjectName("bar11")
        self.bar18 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar18.setGeometry(QtCore.QRect(190, 30, 11, 441))
        self.bar18.setStyleSheet("QProgressBar {\n"
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
        self.bar18.setProperty("value", 83)
        self.bar18.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar18.setTextVisible(False)
        self.bar18.setOrientation(QtCore.Qt.Vertical)
        self.bar18.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar18.setObjectName("bar18")
        self.bar19 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar19.setGeometry(QtCore.QRect(200, 30, 11, 441))
        self.bar19.setStyleSheet("QProgressBar {\n"
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
        self.bar19.setProperty("value", 82)
        self.bar19.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar19.setTextVisible(False)
        self.bar19.setOrientation(QtCore.Qt.Vertical)
        self.bar19.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar19.setObjectName("bar19")
        self.bar12 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar12.setGeometry(QtCore.QRect(130, 30, 11, 441))
        self.bar12.setStyleSheet("QProgressBar {\n"
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
        self.bar12.setProperty("value", 89)
        self.bar12.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar12.setTextVisible(False)
        self.bar12.setOrientation(QtCore.Qt.Vertical)
        self.bar12.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar12.setObjectName("bar12")
        self.bar15 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar15.setGeometry(QtCore.QRect(160, 30, 11, 441))
        self.bar15.setStyleSheet("QProgressBar {\n"
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
        self.bar15.setProperty("value", 86)
        self.bar15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar15.setTextVisible(False)
        self.bar15.setOrientation(QtCore.Qt.Vertical)
        self.bar15.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar15.setObjectName("bar15")
        self.bar20 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar20.setGeometry(QtCore.QRect(210, 30, 11, 441))
        self.bar20.setStyleSheet("QProgressBar {\n"
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
        self.bar20.setProperty("value", 81)
        self.bar20.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar20.setTextVisible(False)
        self.bar20.setOrientation(QtCore.Qt.Vertical)
        self.bar20.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar20.setObjectName("bar20")
        self.bar16 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar16.setGeometry(QtCore.QRect(170, 30, 11, 441))
        self.bar16.setStyleSheet("QProgressBar {\n"
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
        self.bar16.setProperty("value", 85)
        self.bar16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar16.setTextVisible(False)
        self.bar16.setOrientation(QtCore.Qt.Vertical)
        self.bar16.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar16.setObjectName("bar16")
        self.bar17 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar17.setGeometry(QtCore.QRect(180, 30, 11, 441))
        self.bar17.setStyleSheet("QProgressBar {\n"
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
        self.bar17.setProperty("value", 84)
        self.bar17.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar17.setTextVisible(False)
        self.bar17.setOrientation(QtCore.Qt.Vertical)
        self.bar17.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar17.setObjectName("bar17")
        self.bar14 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar14.setGeometry(QtCore.QRect(150, 30, 11, 441))
        self.bar14.setStyleSheet("QProgressBar {\n"
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
        self.bar14.setProperty("value", 87)
        self.bar14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar14.setTextVisible(False)
        self.bar14.setOrientation(QtCore.Qt.Vertical)
        self.bar14.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar14.setObjectName("bar14")
        self.bar13 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar13.setGeometry(QtCore.QRect(140, 30, 11, 441))
        self.bar13.setStyleSheet("QProgressBar {\n"
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
        self.bar13.setProperty("value", 88)
        self.bar13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar13.setTextVisible(False)
        self.bar13.setOrientation(QtCore.Qt.Vertical)
        self.bar13.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar13.setObjectName("bar13")
        self.bar27 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar27.setGeometry(QtCore.QRect(280, 30, 11, 441))
        self.bar27.setStyleSheet("QProgressBar {\n"
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
        self.bar27.setProperty("value", 74)
        self.bar27.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar27.setTextVisible(False)
        self.bar27.setOrientation(QtCore.Qt.Vertical)
        self.bar27.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar27.setObjectName("bar27")
        self.bar30 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar30.setGeometry(QtCore.QRect(310, 30, 11, 441))
        self.bar30.setStyleSheet("QProgressBar {\n"
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
        self.bar30.setProperty("value", 71)
        self.bar30.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar30.setTextVisible(False)
        self.bar30.setOrientation(QtCore.Qt.Vertical)
        self.bar30.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar30.setObjectName("bar30")
        self.bar35 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar35.setGeometry(QtCore.QRect(360, 30, 11, 441))
        self.bar35.setStyleSheet("QProgressBar {\n"
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
        self.bar35.setProperty("value", 66)
        self.bar35.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar35.setTextVisible(False)
        self.bar35.setOrientation(QtCore.Qt.Vertical)
        self.bar35.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar35.setObjectName("bar35")
        self.bar32 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar32.setGeometry(QtCore.QRect(330, 30, 11, 441))
        self.bar32.setStyleSheet("QProgressBar {\n"
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
        self.bar32.setProperty("value", 69)
        self.bar32.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar32.setTextVisible(False)
        self.bar32.setOrientation(QtCore.Qt.Vertical)
        self.bar32.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar32.setObjectName("bar32")
        self.bar33 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar33.setGeometry(QtCore.QRect(340, 30, 11, 441))
        self.bar33.setStyleSheet("QProgressBar {\n"
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
        self.bar33.setProperty("value", 68)
        self.bar33.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar33.setTextVisible(False)
        self.bar33.setOrientation(QtCore.Qt.Vertical)
        self.bar33.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar33.setObjectName("bar33")
        self.bar40 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar40.setGeometry(QtCore.QRect(410, 30, 11, 441))
        self.bar40.setStyleSheet("QProgressBar {\n"
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
        self.bar40.setProperty("value", 61)
        self.bar40.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar40.setTextVisible(False)
        self.bar40.setOrientation(QtCore.Qt.Vertical)
        self.bar40.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar40.setObjectName("bar40")
        self.bar28 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar28.setGeometry(QtCore.QRect(290, 30, 11, 441))
        self.bar28.setStyleSheet("QProgressBar {\n"
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
        self.bar28.setProperty("value", 73)
        self.bar28.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar28.setTextVisible(False)
        self.bar28.setOrientation(QtCore.Qt.Vertical)
        self.bar28.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar28.setObjectName("bar28")
        self.bar21 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar21.setGeometry(QtCore.QRect(220, 30, 11, 441))
        self.bar21.setStyleSheet("QProgressBar {\n"
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
        self.bar21.setProperty("value", 80)
        self.bar21.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar21.setTextVisible(False)
        self.bar21.setOrientation(QtCore.Qt.Vertical)
        self.bar21.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar21.setObjectName("bar21")
        self.bar34 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar34.setGeometry(QtCore.QRect(350, 30, 11, 441))
        self.bar34.setStyleSheet("QProgressBar {\n"
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
        self.bar34.setProperty("value", 67)
        self.bar34.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar34.setTextVisible(False)
        self.bar34.setOrientation(QtCore.Qt.Vertical)
        self.bar34.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar34.setObjectName("bar34")
        self.bar39 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar39.setGeometry(QtCore.QRect(400, 30, 11, 441))
        self.bar39.setStyleSheet("QProgressBar {\n"
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
        self.bar39.setProperty("value", 62)
        self.bar39.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar39.setTextVisible(False)
        self.bar39.setOrientation(QtCore.Qt.Vertical)
        self.bar39.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar39.setObjectName("bar39")
        self.bar29 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar29.setGeometry(QtCore.QRect(300, 30, 11, 441))
        self.bar29.setStyleSheet("QProgressBar {\n"
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
        self.bar29.setProperty("value", 72)
        self.bar29.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar29.setTextVisible(False)
        self.bar29.setOrientation(QtCore.Qt.Vertical)
        self.bar29.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar29.setObjectName("bar29")
        self.bar38 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar38.setGeometry(QtCore.QRect(390, 30, 11, 441))
        self.bar38.setStyleSheet("QProgressBar {\n"
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
        self.bar38.setProperty("value", 63)
        self.bar38.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar38.setTextVisible(False)
        self.bar38.setOrientation(QtCore.Qt.Vertical)
        self.bar38.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar38.setObjectName("bar38")
        self.bar24 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar24.setGeometry(QtCore.QRect(250, 30, 11, 441))
        self.bar24.setStyleSheet("QProgressBar {\n"
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
        self.bar24.setProperty("value", 77)
        self.bar24.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar24.setTextVisible(False)
        self.bar24.setOrientation(QtCore.Qt.Vertical)
        self.bar24.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar24.setObjectName("bar24")
        self.bar25 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar25.setGeometry(QtCore.QRect(260, 30, 11, 441))
        self.bar25.setStyleSheet("QProgressBar {\n"
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
        self.bar25.setProperty("value", 76)
        self.bar25.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar25.setTextVisible(False)
        self.bar25.setOrientation(QtCore.Qt.Vertical)
        self.bar25.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar25.setObjectName("bar25")
        self.bar36 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar36.setGeometry(QtCore.QRect(370, 30, 11, 441))
        self.bar36.setStyleSheet("QProgressBar {\n"
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
        self.bar36.setProperty("value", 65)
        self.bar36.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar36.setTextVisible(False)
        self.bar36.setOrientation(QtCore.Qt.Vertical)
        self.bar36.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar36.setObjectName("bar36")
        self.bar23 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar23.setGeometry(QtCore.QRect(240, 30, 11, 441))
        self.bar23.setStyleSheet("QProgressBar {\n"
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
        self.bar23.setProperty("value", 78)
        self.bar23.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar23.setTextVisible(False)
        self.bar23.setOrientation(QtCore.Qt.Vertical)
        self.bar23.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar23.setObjectName("bar23")
        self.bar22 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar22.setGeometry(QtCore.QRect(230, 30, 11, 441))
        self.bar22.setStyleSheet("QProgressBar {\n"
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
        self.bar22.setProperty("value", 79)
        self.bar22.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar22.setTextVisible(False)
        self.bar22.setOrientation(QtCore.Qt.Vertical)
        self.bar22.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar22.setObjectName("bar22")
        self.bar31 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar31.setGeometry(QtCore.QRect(320, 30, 11, 441))
        self.bar31.setStyleSheet("QProgressBar {\n"
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
        self.bar31.setProperty("value", 70)
        self.bar31.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar31.setTextVisible(False)
        self.bar31.setOrientation(QtCore.Qt.Vertical)
        self.bar31.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar31.setObjectName("bar31")
        self.bar37 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar37.setGeometry(QtCore.QRect(380, 30, 11, 441))
        self.bar37.setStyleSheet("QProgressBar {\n"
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
        self.bar37.setProperty("value", 64)
        self.bar37.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar37.setTextVisible(False)
        self.bar37.setOrientation(QtCore.Qt.Vertical)
        self.bar37.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar37.setObjectName("bar37")
        self.bar26 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar26.setGeometry(QtCore.QRect(270, 30, 11, 441))
        self.bar26.setStyleSheet("QProgressBar {\n"
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
        self.bar26.setProperty("value", 75)
        self.bar26.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar26.setTextVisible(False)
        self.bar26.setOrientation(QtCore.Qt.Vertical)
        self.bar26.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar26.setObjectName("bar26")
        self.bar72 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar72.setGeometry(QtCore.QRect(730, 30, 11, 441))
        self.bar72.setStyleSheet("QProgressBar {\n"
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
        self.bar72.setProperty("value", 29)
        self.bar72.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar72.setTextVisible(False)
        self.bar72.setOrientation(QtCore.Qt.Vertical)
        self.bar72.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar72.setObjectName("bar72")
        self.bar78 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar78.setGeometry(QtCore.QRect(790, 30, 11, 441))
        self.bar78.setStyleSheet("QProgressBar {\n"
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
        self.bar78.setProperty("value", 23)
        self.bar78.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar78.setTextVisible(False)
        self.bar78.setOrientation(QtCore.Qt.Vertical)
        self.bar78.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar78.setObjectName("bar78")
        self.bar68 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar68.setGeometry(QtCore.QRect(690, 30, 11, 441))
        self.bar68.setStyleSheet("QProgressBar {\n"
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
        self.bar68.setProperty("value", 33)
        self.bar68.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar68.setTextVisible(False)
        self.bar68.setOrientation(QtCore.Qt.Vertical)
        self.bar68.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar68.setObjectName("bar68")
        self.bar45 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar45.setGeometry(QtCore.QRect(460, 30, 11, 441))
        self.bar45.setStyleSheet("QProgressBar {\n"
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
        self.bar45.setProperty("value", 56)
        self.bar45.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar45.setTextVisible(False)
        self.bar45.setOrientation(QtCore.Qt.Vertical)
        self.bar45.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar45.setObjectName("bar45")
        self.bar71 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar71.setGeometry(QtCore.QRect(720, 30, 11, 441))
        self.bar71.setStyleSheet("QProgressBar {\n"
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
        self.bar71.setProperty("value", 30)
        self.bar71.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar71.setTextVisible(False)
        self.bar71.setOrientation(QtCore.Qt.Vertical)
        self.bar71.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar71.setObjectName("bar71")
        self.bar55 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar55.setGeometry(QtCore.QRect(560, 30, 11, 441))
        self.bar55.setStyleSheet("QProgressBar {\n"
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
        self.bar55.setProperty("value", 46)
        self.bar55.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar55.setTextVisible(False)
        self.bar55.setOrientation(QtCore.Qt.Vertical)
        self.bar55.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar55.setObjectName("bar55")
        self.bar64 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar64.setGeometry(QtCore.QRect(650, 30, 11, 441))
        self.bar64.setStyleSheet("QProgressBar {\n"
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
        self.bar64.setProperty("value", 37)
        self.bar64.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar64.setTextVisible(False)
        self.bar64.setOrientation(QtCore.Qt.Vertical)
        self.bar64.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar64.setObjectName("bar64")
        self.bar47 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar47.setGeometry(QtCore.QRect(480, 30, 11, 441))
        self.bar47.setStyleSheet("QProgressBar {\n"
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
        self.bar47.setProperty("value", 54)
        self.bar47.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar47.setTextVisible(False)
        self.bar47.setOrientation(QtCore.Qt.Vertical)
        self.bar47.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar47.setObjectName("bar47")
        self.bar43 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar43.setGeometry(QtCore.QRect(440, 30, 11, 441))
        self.bar43.setStyleSheet("QProgressBar {\n"
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
        self.bar43.setProperty("value", 58)
        self.bar43.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar43.setTextVisible(False)
        self.bar43.setOrientation(QtCore.Qt.Vertical)
        self.bar43.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar43.setObjectName("bar43")
        self.bar77 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar77.setGeometry(QtCore.QRect(780, 30, 11, 441))
        self.bar77.setStyleSheet("QProgressBar {\n"
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
        self.bar77.setProperty("value", 24)
        self.bar77.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar77.setTextVisible(False)
        self.bar77.setOrientation(QtCore.Qt.Vertical)
        self.bar77.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar77.setObjectName("bar77")
        self.bar73 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar73.setGeometry(QtCore.QRect(740, 30, 11, 441))
        self.bar73.setStyleSheet("QProgressBar {\n"
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
        self.bar73.setProperty("value", 28)
        self.bar73.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar73.setTextVisible(False)
        self.bar73.setOrientation(QtCore.Qt.Vertical)
        self.bar73.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar73.setObjectName("bar73")
        self.bar62 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar62.setGeometry(QtCore.QRect(630, 30, 11, 441))
        self.bar62.setStyleSheet("QProgressBar {\n"
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
        self.bar62.setProperty("value", 39)
        self.bar62.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar62.setTextVisible(False)
        self.bar62.setOrientation(QtCore.Qt.Vertical)
        self.bar62.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar62.setObjectName("bar62")
        self.bar67 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar67.setGeometry(QtCore.QRect(680, 30, 11, 441))
        self.bar67.setStyleSheet("QProgressBar {\n"
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
        self.bar67.setProperty("value", 34)
        self.bar67.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar67.setTextVisible(False)
        self.bar67.setOrientation(QtCore.Qt.Vertical)
        self.bar67.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar67.setObjectName("bar67")
        self.bar46 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar46.setGeometry(QtCore.QRect(470, 30, 11, 441))
        self.bar46.setStyleSheet("QProgressBar {\n"
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
        self.bar46.setProperty("value", 55)
        self.bar46.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar46.setTextVisible(False)
        self.bar46.setOrientation(QtCore.Qt.Vertical)
        self.bar46.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar46.setObjectName("bar46")
        self.bar56 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar56.setGeometry(QtCore.QRect(570, 30, 11, 441))
        self.bar56.setStyleSheet("QProgressBar {\n"
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
        self.bar56.setProperty("value", 45)
        self.bar56.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar56.setTextVisible(False)
        self.bar56.setOrientation(QtCore.Qt.Vertical)
        self.bar56.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar56.setObjectName("bar56")
        self.bar80 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar80.setGeometry(QtCore.QRect(810, 30, 11, 441))
        self.bar80.setStyleSheet("QProgressBar {\n"
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
        self.bar80.setProperty("value", 21)
        self.bar80.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar80.setTextVisible(False)
        self.bar80.setOrientation(QtCore.Qt.Vertical)
        self.bar80.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar80.setObjectName("bar80")
        self.bar60 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar60.setGeometry(QtCore.QRect(610, 30, 11, 441))
        self.bar60.setStyleSheet("QProgressBar {\n"
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
        self.bar60.setProperty("value", 41)
        self.bar60.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar60.setTextVisible(False)
        self.bar60.setOrientation(QtCore.Qt.Vertical)
        self.bar60.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar60.setObjectName("bar60")
        self.bar75 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar75.setGeometry(QtCore.QRect(760, 30, 11, 441))
        self.bar75.setStyleSheet("QProgressBar {\n"
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
        self.bar75.setProperty("value", 26)
        self.bar75.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar75.setTextVisible(False)
        self.bar75.setOrientation(QtCore.Qt.Vertical)
        self.bar75.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar75.setObjectName("bar75")
        self.bar79 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar79.setGeometry(QtCore.QRect(800, 30, 11, 441))
        self.bar79.setStyleSheet("QProgressBar {\n"
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
        self.bar79.setProperty("value", 22)
        self.bar79.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar79.setTextVisible(False)
        self.bar79.setOrientation(QtCore.Qt.Vertical)
        self.bar79.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar79.setObjectName("bar79")
        self.bar70 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar70.setGeometry(QtCore.QRect(710, 30, 11, 441))
        self.bar70.setStyleSheet("QProgressBar {\n"
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
        self.bar70.setProperty("value", 31)
        self.bar70.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar70.setTextVisible(False)
        self.bar70.setOrientation(QtCore.Qt.Vertical)
        self.bar70.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar70.setObjectName("bar70")
        self.bar50 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar50.setGeometry(QtCore.QRect(510, 30, 11, 441))
        self.bar50.setStyleSheet("QProgressBar {\n"
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
        self.bar50.setProperty("value", 51)
        self.bar50.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar50.setTextVisible(False)
        self.bar50.setOrientation(QtCore.Qt.Vertical)
        self.bar50.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar50.setObjectName("bar50")
        self.bar61 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar61.setGeometry(QtCore.QRect(620, 30, 11, 441))
        self.bar61.setStyleSheet("QProgressBar {\n"
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
        self.bar61.setProperty("value", 40)
        self.bar61.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar61.setTextVisible(False)
        self.bar61.setOrientation(QtCore.Qt.Vertical)
        self.bar61.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar61.setObjectName("bar61")
        self.bar53 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar53.setGeometry(QtCore.QRect(540, 30, 11, 441))
        self.bar53.setStyleSheet("QProgressBar {\n"
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
        self.bar53.setProperty("value", 48)
        self.bar53.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar53.setTextVisible(False)
        self.bar53.setOrientation(QtCore.Qt.Vertical)
        self.bar53.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar53.setObjectName("bar53")
        self.bar52 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar52.setGeometry(QtCore.QRect(530, 30, 11, 441))
        self.bar52.setStyleSheet("QProgressBar {\n"
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
        self.bar52.setProperty("value", 49)
        self.bar52.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar52.setTextVisible(False)
        self.bar52.setOrientation(QtCore.Qt.Vertical)
        self.bar52.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar52.setObjectName("bar52")
        self.bar66 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar66.setGeometry(QtCore.QRect(670, 30, 11, 441))
        self.bar66.setStyleSheet("QProgressBar {\n"
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
        self.bar66.setProperty("value", 35)
        self.bar66.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar66.setTextVisible(False)
        self.bar66.setOrientation(QtCore.Qt.Vertical)
        self.bar66.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar66.setObjectName("bar66")
        self.bar48 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar48.setGeometry(QtCore.QRect(490, 30, 11, 441))
        self.bar48.setStyleSheet("QProgressBar {\n"
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
        self.bar48.setProperty("value", 53)
        self.bar48.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar48.setTextVisible(False)
        self.bar48.setOrientation(QtCore.Qt.Vertical)
        self.bar48.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar48.setObjectName("bar48")
        self.bar49 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar49.setGeometry(QtCore.QRect(500, 30, 11, 441))
        self.bar49.setStyleSheet("QProgressBar {\n"
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
        self.bar49.setProperty("value", 52)
        self.bar49.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar49.setTextVisible(False)
        self.bar49.setOrientation(QtCore.Qt.Vertical)
        self.bar49.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar49.setObjectName("bar49")
        self.bar63 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar63.setGeometry(QtCore.QRect(640, 30, 11, 441))
        self.bar63.setStyleSheet("QProgressBar {\n"
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
        self.bar63.setProperty("value", 38)
        self.bar63.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar63.setTextVisible(False)
        self.bar63.setOrientation(QtCore.Qt.Vertical)
        self.bar63.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar63.setObjectName("bar63")
        self.bar51 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar51.setGeometry(QtCore.QRect(520, 30, 11, 441))
        self.bar51.setStyleSheet("QProgressBar {\n"
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
        self.bar51.setProperty("value", 50)
        self.bar51.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar51.setTextVisible(False)
        self.bar51.setOrientation(QtCore.Qt.Vertical)
        self.bar51.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar51.setObjectName("bar51")
        self.bar54 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar54.setGeometry(QtCore.QRect(550, 30, 11, 441))
        self.bar54.setStyleSheet("QProgressBar {\n"
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
        self.bar54.setProperty("value", 47)
        self.bar54.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar54.setTextVisible(False)
        self.bar54.setOrientation(QtCore.Qt.Vertical)
        self.bar54.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar54.setObjectName("bar54")
        self.bar76 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar76.setGeometry(QtCore.QRect(770, 30, 11, 441))
        self.bar76.setStyleSheet("QProgressBar {\n"
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
        self.bar76.setProperty("value", 25)
        self.bar76.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar76.setTextVisible(False)
        self.bar76.setOrientation(QtCore.Qt.Vertical)
        self.bar76.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar76.setObjectName("bar76")
        self.bar69 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar69.setGeometry(QtCore.QRect(700, 30, 11, 441))
        self.bar69.setStyleSheet("QProgressBar {\n"
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
        self.bar69.setProperty("value", 32)
        self.bar69.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar69.setTextVisible(False)
        self.bar69.setOrientation(QtCore.Qt.Vertical)
        self.bar69.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar69.setObjectName("bar69")
        self.bar44 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar44.setGeometry(QtCore.QRect(450, 30, 11, 441))
        self.bar44.setStyleSheet("QProgressBar {\n"
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
        self.bar44.setProperty("value", 57)
        self.bar44.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar44.setTextVisible(False)
        self.bar44.setOrientation(QtCore.Qt.Vertical)
        self.bar44.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar44.setObjectName("bar44")
        self.bar42 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar42.setGeometry(QtCore.QRect(430, 30, 11, 441))
        self.bar42.setStyleSheet("QProgressBar {\n"
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
        self.bar42.setProperty("value", 59)
        self.bar42.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar42.setTextVisible(False)
        self.bar42.setOrientation(QtCore.Qt.Vertical)
        self.bar42.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar42.setObjectName("bar42")
        self.bar58 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar58.setGeometry(QtCore.QRect(590, 30, 11, 441))
        self.bar58.setStyleSheet("QProgressBar {\n"
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
        self.bar58.setProperty("value", 43)
        self.bar58.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar58.setTextVisible(False)
        self.bar58.setOrientation(QtCore.Qt.Vertical)
        self.bar58.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar58.setObjectName("bar58")
        self.bar74 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar74.setGeometry(QtCore.QRect(750, 30, 11, 441))
        self.bar74.setStyleSheet("QProgressBar {\n"
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
        self.bar74.setProperty("value", 27)
        self.bar74.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar74.setTextVisible(False)
        self.bar74.setOrientation(QtCore.Qt.Vertical)
        self.bar74.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar74.setObjectName("bar74")
        self.bar65 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar65.setGeometry(QtCore.QRect(660, 30, 11, 441))
        self.bar65.setStyleSheet("QProgressBar {\n"
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
        self.bar65.setProperty("value", 36)
        self.bar65.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar65.setTextVisible(False)
        self.bar65.setOrientation(QtCore.Qt.Vertical)
        self.bar65.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar65.setObjectName("bar65")
        self.bar59 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar59.setGeometry(QtCore.QRect(600, 30, 11, 441))
        self.bar59.setStyleSheet("QProgressBar {\n"
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
        self.bar59.setProperty("value", 42)
        self.bar59.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar59.setTextVisible(False)
        self.bar59.setOrientation(QtCore.Qt.Vertical)
        self.bar59.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar59.setObjectName("bar59")
        self.bar41 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar41.setGeometry(QtCore.QRect(420, 30, 11, 441))
        self.bar41.setStyleSheet("QProgressBar {\n"
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
        self.bar41.setProperty("value", 60)
        self.bar41.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar41.setTextVisible(False)
        self.bar41.setOrientation(QtCore.Qt.Vertical)
        self.bar41.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar41.setObjectName("bar41")
        self.bar57 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar57.setGeometry(QtCore.QRect(580, 30, 11, 441))
        self.bar57.setStyleSheet("QProgressBar {\n"
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
        self.bar57.setProperty("value", 44)
        self.bar57.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar57.setTextVisible(False)
        self.bar57.setOrientation(QtCore.Qt.Vertical)
        self.bar57.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar57.setObjectName("bar57")
        self.bar88 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar88.setGeometry(QtCore.QRect(890, 30, 11, 441))
        self.bar88.setStyleSheet("QProgressBar {\n"
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
        self.bar88.setProperty("value", 13)
        self.bar88.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar88.setTextVisible(False)
        self.bar88.setOrientation(QtCore.Qt.Vertical)
        self.bar88.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar88.setObjectName("bar88")
        self.bar92 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar92.setGeometry(QtCore.QRect(930, 30, 11, 441))
        self.bar92.setStyleSheet("QProgressBar {\n"
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
        self.bar92.setProperty("value", 9)
        self.bar92.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar92.setTextVisible(False)
        self.bar92.setOrientation(QtCore.Qt.Vertical)
        self.bar92.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar92.setObjectName("bar92")
        self.bar96 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar96.setGeometry(QtCore.QRect(970, 30, 11, 441))
        self.bar96.setStyleSheet("QProgressBar {\n"
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
        self.bar96.setProperty("value", 5)
        self.bar96.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar96.setTextVisible(False)
        self.bar96.setOrientation(QtCore.Qt.Vertical)
        self.bar96.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar96.setObjectName("bar96")
        self.bar98 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar98.setGeometry(QtCore.QRect(990, 30, 11, 441))
        self.bar98.setStyleSheet("QProgressBar {\n"
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
        self.bar98.setProperty("value", 3)
        self.bar98.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar98.setTextVisible(False)
        self.bar98.setOrientation(QtCore.Qt.Vertical)
        self.bar98.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar98.setObjectName("bar98")
        self.bar93 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar93.setGeometry(QtCore.QRect(940, 30, 11, 441))
        self.bar93.setStyleSheet("QProgressBar {\n"
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
        self.bar93.setProperty("value", 8)
        self.bar93.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar93.setTextVisible(False)
        self.bar93.setOrientation(QtCore.Qt.Vertical)
        self.bar93.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar93.setObjectName("bar93")
        self.bar82 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar82.setGeometry(QtCore.QRect(830, 30, 11, 441))
        self.bar82.setStyleSheet("QProgressBar {\n"
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
        self.bar82.setProperty("value", 19)
        self.bar82.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar82.setTextVisible(False)
        self.bar82.setOrientation(QtCore.Qt.Vertical)
        self.bar82.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar82.setObjectName("bar82")
        self.bar86 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar86.setGeometry(QtCore.QRect(870, 30, 11, 441))
        self.bar86.setStyleSheet("QProgressBar {\n"
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
        self.bar86.setProperty("value", 15)
        self.bar86.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar86.setTextVisible(False)
        self.bar86.setOrientation(QtCore.Qt.Vertical)
        self.bar86.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar86.setObjectName("bar86")
        self.bar81 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar81.setGeometry(QtCore.QRect(820, 30, 11, 441))
        self.bar81.setStyleSheet("QProgressBar {\n"
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
        self.bar81.setProperty("value", 20)
        self.bar81.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar81.setTextVisible(False)
        self.bar81.setOrientation(QtCore.Qt.Vertical)
        self.bar81.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar81.setObjectName("bar81")
        self.bar94 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar94.setGeometry(QtCore.QRect(950, 30, 11, 441))
        self.bar94.setStyleSheet("QProgressBar {\n"
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
        self.bar94.setProperty("value", 7)
        self.bar94.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar94.setTextVisible(False)
        self.bar94.setOrientation(QtCore.Qt.Vertical)
        self.bar94.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar94.setObjectName("bar94")
        self.bar99 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar99.setGeometry(QtCore.QRect(1000, 30, 11, 441))
        self.bar99.setStyleSheet("QProgressBar {\n"
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
        self.bar99.setProperty("value", 2)
        self.bar99.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar99.setTextVisible(False)
        self.bar99.setOrientation(QtCore.Qt.Vertical)
        self.bar99.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar99.setObjectName("bar99")
        self.bar85 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar85.setGeometry(QtCore.QRect(860, 30, 11, 441))
        self.bar85.setStyleSheet("QProgressBar {\n"
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
        self.bar85.setProperty("value", 16)
        self.bar85.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar85.setTextVisible(False)
        self.bar85.setOrientation(QtCore.Qt.Vertical)
        self.bar85.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar85.setObjectName("bar85")
        self.bar97 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar97.setGeometry(QtCore.QRect(980, 30, 11, 441))
        self.bar97.setStyleSheet("QProgressBar {\n"
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
        self.bar97.setProperty("value", 4)
        self.bar97.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar97.setTextVisible(False)
        self.bar97.setOrientation(QtCore.Qt.Vertical)
        self.bar97.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar97.setObjectName("bar97")
        self.bar83 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar83.setGeometry(QtCore.QRect(840, 30, 11, 441))
        self.bar83.setStyleSheet("QProgressBar {\n"
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
        self.bar83.setProperty("value", 18)
        self.bar83.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar83.setTextVisible(False)
        self.bar83.setOrientation(QtCore.Qt.Vertical)
        self.bar83.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar83.setObjectName("bar83")
        self.bar89 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar89.setGeometry(QtCore.QRect(900, 30, 11, 441))
        self.bar89.setStyleSheet("QProgressBar {\n"
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
        self.bar89.setProperty("value", 12)
        self.bar89.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar89.setTextVisible(False)
        self.bar89.setOrientation(QtCore.Qt.Vertical)
        self.bar89.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar89.setObjectName("bar89")
        self.bar100 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar100.setGeometry(QtCore.QRect(1010, 30, 11, 441))
        self.bar100.setStyleSheet("QProgressBar {\n"
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
        self.bar100.setProperty("value", 1)
        self.bar100.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar100.setTextVisible(False)
        self.bar100.setOrientation(QtCore.Qt.Vertical)
        self.bar100.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar100.setObjectName("bar100")
        self.bar90 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar90.setGeometry(QtCore.QRect(910, 30, 11, 441))
        self.bar90.setStyleSheet("QProgressBar {\n"
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
        self.bar90.setProperty("value", 11)
        self.bar90.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar90.setTextVisible(False)
        self.bar90.setOrientation(QtCore.Qt.Vertical)
        self.bar90.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar90.setObjectName("bar90")
        self.bar95 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar95.setGeometry(QtCore.QRect(960, 30, 11, 441))
        self.bar95.setStyleSheet("QProgressBar {\n"
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
        self.bar95.setProperty("value", 6)
        self.bar95.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar95.setTextVisible(False)
        self.bar95.setOrientation(QtCore.Qt.Vertical)
        self.bar95.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar95.setObjectName("bar95")
        self.bar87 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar87.setGeometry(QtCore.QRect(880, 30, 11, 441))
        self.bar87.setStyleSheet("QProgressBar {\n"
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
        self.bar87.setProperty("value", 14)
        self.bar87.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar87.setTextVisible(False)
        self.bar87.setOrientation(QtCore.Qt.Vertical)
        self.bar87.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar87.setObjectName("bar87")
        self.bar91 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar91.setGeometry(QtCore.QRect(920, 30, 11, 441))
        self.bar91.setStyleSheet("QProgressBar {\n"
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
        self.bar91.setProperty("value", 10)
        self.bar91.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar91.setTextVisible(False)
        self.bar91.setOrientation(QtCore.Qt.Vertical)
        self.bar91.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar91.setObjectName("bar91")
        self.bar84 = QtWidgets.QProgressBar(self.centralwidget)
        self.bar84.setGeometry(QtCore.QRect(850, 30, 11, 441))
        self.bar84.setStyleSheet("QProgressBar {\n"
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
        self.bar84.setProperty("value", 17)
        self.bar84.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.bar84.setTextVisible(False)
        self.bar84.setOrientation(QtCore.Qt.Vertical)
        self.bar84.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.bar84.setObjectName("bar84")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 20, 1021, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1050, 250, 121, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1050, 160, 121, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1050, 220, 121, 30))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1050, 190, 121, 30))
        self.pushButton_10.setObjectName("pushButton_10")
        self.frame.raise_()
        self.bar1.raise_()
        self.bar2.raise_()
        self.bar3.raise_()
        self.bar4.raise_()
        self.bar5.raise_()
        self.bar6.raise_()
        self.bar7.raise_()
        self.bar8.raise_()
        self.bar9.raise_()
        self.bar10.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.horizontalSlider.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_5.raise_()
        self.label_5.raise_()
        self.pushButton_6.raise_()
        self.bar11.raise_()
        self.bar18.raise_()
        self.bar19.raise_()
        self.bar12.raise_()
        self.bar15.raise_()
        self.bar20.raise_()
        self.bar16.raise_()
        self.bar17.raise_()
        self.bar14.raise_()
        self.bar13.raise_()
        self.bar27.raise_()
        self.bar30.raise_()
        self.bar35.raise_()
        self.bar32.raise_()
        self.bar33.raise_()
        self.bar40.raise_()
        self.bar28.raise_()
        self.bar21.raise_()
        self.bar34.raise_()
        self.bar39.raise_()
        self.bar29.raise_()
        self.bar38.raise_()
        self.bar24.raise_()
        self.bar25.raise_()
        self.bar36.raise_()
        self.bar23.raise_()
        self.bar22.raise_()
        self.bar31.raise_()
        self.bar37.raise_()
        self.bar26.raise_()
        self.bar72.raise_()
        self.bar78.raise_()
        self.bar68.raise_()
        self.bar45.raise_()
        self.bar71.raise_()
        self.bar55.raise_()
        self.bar64.raise_()
        self.bar47.raise_()
        self.bar43.raise_()
        self.bar77.raise_()
        self.bar73.raise_()
        self.bar62.raise_()
        self.bar67.raise_()
        self.bar46.raise_()
        self.bar56.raise_()
        self.bar80.raise_()
        self.bar60.raise_()
        self.bar75.raise_()
        self.bar79.raise_()
        self.bar70.raise_()
        self.bar50.raise_()
        self.bar61.raise_()
        self.bar53.raise_()
        self.bar52.raise_()
        self.bar66.raise_()
        self.bar48.raise_()
        self.bar49.raise_()
        self.bar63.raise_()
        self.bar51.raise_()
        self.bar54.raise_()
        self.bar76.raise_()
        self.bar69.raise_()
        self.bar44.raise_()
        self.bar42.raise_()
        self.bar58.raise_()
        self.bar74.raise_()
        self.bar65.raise_()
        self.bar59.raise_()
        self.bar41.raise_()
        self.bar57.raise_()
        self.bar88.raise_()
        self.bar92.raise_()
        self.bar96.raise_()
        self.bar98.raise_()
        self.bar93.raise_()
        self.bar82.raise_()
        self.bar86.raise_()
        self.bar81.raise_()
        self.bar94.raise_()
        self.bar99.raise_()
        self.bar85.raise_()
        self.bar97.raise_()
        self.bar83.raise_()
        self.bar89.raise_()
        self.bar100.raise_()
        self.bar90.raise_()
        self.bar95.raise_()
        self.bar87.raise_()
        self.bar91.raise_()
        self.bar84.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1182, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_2.clicked.connect(self.bubbleSort)
        self.horizontalSlider.valueChanged.connect(self.updateSpeed)
        self.pushButton_6.clicked.connect(self.generateDescending)
        self.pushButton.clicked.connect(self.generateRandom)
        self.pushButton_3.clicked.connect(self.insertionSort)
        self.pushButton_4.clicked.connect(self.selectionSort)
        self.pushButton_5.clicked.connect(self.shellSort)
        self.pushButton_8.clicked.connect(self.quickSortHelper)
        self.pushButton_10.clicked.connect(self.mergeSortHelper)
        self.pushButton_9.clicked.connect(self.heapSortHelper)
        self.pushButton_7.clicked.connect(self.radixSortHelper)

    def updateSpeed(self):
        self.numMS = self.horizontalSlider.value() * 0.001
        self.label_5.setText(str(self.horizontalSlider.value()))

    def generateRandom(self):
        self.label_2.setText("Generating...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        for i in range(len(barArr)):
            time.sleep(self.numMS)
            barArr[i].setValue(random.randint(0, 101))
        self.label_2.setText("Idle")

    def generateDescending(self):
        self.label_2.setText("Generating...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        curr = 100
        for i in range(len(barArr)):
            time.sleep(self.numMS)
            barArr[i].setValue(curr - (1*i))
        self.label_2.setText("Idle")

    def bubbleSort(self):
        self.label_2.setText("Bubble Sorting...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        valueArr = [barObj.value() for barObj in barArr]
        
        n = len(valueArr)
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                    if valueArr[j] > valueArr[j+1]:
                        time.sleep(self.numMS)
                        barArr[j].setValue(valueArr[j+1])
                        barArr[j+1].setValue(valueArr[j])
                        valueArr[j], valueArr[j+1] = valueArr[j+1], valueArr[j]
        self.label_2.setText("Idle")

    def insertionSort(self):
        self.label_2.setText("Insertion Sorting...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        valueArr = [barObj.value() for barObj in barArr]

        for i in range(1, len(barArr)): 
            key = valueArr[i]  
            j = i-1
            while j >=0 and key < valueArr[j]:
                    valueArr[j+1] = valueArr[j]
                    barArr[j+1].setValue(valueArr[j])
                    time.sleep(self.numMS)
                    j -= 1
            valueArr[j+1] = key
            barArr[j+1].setValue(key)
        self.label_2.setText("Idle")

    def selectionSort(self):
        self.label_2.setText("Selection Sorting...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        valueArr = [barObj.value() for barObj in barArr]

        for i in range(len(barArr)): 
            min_idx = i 
            for j in range(i+1, len(barArr)): 
                if valueArr[min_idx] > valueArr[j]: 
                    min_idx = j
            barArr[i].setValue(valueArr[min_idx])
            barArr[min_idx].setValue(valueArr[i])   
            valueArr[i], valueArr[min_idx] = valueArr[min_idx], valueArr[i] 
            time.sleep(self.numMS)
        
        self.label_2.setText("Idle")

    def shellSort(self):
        self.label_2.setText("Shell Sorting...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        valueArr = [barObj.value() for barObj in barArr]
        n = len(barArr) 
        gap = n//2
        while gap > 0: 
            for i in range(gap,n): 
                temp = valueArr[i] 
                j = i 
                while  j >= gap and valueArr[j-gap] > temp:
                    time.sleep(self.numMS)
                    barArr[j].setValue(valueArr[j-gap])
                    valueArr[j] = valueArr[j-gap] 
                    j -= gap 
                time.sleep(self.numMS)
                barArr[j].setValue(temp)
                valueArr[j] = temp 
            gap //= 2
        self.label_2.setText("Idle")

    def quickSortHelper(self):
        self.label_2.setText("Quick Sorting...")
        self.quickSort(0, 99)
        self.label_2.setText("Idle")

    def partition(self, low, high):
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        arr = [barObj.value() for barObj in barArr]
        
        i = ( low-1 )
        pivot = arr[high]
  
        for j in range(low , high): 
            if arr[j] <= pivot: 
                i = i+1 
                time.sleep(self.numMS)
                barArr[i].setValue(arr[j])
                barArr[j].setValue(arr[i])
                arr[i], arr[j] = arr[j], arr[i]
        time.sleep(self.numMS)
        barArr[i+1].setValue(arr[high])
        barArr[high].setValue(arr[i+1])
        arr[i+1], arr[high] = arr[high], arr[i+1] 
        return (i+1) 

    def quickSort(self, low, high):
        if low < high: 
            pi = self.partition(low,high) 

            self.quickSort(low, pi-1) 
            self.quickSort(pi+1, high) 

    def mergeSortHelper(self):
        self.label_2.setText("Merge Sorting...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        arr = [barObj.value() for barObj in barArr]
        self.mergeSort(arr)
        self.label_2.setText("Idle")

    def mergeSort(self, arr):
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        if len(arr) > 1: 
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R): 
                if L[i] < R[j]:
                    time.sleep(self.numMS)
                    barArr[k].setValue(L[i])
                    arr[k] = L[i] 
                    i+=1
                else:
                    time.sleep(self.numMS)
                    barArr[k].setValue(R[j])
                    arr[k] = R[j] 
                    j+=1
                k+=1
            while i < len(L):
                time.sleep(self.numMS)
                barArr[k].setValue(L[i])
                arr[k] = L[i] 
                i+=1
                k+=1
        
            while j < len(R):
                time.sleep(self.numMS)
                barArr[k].setValue(R[j])
                arr[k] = R[j] 
                j+=1
                k+=1 

    def heapSortHelper(self):
        self.label_2.setText("Heap Sorting...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        arr = [barObj.value() for barObj in barArr]
        self.heapSort(arr)
        self.label_2.setText("Idle")

    def heapify(self, arr, n, i):
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        largest = i 
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]: 
            largest = l
        if r < n and arr[largest] < arr[r]: 
            largest = r 
        if largest != i:
            time.sleep(self.numMS)
            barArr[i].setValue(arr[largest])
            barArr[largest].setValue(arr[i])
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr, n, largest) 
  
    def heapSort(self, arr):
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        n = len(arr) 
        for i in range(n // 2 - 1, -1, -1): 
            self.heapify(arr, n, i) 
        for i in range(n-1, 0, -1):
            time.sleep(self.numMS)
            barArr[i].setValue(arr[0])
            barArr[0].setValue(arr[i])
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

    def radixSortHelper(self):
        self.label_2.setText("Radix Sorting...")
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        arr = [barObj.value() for barObj in barArr]
        self.radixSort(arr)
        self.label_2.setText("Idle")

    def countingSort(self, arr, exp1):
        barArr = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10, self.bar11, self.bar12, self.bar13, self.bar14, self.bar15, self.bar16, self.bar17, self.bar18, self.bar19, self.bar20, self.bar21, self.bar22, self.bar23, self.bar24, self.bar25, self.bar26, self.bar27, self.bar28, self.bar29, self.bar30, self.bar31, self.bar32, self.bar33, self.bar34, self.bar35, self.bar36, self.bar37, self.bar38, self.bar39, self.bar40, self.bar41, self.bar42, self.bar43, self.bar44, self.bar45, self.bar46, self.bar47, self.bar48, self.bar49, self.bar50, self.bar51, self.bar52, self.bar53, self.bar54, self.bar55, self.bar56, self.bar57, self.bar58, self.bar59, self.bar60, self.bar61, self.bar62, self.bar63, self.bar64, self.bar65, self.bar66, self.bar67, self.bar68, self.bar69, self.bar70, self.bar71, self.bar72, self.bar73, self.bar74, self.bar75, self.bar76, self.bar77, self.bar78, self.bar79, self.bar80, self.bar81, self.bar82, self.bar83, self.bar84, self.bar85, self.bar86, self.bar87, self.bar88, self.bar89, self.bar90, self.bar91, self.bar92, self.bar93, self.bar94, self.bar95, self.bar96, self.bar97, self.bar98, self.bar99, self.bar100]
        n = len(arr)
        output = [0] * (n) 
        count = [0] * (10) 
        for i in range(0, n): 
            index = (arr[i]/exp1) 
            count[int(index % 10)] += 1
        for i in range(1,10): 
            count[i] += count[i-1] 
        i = n-1
        while i>=0: 
            index = (arr[i]/exp1) 
            output[count[int((index) % 10)] - 1] = arr[i] 
            count[int((index)%10)] -= 1
            i -= 1
        i = 0
        for i in range(len(arr)):
            time.sleep(self.numMS)
            barArr[i].setValue(output[i])
            arr[i] = output[i]

    def radixSort(self, arr):    
        exp = 1
        for i in range(3):
            self.countingSort(arr,exp) 
            exp *= 10

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sort Visualizer - Rafael Almazar"))
        self.bar1.setFormat(_translate("MainWindow", "%p"))
        self.bar2.setFormat(_translate("MainWindow", "%p"))
        self.bar3.setFormat(_translate("MainWindow", "%p"))
        self.bar4.setFormat(_translate("MainWindow", "%p"))
        self.bar5.setFormat(_translate("MainWindow", "%p"))
        self.bar6.setFormat(_translate("MainWindow", "%p"))
        self.bar7.setFormat(_translate("MainWindow", "%p"))
        self.bar8.setFormat(_translate("MainWindow", "%p"))
        self.bar9.setFormat(_translate("MainWindow", "%p"))
        self.bar10.setFormat(_translate("MainWindow", "%p"))
        self.pushButton.setText(_translate("MainWindow", "Generate Random"))
        self.pushButton_2.setText(_translate("MainWindow", "Bubble Sort"))
        self.pushButton_3.setText(_translate("MainWindow", "Insertion Sort"))
        self.pushButton_4.setText(_translate("MainWindow", "Selection Sort"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.label_2.setText(_translate("MainWindow", "Idle"))
        self.label_3.setText(_translate("MainWindow", "Speed (ms):"))
        self.label_4.setText(_translate("MainWindow", "Sorts:"))
        self.pushButton_5.setText(_translate("MainWindow", "Shell Sort"))
        self.label_5.setText(_translate("MainWindow", "10"))
        self.pushButton_6.setText(_translate("MainWindow", "Generate Descending"))
        self.bar11.setFormat(_translate("MainWindow", "%p"))
        self.bar18.setFormat(_translate("MainWindow", "%p"))
        self.bar19.setFormat(_translate("MainWindow", "%p"))
        self.bar12.setFormat(_translate("MainWindow", "%p"))
        self.bar15.setFormat(_translate("MainWindow", "%p"))
        self.bar20.setFormat(_translate("MainWindow", "%p"))
        self.bar16.setFormat(_translate("MainWindow", "%p"))
        self.bar17.setFormat(_translate("MainWindow", "%p"))
        self.bar14.setFormat(_translate("MainWindow", "%p"))
        self.bar13.setFormat(_translate("MainWindow", "%p"))
        self.bar27.setFormat(_translate("MainWindow", "%p"))
        self.bar30.setFormat(_translate("MainWindow", "%p"))
        self.bar35.setFormat(_translate("MainWindow", "%p"))
        self.bar32.setFormat(_translate("MainWindow", "%p"))
        self.bar33.setFormat(_translate("MainWindow", "%p"))
        self.bar40.setFormat(_translate("MainWindow", "%p"))
        self.bar28.setFormat(_translate("MainWindow", "%p"))
        self.bar21.setFormat(_translate("MainWindow", "%p"))
        self.bar34.setFormat(_translate("MainWindow", "%p"))
        self.bar39.setFormat(_translate("MainWindow", "%p"))
        self.bar29.setFormat(_translate("MainWindow", "%p"))
        self.bar38.setFormat(_translate("MainWindow", "%p"))
        self.bar24.setFormat(_translate("MainWindow", "%p"))
        self.bar25.setFormat(_translate("MainWindow", "%p"))
        self.bar36.setFormat(_translate("MainWindow", "%p"))
        self.bar23.setFormat(_translate("MainWindow", "%p"))
        self.bar22.setFormat(_translate("MainWindow", "%p"))
        self.bar31.setFormat(_translate("MainWindow", "%p"))
        self.bar37.setFormat(_translate("MainWindow", "%p"))
        self.bar26.setFormat(_translate("MainWindow", "%p"))
        self.bar72.setFormat(_translate("MainWindow", "%p"))
        self.bar78.setFormat(_translate("MainWindow", "%p"))
        self.bar68.setFormat(_translate("MainWindow", "%p"))
        self.bar45.setFormat(_translate("MainWindow", "%p"))
        self.bar71.setFormat(_translate("MainWindow", "%p"))
        self.bar55.setFormat(_translate("MainWindow", "%p"))
        self.bar64.setFormat(_translate("MainWindow", "%p"))
        self.bar47.setFormat(_translate("MainWindow", "%p"))
        self.bar43.setFormat(_translate("MainWindow", "%p"))
        self.bar77.setFormat(_translate("MainWindow", "%p"))
        self.bar73.setFormat(_translate("MainWindow", "%p"))
        self.bar62.setFormat(_translate("MainWindow", "%p"))
        self.bar67.setFormat(_translate("MainWindow", "%p"))
        self.bar46.setFormat(_translate("MainWindow", "%p"))
        self.bar56.setFormat(_translate("MainWindow", "%p"))
        self.bar80.setFormat(_translate("MainWindow", "%p"))
        self.bar60.setFormat(_translate("MainWindow", "%p"))
        self.bar75.setFormat(_translate("MainWindow", "%p"))
        self.bar79.setFormat(_translate("MainWindow", "%p"))
        self.bar70.setFormat(_translate("MainWindow", "%p"))
        self.bar50.setFormat(_translate("MainWindow", "%p"))
        self.bar61.setFormat(_translate("MainWindow", "%p"))
        self.bar53.setFormat(_translate("MainWindow", "%p"))
        self.bar52.setFormat(_translate("MainWindow", "%p"))
        self.bar66.setFormat(_translate("MainWindow", "%p"))
        self.bar48.setFormat(_translate("MainWindow", "%p"))
        self.bar49.setFormat(_translate("MainWindow", "%p"))
        self.bar63.setFormat(_translate("MainWindow", "%p"))
        self.bar51.setFormat(_translate("MainWindow", "%p"))
        self.bar54.setFormat(_translate("MainWindow", "%p"))
        self.bar76.setFormat(_translate("MainWindow", "%p"))
        self.bar69.setFormat(_translate("MainWindow", "%p"))
        self.bar44.setFormat(_translate("MainWindow", "%p"))
        self.bar42.setFormat(_translate("MainWindow", "%p"))
        self.bar58.setFormat(_translate("MainWindow", "%p"))
        self.bar74.setFormat(_translate("MainWindow", "%p"))
        self.bar65.setFormat(_translate("MainWindow", "%p"))
        self.bar59.setFormat(_translate("MainWindow", "%p"))
        self.bar41.setFormat(_translate("MainWindow", "%p"))
        self.bar57.setFormat(_translate("MainWindow", "%p"))
        self.bar88.setFormat(_translate("MainWindow", "%p"))
        self.bar92.setFormat(_translate("MainWindow", "%p"))
        self.bar96.setFormat(_translate("MainWindow", "%p"))
        self.bar98.setFormat(_translate("MainWindow", "%p"))
        self.bar93.setFormat(_translate("MainWindow", "%p"))
        self.bar82.setFormat(_translate("MainWindow", "%p"))
        self.bar86.setFormat(_translate("MainWindow", "%p"))
        self.bar81.setFormat(_translate("MainWindow", "%p"))
        self.bar94.setFormat(_translate("MainWindow", "%p"))
        self.bar99.setFormat(_translate("MainWindow", "%p"))
        self.bar85.setFormat(_translate("MainWindow", "%p"))
        self.bar97.setFormat(_translate("MainWindow", "%p"))
        self.bar83.setFormat(_translate("MainWindow", "%p"))
        self.bar89.setFormat(_translate("MainWindow", "%p"))
        self.bar100.setFormat(_translate("MainWindow", "%p"))
        self.bar90.setFormat(_translate("MainWindow", "%p"))
        self.bar95.setFormat(_translate("MainWindow", "%p"))
        self.bar87.setFormat(_translate("MainWindow", "%p"))
        self.bar91.setFormat(_translate("MainWindow", "%p"))
        self.bar84.setFormat(_translate("MainWindow", "%p"))
        self.pushButton_7.setText(_translate("MainWindow", "Radix Sort"))
        self.pushButton_8.setText(_translate("MainWindow", "Quick Sort"))
        self.pushButton_9.setText(_translate("MainWindow", "Heap Sort"))
        self.pushButton_10.setText(_translate("MainWindow", "Merge Sort"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
