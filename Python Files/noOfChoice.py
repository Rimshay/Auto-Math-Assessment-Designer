import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from virtualkeyboard import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import docx2txt
import source

class Choice(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(283, 140)
        Dialog.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 150, 41))
        self.label.setStyleSheet("font: 11pt \"Arial\";")
        self.label.setObjectName("label")
        self.choice = QtWidgets.QLineEdit(Dialog)
        self.choice.setGeometry(QtCore.QRect(190, 30, 40, 41))
        #self.choice.setStyleSheet("image: url(:/newPrefix/exclamation.png);")
        #self.choice.setText("")
        self.choice.setObjectName("label_2")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(70, 80, 60, 41)
        self.pushButton.setText("ok")
        self.pushButton.setStyleSheet("background-color: rgb(2, 114, 118);\n"
"font: 13pt \"Arial\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;")
        #self.pushButton.clicked.connect(self.virtualkeyboard)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #self.s = self.pushButton.clicked.connect(self.clickbutton)
        #self.x = self.choice.text()
        #print(self.x)
        #self.x = '3'

        #if self.x == '3':
        #    self.s = self.pushButton.clicked.connect(self.clickbutton)



    #def clickbutton(self):
    #    self.c = self.choice.text()
    #    if self.c == '3':
    #        print(self.c)
        #sender_button = self.sender()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "MCQs Options"))
        Dialog.setWindowIcon(QIcon("Splashlogo.png"))
        self.label.setText(_translate("Dialog", "Enter no of choices"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Choice()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
