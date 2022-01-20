# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SplashScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from LoginScreen import Ui_LoginScreen
import source

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(551, 426)
        SplashScreen.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        SplashScreen.setStyleSheet("background-color: rgba(62, 62, 62, 240);\n"
"border-radius: 10px")
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.SplashImage = QtWidgets.QLabel(self.centralwidget)
        self.SplashImage.setGeometry(QtCore.QRect(140, 10, 281, 231))
        self.SplashImage.setStyleSheet("background-color: rgba(62, 62, 62, 240);\n"
"image: url(:/newPrefix/Splashlogo.png);")
        self.SplashImage.setText("")
        self.SplashImage.setObjectName("SplashImage")
        self.SplashHeading = QtWidgets.QLabel(self.centralwidget)
        self.SplashHeading.setGeometry(QtCore.QRect(100, 230, 361, 31))
        self.SplashHeading.setStyleSheet("color: rgb(240, 240, 240);\n"
"font: 18pt \"Arial\";")
        self.SplashHeading.setObjectName("SplashHeading")
        self.SplashProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.SplashProgressBar.setGeometry(QtCore.QRect(60, 300, 431, 23))
        self.SplashProgressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(200, 200, 200);\n"
"color: rgb(3, 152, 158);\n"
"borde-style : none;\n"
"border-radius : 10px;\n"
"text-align : center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius : 10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.0284091, y1:0.574, x2:1, y2:0.568, stop:0 rgba(3, 141, 146, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.SplashProgressBar.setProperty("value", 24)
        self.SplashProgressBar.setObjectName("SplashProgressBar")
        self.SplashLoading = QtWidgets.QLabel(self.centralwidget)
        self.SplashLoading.setGeometry(QtCore.QRect(250, 350, 71, 21))
        self.SplashLoading.setStyleSheet("font: 11pt \"Arial\";\n"
"color: rgb(225, 225, 225);\n"
"")
        self.SplashLoading.setObjectName("SplashLoading")
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.SplashHeading.setText(_translate("SplashScreen", "Auto Math Assessment Designer"))
        self.SplashLoading.setText(_translate("SplashScreen", "Loading...."))
