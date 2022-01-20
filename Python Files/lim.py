import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from virtualkeyboard import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
#import docx2txt
import source

class Ui_lim(object):
    #sett = qtc.pyqtSignal(str)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 150)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 55, 13))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(140, 30, 81, 41))
        self.textEdit.setObjectName("textEdit")

        self.Okbtn = QtWidgets.QPushButton(Dialog)
        self.Okbtn.setText("OK")
        self.Okbtn.setGeometry(QtCore.QRect(100, 100, 100, 35))
        self.Okbtn.setObjectName("Okbtn")
        self.Okbtn.setStyleSheet("QPushButton#Okbtn{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#Okbtn:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#Okbtn:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")
        #self.Okbtn.clicked.connect(self.click)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #def click(self):
    #    self.d1 = str(self.textEdit.toPlainText())
        #\lim_{}
    #    self.string = "\lim_{" +self.d1+ "}"
    #    self.sett.emit(self.string)
    #    self.sett.connect(window.fraction)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Symbols Power and base"))
        Dialog.setWindowIcon(QIcon("Splashlogo.png"))
        self.label.setText(_translate("Dialog", "Base"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_lim()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
