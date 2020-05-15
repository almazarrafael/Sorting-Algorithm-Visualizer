from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 25, 16, 441))
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
        self.progressBar_2.setGeometry(QtCore.QRect(60, 25, 16, 441))
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
        self.progressBar_2.setProperty("value", 90)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_2.setObjectName("progressBar_2")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(90, 25, 16, 441))
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
        self.progressBar_3.setProperty("value", 80)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_3.setTextVisible(False)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_3.setObjectName("progressBar_3")
        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(120, 25, 16, 441))
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
        self.progressBar_4.setProperty("value", 70)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_4.setTextVisible(False)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_4.setObjectName("progressBar_4")
        self.progressBar_5 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_5.setGeometry(QtCore.QRect(150, 25, 16, 441))
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
        self.progressBar_5.setProperty("value", 60)
        self.progressBar_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_5.setTextVisible(False)
        self.progressBar_5.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_5.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_5.setObjectName("progressBar_5")
        self.progressBar_6 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_6.setGeometry(QtCore.QRect(180, 25, 16, 441))
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
        self.progressBar_6.setProperty("value", 50)
        self.progressBar_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_6.setTextVisible(False)
        self.progressBar_6.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_6.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_6.setObjectName("progressBar_6")
        self.progressBar_7 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_7.setGeometry(QtCore.QRect(210, 25, 16, 441))
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
        self.progressBar_7.setProperty("value", 40)
        self.progressBar_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_7.setTextVisible(False)
        self.progressBar_7.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_7.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_7.setObjectName("progressBar_7")
        self.progressBar_8 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_8.setGeometry(QtCore.QRect(240, 25, 16, 441))
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
        self.progressBar_8.setProperty("value", 30)
        self.progressBar_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_8.setTextVisible(False)
        self.progressBar_8.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_8.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_8.setObjectName("progressBar_8")
        self.progressBar_9 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_9.setGeometry(QtCore.QRect(270, 25, 16, 441))
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
        self.progressBar_9.setProperty("value", 20)
        self.progressBar_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.progressBar_9.setTextVisible(False)
        self.progressBar_9.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_9.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_9.setObjectName("progressBar_9")
        self.progressBar_10 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_10.setGeometry(QtCore.QRect(300, 25, 16, 441))
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
        self.progressBar_10.setProperty("value", 10)
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
        self.pushButton.setGeometry(QtCore.QRect(350, 40, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 140, 121, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 240, 121, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 340, 121, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 430, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 450, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
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

        self.pushButton_2.clicked.connect(self.bubbleSort)

    def bubbleSort(self):
        self.label_2.setText("Sorting...")
        arr = [self.progressBar.value(), self.progressBar_2.value(), self.progressBar_3.value(), self.progressBar_4.value(), self.progressBar_5.value(), self.progressBar_6.value(), self.progressBar_7.value(), self.progressBar_8.value(), self.progressBar_9.value(), self.progressBar_10.value()]
        arr1 = [self.progressBar, self.progressBar_2, self.progressBar_3, self.progressBar_4, self.progressBar_5, self.progressBar_6, self.progressBar_7, self.progressBar_8, self.progressBar_9, self.progressBar_10]
        n = len(arr)
        for i in range(n-1): 
            for j in range(0, n-i-1): 
                    if arr[j] > arr[j+1] : 
                            time.sleep(0.1)
                            arr[j], arr[j+1] = arr[j+1], arr[j]
                            arr1[j].setValue(arr[j])
                            arr1[j+1].setValue(arr[j+1])
        self.label_2.setText("Idle")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.pushButton.setText(_translate("MainWindow", "Generate"))
        self.pushButton_2.setText(_translate("MainWindow", "Bubble Sort"))
        self.pushButton_3.setText(_translate("MainWindow", "Insertion Sort"))
        self.pushButton_4.setText(_translate("MainWindow", "Merge Sort"))
        self.label.setText(_translate("MainWindow", "Status:"))
        self.label_2.setText(_translate("MainWindow", "Idle"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
