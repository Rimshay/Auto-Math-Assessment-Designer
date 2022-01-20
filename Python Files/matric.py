import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from virtualkeyboard import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
#import docx2txt
import source

class Ui_Matrix(object):
    #pick = qtc.pyqtSignal(str, str, str)

    def setupUi(self, Matrix):
        Matrix.setObjectName("Matrix")
        Matrix.resize(350, 250)
        self.label = QtWidgets.QLabel(Matrix)
        self.label.setGeometry(QtCore.QRect(60, 40, 80, 13))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.label1 = QtWidgets.QLabel(Matrix)
        self.label1.setGeometry(QtCore.QRect(40, 80, 200, 13))
        self.label1.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label1.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Matrix)
        self.label2.setGeometry(QtCore.QRect(40, 100, 200, 13))
        self.label2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label2.setObjectName("label")

        self.label3 = QtWidgets.QLabel(Matrix)
        self.label3.setGeometry(QtCore.QRect(40, 120, 200, 13))
        self.label3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label3.setObjectName("label")

        self.label4 = QtWidgets.QLabel(Matrix)
        self.label4.setGeometry(QtCore.QRect(40, 140, 200, 13))
        self.label4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label4.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Matrix)
        self.textEdit.setGeometry(QtCore.QRect(150, 30, 60, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Matrix)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 30, 60, 41))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(Matrix)
        self.textEdit_3.setGeometry(QtCore.QRect(220, 100, 60, 41))
        self.textEdit_3.setObjectName("textEdit_2")

        self.Okbtn = QtWidgets.QPushButton(Matrix)
        self.Okbtn.setText("OK")
        self.Okbtn.setGeometry(QtCore.QRect(130, 180, 100, 35))
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
        #self.Okbtn.clicked.connect(self.arrclick)
        self.retranslateUi(Matrix)
        QtCore.QMetaObject.connectSlotsByName(Matrix)

    #def arrclick(self):
    #    print('p')
    #    self.d1 = self.textEdit.toPlainText()
    #    print('p')
    #    self.d2 = self.textEdit_2.toPlainText()
    #    print('p')
    #    self.t3 = self.textEdit_3.toPlainText()
    #    print('p')
    #    try:
    #        self.pick.emit(self.d1, self.d2, self.t3)
    #    except Exception as e:
    #        print(e)
    #    print('p')
    #    self.pick.connect(window.matrixupdate)
    #    print('p')



    def retranslateUi(self, Matrix):
        _translate = QtCore.QCoreApplication.translate
        Matrix.setWindowTitle(_translate("Matrix", "Dimension of the Array"))
        Matrix.setWindowIcon(QIcon("Splashlogo.png"))
        self.label.setText(_translate("Matrix", "Dimension"))
        self.label1.setText(_translate("Matrix", "Absolute-value bars = A"))
        self.label2.setText(_translate("Matrix", "Square Matrix = B"))
        self.label3.setText(_translate("Matrix", "Round Matrix  = C"))
        self.label4.setText(_translate("Matrix", "Curly Matrix = D"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Matrix()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
