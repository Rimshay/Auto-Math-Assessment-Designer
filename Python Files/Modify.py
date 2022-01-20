import sys
#sys.getdefaulencoding()
import pylatex
import numpy as np
from sympy.matrices import Matrix
from sympy import *
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from noOfChoice import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import docx2txt
import sqlite3
import source
#from SignupScreen import Ui_LoginScreen

#####################################################################
######################################################################

class MainApp(QMainWindow):
    """ the main class of our app """
    def __init__(self):
        """ init things here """
        super().__init__()

        self.option1 = QRadioButton(self)
        self.option2 = QRadioButton(self)
        self.option3 = QRadioButton(self)
        self.option4 = QRadioButton(self)
        self.option5 = QRadioButton(self)
        self.optionedit1 = QTextEdit(self)
        self.optionedit2 = QTextEdit(self)
        self.optionedit3 = QTextEdit(self)
        self.optionedit4 = QTextEdit(self)
        self.optionedit5 = QTextEdit(self)
        self.optionedit6 = QLabel(self)
        self.optionedit7 = QLabel(self)
        self.chep = QLabel(self)                       # parent class initializer

        # window title
        self.title = "Modify a Question"
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon("Splashlogo.png"))
        self.resize(700, 600)

        self.heading1 = QLabel(self)
        self.heading1.setText("Question Description")
        self.heading1.setStyleSheet("font: 15pt \"Arial\";")
        self.heading1.setGeometry(QtCore.QRect(80, 200, 500, 31))
        self.heading1.setObjectName("heading1")


        self.ee = QLabel(self)
        #self.LoginScreen = QtWidgets.QMainWindow()
        #self.ui = Ui_LoginScreen()
        #self.ui.setupUi(self.LoginScreen)
        #self.s = self.ui.loginfunction()
        #self.ee.setText(self.s)
        self.ee.setStyleSheet("color: rgb(220, 220, 220)")
        self.ee.setGeometry(QtCore.QRect(300, 200, 600, 31))
        self.ee.setObjectName("ee")


        # editor section
        self.editor = QTextEdit(self)
        self.editor.setMinimumSize(QSize(0, 170));
        self.editor.setMaximumSize(QSize(16777215, 170));
        self.editor.setGeometry(QtCore.QRect(80, 240, 550, 31))

         # creating a radio button
        #self.radio_button = QRadioButton(self)
        #self.radio_button.setGeometry(100,  450, 120, 40)
        #self.radio_button.setText("Subjective")
        #self.radio_button.setChecked(True)
        #self.radio_button.setStyleSheet("font: 15pt \"Arial\";")
        #self.radio_button.toggled.connect(self.action2)

        self.radio_button1 = QRadioButton(self)
        self.radio_button1.setGeometry(230, 450, 120, 40)
        self.radio_button1.setText("Objective")
        self.radio_button1.setStyleSheet("font: 15pt \"Arial\";")
        #self.radio_button1.toggled.connect(self.action)
        self.radio_button1.clicked.connect(self.action)


        self.chep.setGeometry(230, 400, 120, 40)
        self.chep.setText("O")
        self.chep.setStyleSheet("color: rgb(225, 225, 225)")
        self.chep.setObjectName("chep")
        #print(self.chep.text())


        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(250, 115, 230, 40)
        self.pushButton.setText("Virtual Mathematic keyboard")
        self.pushButton.setStyleSheet("background-color: rgb(2, 114, 118);\n"
"font: 13pt \"Arial\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;")
        self.pushButton.clicked.connect(self.Vkeyboard)

        self.combo = QComboBox(self)
        self.combo.setGeometry(420, 430, 130, 40)
        self.combo.addItem("Linear Algebra")
        self.combo.addItem("Calculus")
        self.combo.addItem("Probability")
        self.combo.setStyleSheet("border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 6em;\n")

        self.save = QPushButton(self)
        self.save.setGeometry(420, 500, 90, 40)
        self.save.setText("Save")
        self.save.setStyleSheet("background-color: rgb(2, 114, 118);\n"
"font: 10pt \"Arial\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;")

        self.save.clicked.connect(self.save_to_db)

        self.cancel = QPushButton(self)
        self.cancel.setGeometry(550, 500, 90, 40)
        self.cancel.setText("Cancel")
        self.cancel.setStyleSheet("background-color: rgb(2, 114, 118);\n"
"font: 10pt \"Arial\";\n"
"color: rgba(255, 255, 255, 200);\n"
"border-radius: 10px;")

        # create menubar and toolbar first
        self.create_menu_bar()
        self.create_toolbar()

        # after craeting toolabr we can call and select font size
        font = QFont('Times', 12)
        self.editor.setFont(font)
        self.editor.setFontPointSize(12)
        # stores path
        self.path = ''

    def Vkeyboard(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_keyboard()
        self.ui.setupUi(self.window)
        self.ui.submitted.connect(self.updatefield)
        self.window.show()
        #self.ui.show()
        #print("helo")
        #if self.ui.pushButton_7.clicked.connect(self.powba):
        #    print("helo")
            #self.send.connect(self.update)



    def action2(self):
        self.resize(700, 530)

    def action(self):
        radiobtn = self.sender()

        if radiobtn.isChecked():
            self.window = QtWidgets.QDialog()
            self.ui = Choice()
            self.ui.setupUi(self.window)
            self.window.show()

            self.ui.pushButton.clicked.connect(self.clickbutton)

    def clickbutton(self):

         self.ch = self.ui.choice.text()
         print(self.ch)

         if self.ch == '2':
             #self.s = self.ch
             #print(self.s)
             self.chep.setText('2')

             self.resize(700, 640)
             self.option1.setText("a)")
             self.option1.setStyleSheet("font: 15pt \"Arial\";")
             self.option1.setGeometry(160, 520, 500, 40)

             self.option2.setText("b)")
             self.option2.setStyleSheet("font: 15pt \"Arial\";")
             self.option2.setGeometry(300, 520, 500, 40)\

             self.optionedit6.setText("true")
             self.optionedit6.setStyleSheet("font: 15pt \"Arial\";")
             self.optionedit6.setMinimumSize(QSize(0, 25));
             self.optionedit6.setMaximumSize(QSize(60, 25));
             self.optionedit6.setGeometry(QtCore.QRect(200, 530, 210, 40))

             self.optionedit7.setText("false")
             self.optionedit7.setStyleSheet("font: 15pt \"Arial\";")
             self.optionedit7.setMinimumSize(QSize(0, 25));
             self.optionedit7.setMaximumSize(QSize(60, 25));
             self.optionedit7.setGeometry(QtCore.QRect(340, 530, 210, 40))

         elif self.ch == '3':
            self.chep.setText('3')
            self.resize(700, 650)
            self.option1.setText("a)")
            self.option1.setStyleSheet("font: 15pt \"Arial\";")
            self.option1.setGeometry(160, 520, 500, 40)

            self.option2.setText("b)")
            self.option2.setStyleSheet("font: 15pt \"Arial\";")
            self.option2.setGeometry(300, 520, 500, 40)

            self.option3.setText("c)")
            self.option3.setStyleSheet("font: 15pt \"Arial\";")
            self.option3.setGeometry(160, 570, 500, 40)

            self.optionedit1.setMinimumSize(QSize(0, 25));
            self.optionedit1.setMaximumSize(QSize(60, 25));
            self.optionedit1.setGeometry(QtCore.QRect(200, 530, 210, 40))

            self.optionedit2.setMinimumSize(QSize(0, 25));
            self.optionedit2.setMaximumSize(QSize(60, 25));
            self.optionedit2.setGeometry(QtCore.QRect(340, 530, 210, 40))

            self.optionedit3.setMinimumSize(QSize(0, 25));
            self.optionedit3.setMaximumSize(QSize(60, 25));
            self.optionedit3.setGeometry(QtCore.QRect(200, 580, 210, 40))


         elif self.ch == '4':
            self.chep.setText('4')
            self.resize(700, 660)
            self.option1.setText("a)")
            self.option1.setStyleSheet("font: 15pt \"Arial\";")
            self.option1.setGeometry(160, 520, 500, 40)

            self.option2.setText("b)")
            self.option2.setStyleSheet("font: 15pt \"Arial\";")
            self.option2.setGeometry(300, 520, 500, 40)

            self.option3.setText("c)")
            self.option3.setStyleSheet("font: 15pt \"Arial\";")
            self.option3.setGeometry(160, 570, 500, 40)

            self.option4.setText("d)")
            self.option4.setStyleSheet("font: 15pt \"Arial\";")
            self.option4.setGeometry(300, 570, 500, 40)

            self.optionedit1.setMinimumSize(QSize(0, 25));
            self.optionedit1.setMaximumSize(QSize(60, 25));
            self.optionedit1.setGeometry(QtCore.QRect(200, 530, 210, 40))

            self.optionedit2.setMinimumSize(QSize(0, 25));
            self.optionedit2.setMaximumSize(QSize(60, 25));
            self.optionedit2.setGeometry(QtCore.QRect(340, 530, 210, 40))

            self.optionedit3.setMinimumSize(QSize(0, 25));
            self.optionedit3.setMaximumSize(QSize(60, 25));
            self.optionedit3.setGeometry(QtCore.QRect(200, 580, 210, 40))

            self.optionedit4.setMinimumSize(QSize(0, 25));
            self.optionedit4.setMaximumSize(QSize(60, 25));
            self.optionedit4.setGeometry(QtCore.QRect(340, 580, 210, 40))

         elif self.ch == '5':
             self.chep.setText('5')
             self.resize(700, 680)
             self.option1.setText("a)")
             self.option1.setStyleSheet("font: 15pt \"Arial\";")
             self.option1.setGeometry(160, 520, 500, 40)

             self.option2.setText("b)")
             self.option2.setStyleSheet("font: 15pt \"Arial\";")
             self.option2.setGeometry(300, 520, 500, 40)

             self.option3.setText("c)")
             self.option3.setStyleSheet("font: 15pt \"Arial\";")
             self.option3.setGeometry(160, 570, 500, 40)

             self.option4.setText("d)")
             self.option4.setStyleSheet("font: 15pt \"Arial\";")
             self.option4.setGeometry(300, 570, 500, 40)

             self.option5.setText("e)")
             self.option5.setStyleSheet("font: 15pt \"Arial\";")
             self.option5.setGeometry(160, 620, 500, 40)

             self.optionedit1.setMinimumSize(QSize(0, 25));
             self.optionedit1.setMaximumSize(QSize(60, 25));
             self.optionedit1.setGeometry(QtCore.QRect(200, 530, 210, 40))

             self.optionedit2.setMinimumSize(QSize(0, 25));
             self.optionedit2.setMaximumSize(QSize(60, 25));
             self.optionedit2.setGeometry(QtCore.QRect(340, 530, 210, 40))

             self.optionedit3.setMinimumSize(QSize(0, 25));
             self.optionedit3.setMaximumSize(QSize(60, 25));
             self.optionedit3.setGeometry(QtCore.QRect(200, 580, 210, 40))

             self.optionedit4.setMinimumSize(QSize(0, 25));
             self.optionedit4.setMaximumSize(QSize(60, 25));
             self.optionedit4.setGeometry(QtCore.QRect(340, 580, 210, 40))

             self.optionedit5.setMinimumSize(QSize(0, 25));
             self.optionedit5.setMaximumSize(QSize(60, 25));
             self.optionedit5.setGeometry(QtCore.QRect(200, 630, 210, 40))

             self.getq = self.editor.toPlainText()
             print(self.getq)

    def save_to_db(self):
        self.selected = self.combo.currentText()
        tex = str(self.editor.toPlainText())
        self.email = self.ee.text()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        if self.selected == 'Linear Algebra':
            print('h')
            self.cc = self.chep.text()
            print('h')
            if self.cc == '2':
                print('h')
                self.t = self.optionedit6.text()
                self.f = self.optionedit7.text()
                self.mcqs = tex + ',' + self.t + ',' + self.f
                cur.execute("CREATE TABLE IF NOT EXISTS LinearOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO LinearOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM LinearOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()

            elif self.cc == '3':
                print('h')
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.mcqs = tex + ',' + self.one + ',' + self.two + ',' + self.three
                cur.execute("CREATE TABLE IF NOT EXISTS LinearOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO LinearOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM LinearOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()
            elif self.cc == '4':
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.four = self.optionedit4.toPlainText()
                self.mcqs = tex + ',' + self.one + ',' + self.two + ',' + self.three + ',' + self.four
                cur.execute("CREATE TABLE IF NOT EXISTS LinearOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO LinearOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM LinearOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()
            elif self.cc == '5':
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.four = self.optionedit4.toPlainText()
                self.five = self.optionedit5.toPlainText()
                self.mcqs = tex + ',' + self.one + ',' + self.two + ',' + self.three + ',' + self.four + ',' + self.five
                cur.execute("CREATE TABLE IF NOT EXISTS LinearOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO LinearOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM LinearOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()


            else:
                print("yes")
                self.q = self.editor.text()
                cur.execute("CREATE TABLE IF NOT EXISTS LinearSub (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO LinearSub (QDes, Email) VALUES (?,?)", (tex, self.email))
                cur.execute(f"SELECT QDes FROM LinearSub WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()

        elif self.selected == 'Calculus':
            self.cc = self.chep.text()
            print('h')
            if self.cc == '2':
                print('h')
                self.t = self.optionedit6.text()
                self.f = self.optionedit7.text()
                self.mcqs = tex + self.t + self.f
                cur.execute("CREATE TABLE IF NOT EXISTS CalculusOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO CalculusOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM CalculusOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()

            elif self.cc == '3':
                print('h')
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.mcqs = tex + self.one + self.two + self.three
                cur.execute("CREATE TABLE IF NOT EXISTS CalculusOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO CalculusOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM CalculusOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()
            elif self.cc == '4':
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.four = self.optionedit4.toPlainText()
                self.mcqs = tex + self.one + self.two + self.three + self.four
                cur.execute("CREATE TABLE IF NOT EXISTS CalculusOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO CalculusOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM CalculusOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()
            elif self.cc == '5':
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.four = self.optionedit4.toPlainText()
                self.five = self.optionedit5.toPlainText()
                self.mcqs = tex + self.one + self.two + self.three + self.four + self.five
                cur.execute("CREATE TABLE IF NOT EXISTS CalculusOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO CalculusOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM CalculusOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()


            else:
                print("yes")
                cur.execute("CREATE TABLE IF NOT EXISTS CalculusSub (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO CalculusSub (QDes, Email) VALUES (?,?)", (tex, self.email))
                cur.execute(f"SELECT QDes FROM CalculusSub WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()



        elif self.selected == 'Probability':
            self.cc = self.chep.text()
            print('h')
            if self.cc == '2':
                print('h')
                self.t = self.optionedit6.text()
                self.f = self.optionedit7.text()
                self.mcqs = tex + self.t + self.f
                cur.execute("CREATE TABLE IF NOT EXISTS ProbabilityOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO ProbabilityOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM ProbabilityOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()

            elif self.cc == '3':
                print('h')
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.mcqs = tex + self.one + self.two + self.three
                cur.execute("CREATE TABLE IF NOT EXISTS ProbabilityOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO ProbabilityOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM ProbabilityOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()
            elif self.cc == '4':
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.four = self.optionedit4.toPlainText()
                self.mcqs = tex + self.one + self.two + self.three + self.four
                cur.execute("CREATE TABLE IF NOT EXISTS ProbabilityOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO ProbabilityOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM ProbabilityOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()
            elif self.cc == '5':
                self.one = self.optionedit1.toPlainText()
                self.two = self.optionedit2.toPlainText()
                self.three = self.optionedit3.toPlainText()
                self.four = self.optionedit4.toPlainText()
                self.five = self.optionedit5.toPlainText()
                self.mcqs = tex + self.one + self.two + self.three + self.four + self.five
                cur.execute("CREATE TABLE IF NOT EXISTS ProbabilityOb (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO ProbabilityOb (QDes, Email) VALUES (?,?)", (self.mcqs, self.email))
                cur.execute(f"SELECT QDes FROM ProbabilityOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()


            else:
                print("yes")
                cur.execute("CREATE TABLE IF NOT EXISTS ProbabilitySub (QDes TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")
                cur.execute("INSERT INTO ProbabilitySub (QDes, Email) VALUES (?,?)", (tex, self.email))
                cur.execute(f"SELECT QDes FROM ProbabilitySub WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                conn.commit()
                conn.close()






    @qtc.pyqtSlot(str)
    def updatefield(self, word):
        self.word = word
        self.cursor = self.editor.textCursor()
        self.cursor.insertText(self.word)

    @qtc.pyqtSlot(str, str)
    def update(self, po, ba):
        self.po = po
        self.ba = ba
        self.cursor = self.editor.textCursor()
        self.cursor.insertText(self.po)
        self.cursor.insertText(self.ba)

    @qtc.pyqtSlot(str)
    def matrixupdate(self, arry):
        self.arry = arry
        self.cursor = self.editor.textCursor()
        self.cursor.insertText(self.arry)

    @qtc.pyqtSlot(str)
    def squpdate(self, s):
        self.s = s
        #self.sqaures = sqrt(self.s)
        print("hello")
        #self.q = ["$\frac{a}{b}$"]
        #self.q = r'\overline{b}^3'
        self.q = r"$"+ "frac{a}{b}" + r"$"
        #self.label =u'\u222B'
        print(self.q)  #\sqrt{self.s}
        self.cursor = self.editor.textCursor()
        self.cursor.insertText(self.q)
        #self.cursor.setMarkdown(self.q)


    def create_menu_bar(self):
        menuBar = QMenuBar(self)

        """ add elements to the menubar """
        # App icon will go here
        app_icon = menuBar.addMenu(QIcon("doc_icon.png"), "icon")

        # file menu **
        file_menu = QMenu("File", self)
        menuBar.addMenu(file_menu)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.file_save)
        file_menu.addAction(save_action)

        open_action = QAction('Open', self)
        open_action.triggered.connect(self.file_open)
        file_menu.addAction(open_action)

        rename_action = QAction('Rename', self)
        rename_action.triggered.connect(self.file_saveas)
        file_menu.addAction(rename_action)

        pdf_action = QAction("Save as PDF", self)
        pdf_action.triggered.connect(self.save_pdf)
        file_menu.addAction(pdf_action)


        # edit menu **
        edit_menu = QMenu("Edit", self)
        menuBar.addMenu(edit_menu)

        # paste
        paste_action = QAction('Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        edit_menu.addAction(paste_action)

        # clear
        clear_action = QAction('Clear', self)
        clear_action.triggered.connect(self.editor.clear)
        edit_menu.addAction(clear_action)

        # select all
        select_action = QAction('Select All', self)
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        # view menu **
        view_menu = QMenu("View", self)
        menuBar.addMenu(view_menu)

        # fullscreen
        fullscr_action = QAction('Full Screen View', self)
        fullscr_action.triggered.connect(lambda : self.showFullScreen())
        view_menu.addAction(fullscr_action)

        # normal screen
        normscr_action = QAction('Normal View', self)
        normscr_action.triggered.connect(lambda : self.showNormal())
        view_menu.addAction(normscr_action)

        # minimize
        minscr_action = QAction('Minimize', self)
        minscr_action.triggered.connect(lambda : self.showMinimized())
        view_menu.addAction(minscr_action)

        self.setMenuBar(menuBar)

    def create_toolbar(self):
        # Using a title
        ToolBar = QToolBar("Tools", self)

        # undo
        undo_action = QAction(QIcon("undo.png"), 'Undo', self)
        undo_action.triggered.connect(self.editor.undo)
        ToolBar.addAction(undo_action)

        # redo
        redo_action = QAction(QIcon("redo.png"), 'Redo', self)
        redo_action.triggered.connect(self.editor.redo)
        ToolBar.addAction(redo_action)

        # adding separator
        ToolBar.addSeparator()

        # copy
        copy_action = QAction(QIcon("copy.png"), 'Copy', self)
        copy_action.triggered.connect(self.editor.copy)
        ToolBar.addAction(copy_action)

        # cut
        cut_action = QAction(QIcon("cut.png"), 'Cut', self)
        cut_action.triggered.connect(self.editor.cut)
        ToolBar.addAction(cut_action)

        # paste
        paste_action = QAction(QIcon("paste.png"), 'Paste', self)
        paste_action.triggered.connect(self.editor.paste)
        ToolBar.addAction(paste_action)

        # adding separator
        ToolBar.addSeparator()
        ToolBar.addSeparator()

        # fonts
        self.font_combo = QComboBox(self)
        self.font_combo.addItems(["Courier Std", "Hellentic Typewriter Regular", "Helvetica", "Arial", "SansSerif", "Helvetica", "Times", "Monospace"])
        self.font_combo.activated.connect(self.set_font)      # connect with function
        ToolBar.addWidget(self.font_combo)

        # font size
        self.font_size = QSpinBox(self)
        self.font_size.setValue(12)
        self.font_size.valueChanged.connect(self.set_font_size)      # connect with funcion
        ToolBar.addWidget(self.font_size)

        # separator
        ToolBar.addSeparator()

        # bold
        bold_action = QAction(QIcon("bold.png"), 'Bold', self)
        bold_action.triggered.connect(self.bold_text)
        ToolBar.addAction(bold_action)

        # underline
        underline_action = QAction(QIcon("underline.png"), 'Underline', self)
        underline_action.triggered.connect(self.underline_text)
        ToolBar.addAction(underline_action)

        # italic
        italic_action = QAction(QIcon("italic.png"), 'Italic', self)
        italic_action.triggered.connect(self.italic_text)
        ToolBar.addAction(italic_action)

        # separator
        ToolBar.addSeparator()

        # text alignment
        right_alignment_action = QAction(QIcon("alignright.png"), 'Align Right', self)
        right_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignRight))
        ToolBar.addAction(right_alignment_action)

        left_alignment_action = QAction(QIcon("alignleft.png"), 'Align Left', self)
        left_alignment_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignLeft))
        ToolBar.addAction(left_alignment_action)

        justification_action = QAction(QIcon("aligncenter.png"), 'Center/Justify', self)
        justification_action.triggered.connect(lambda : self.editor.setAlignment(Qt.AlignCenter))
        ToolBar.addAction(justification_action)


        ToolBar.addSeparator()


        subAction = QAction(QIcon("icons/subscript.png"),"Subscript",self)
        subAction.triggered.connect(self.subScript)
        ToolBar.addAction(subAction)

        superAction = QAction(QIcon("icons/superscript.png"),"Superscript",self)
        superAction.triggered.connect(self.superScript)
        ToolBar.addAction(superAction)

        overLineAction = QAction(QIcon("icons/superscript.png"),"OverLine",self)
        overLineAction.triggered.connect(self.overLine)
        ToolBar.addAction(overLineAction)


        # separator


        # zoom in
        #zoom_in_action = QAction(QIcon("zoom-in.png"), 'Zoom in', self)
        #zoom_in_action.triggered.connect(self.editor.zoomIn)
        #ToolBar.addAction(zoom_in_action)

        # zoom out
        #zoom_out_action = QAction(QIcon("zoom-out.png"), 'Zoom out', self)
        #zoom_out_action.triggered.connect(self.editor.zoomOut)
        #ToolBar.addAction(zoom_out_action)


        # separator
        ToolBar.addSeparator()

        self.addToolBar(ToolBar)


    def strike(self):
        # Grab the text's format
        fmt = self.editor.currentCharFormat()
        # Set the fontStrikeOut property to its opposite
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        #fmt.setFontUnderline(fmt.fontUnderline())
        # And set the next char format
        self.editor.setCurrentCharFormat(fmt)

    def overLine(self):
        # Grab the current format
        fmt = self.editor.currentCharFormat()
        # And get the vertical alignment property
        #align = fmt.verticalAlignment()
        align = fmt.fontOverline()

        # Toggle the state
        if align == QTextCharFormat.AlignNormal:
            #fmt.setVerticalAlignment(QTextCharFormat.fontUnderline)
            #fmt.setFontUnderline(QTextCharFormat.fontUnderline)
            fmt.setFontOverline(True)

        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        # Set the new format
        self.editor.setCurrentCharFormat(fmt)

    def subScript(self):
        # Grab the current format
        fmt = self.editor.currentCharFormat()
        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSubScript)

        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        # Set the new format
        self.editor.setCurrentCharFormat(fmt)

    def superScript(self):
        # Grab the current format
        fmt = self.editor.currentCharFormat()
        # And get the vertical alignment property
        align = fmt.verticalAlignment()

        # Toggle the state
        if align == QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)

        else:
            fmt.setVerticalAlignment(QTextCharFormat.AlignNormal)

        # Set the new format
        self.editor.setCurrentCharFormat(fmt)

    def italic_text(self):
        # if already italic, change into normal, else italic
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))

    def underline_text(self):
        # if already underlined, change into normal, else underlined
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))

    def bold_text(self):

        if self.editor.fontWeight() != QFont.Bold:
            self.editor.setFontWeight(QFont.Bold)


    def set_font(self):
        font = self.font_combo.currentText()
        self.editor.setCurrentFont(QFont(font))


    def set_font_size(self):
        value = self.font_size.value()
        self.editor.setFontPointSize(value)


        # we can also make it one liner without writing such function.
        # by using lamba function -
        # self.font_size.valueChanged.connect(self.editor.setFontPointSize(self.font_size.value()))


    def file_open(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.text);Text documents (*.txt);All files (*.*)")

        try:
            #with open(self.path, 'r') as f:
            #    text = f.read()
            text = docx2txt.process(self.path) # docx2txt
            #doc = Document(self.path)         # if using docx
            #text = ''
            #for line in doc.paragraphs:
            #    text += line.text
        except Exception as e:
            print(e)
        else:
            self.editor.setText(text)
            self.update_title()

    def file_save(self):
        print(self.path)
        if self.path == '':
            # If we do not have a path, we need to use Save As.
            self.file_saveas()

        text = self.editor.toPlainText()

        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def file_saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "text documents (*.text);Text documents (*.txt);All files (*.*)")

        if self.path == '':
            return   # If dialog is cancelled, will return ''

        text = self.editor.toPlainText()

        try:
            with open(path, 'w') as f:
                f.write(text)
                self.update_title()
        except Exception as e:
            print(e)

    def update_title(self):
        self.setWindowTitle(self.title + ' ' + self.path)

    def save_pdf(self):
        f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All files()")
        print(f_name)

        if f_name != '':  # if name not empty
           printer = QPrinter(QPrinter.HighResolution)
           printer.setOutputFormat(QPrinter.PdfFormat)
           printer.setOutputFileName(f_name)
           self.editor.document().print_(printer)


###################################################################

###################################################################


class Ui_keyboard(MainApp):
    submitted = qtc.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        #MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")

        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        #self.pushButton_2.setIcon(QIcon("image : url(cal1.png);"))
        self.pushButton.setStyleSheet("background-color:white;\n"
        "image : url(cal1.png);")
        self.pushButton.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setStyleSheet("background-color:white;\n"
        "image : url(cal2.png);")
        self.pushButton_2.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_3.setStyleSheet("background-color:white;\n"
        "image : url(cal3.png);")
        self.pushButton_3.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_3, 1, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_4.setStyleSheet("background-color:white;\n"
        "image : url(cal4.png);")
        self.pushButton_4.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_5.setStyleSheet("background-color:white;\n"
        "image : url(cal5.png);")
        self.pushButton_5.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_5, 1, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_6.setStyleSheet("background-color:white;\n"
        "image : url(cal6.png);")
        self.pushButton_6.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_6, 1, 5, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_7.setStyleSheet("background-color:white;\n"
        "image : url(cal7.png);")
        self.pushButton_7.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_7, 1, 6, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_8.setStyleSheet("background-color:white;\n"
        "image : url(cal8.png);")
        self.pushButton_8.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_8, 1, 7, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_9.setStyleSheet("background-color:white;\n"
        "image : url(cal9.png);")
        self.pushButton_9.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_9, 1, 8, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_10.setStyleSheet("background-color:white;\n"
        "image : url(cal10.png);")
        self.pushButton_10.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_10, 2, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_11.setStyleSheet("background-color:white;\n"
        "image : url(cal11.png);")
        self.pushButton_11.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_11, 2, 1, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_12.setStyleSheet("background-color:white;\n"
        "image : url(cal12.png);")
        self.pushButton_12.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_14.setStyleSheet("background-color:white;\n"
        "image : url(cal13.png);")
        self.pushButton_14.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_14, 2, 3, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_15.setStyleSheet("background-color:white;\n"
        "image : url(cal14.png);")
        self.pushButton_15.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_15, 2, 4, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_16.setStyleSheet("background-color:white;\n"
        "image : url(cal15.png);")
        self.pushButton_16.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_16, 2, 5, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_17.setStyleSheet("background-color:white;\n"
        "image : url(cal16.png);")
        self.pushButton_17.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_17, 2, 6, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_18.setStyleSheet("background-color:white;\n"
        "image : url(cal18.png);")
        self.pushButton_18.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_18, 2, 7, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_19.sizePolicy().hasHeightForWidth())
        self.pushButton_19.setSizePolicy(sizePolicy)
        self.pushButton_19.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_19.setStyleSheet("background-color:white;\n"
        "image : url(cal19.png);")
        self.pushButton_19.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_19, 2, 8, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy)
        self.pushButton_20.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_20.setStyleSheet("background-color:white;\n"
        "image : url(cal20.png);")
        self.pushButton_20.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_20, 3, 0, 1, 1)
        self.pushButton21 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton21.sizePolicy().hasHeightForWidth())
        self.pushButton21.setSizePolicy(sizePolicy)
        self.pushButton21.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton21.setStyleSheet("background-color:white;\n"
        "image : url(cal21.png);")
        self.pushButton21.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton21, 3, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_22.setStyleSheet("background-color:white;\n"
        "image : url(cal22.png);")
        self.pushButton_22.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_22, 3, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_23.setStyleSheet("background-color:white;\n"
        "image : url(cal23.png);")
        self.pushButton_23.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_23, 3, 3, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_24.setStyleSheet("background-color:white;\n"
        "image : url(cal24.png);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_24, 3, 4, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)
        self.pushButton_26.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_26.setStyleSheet("background-color:white;\n"
        "image : url(cal25.png);")
        self.pushButton_26.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_26, 3, 5, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)
        self.pushButton_27.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_27.setStyleSheet("background-color:white;\n"
        "image : url(cal26.png);")
        self.pushButton_27.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_27, 3, 6, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_28.setStyleSheet("background-color:white;\n"
        "image : url(cal27.png);")
        self.pushButton_28.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_28, 3, 7, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)
        self.pushButton_29.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_29.setStyleSheet("background-color:white;\n"
        "image : url(cal28.png);")
        self.pushButton_29.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_29, 3, 8, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)
        self.pushButton_30.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_30.setStyleSheet("background-color:white;\n"
        "image : url(cal29.png);")
        self.pushButton_30.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_30, 4, 0, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setText("ε")
        self.pushButton_31.setSizePolicy(sizePolicy)
        self.pushButton_31.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_31.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_31.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_31, 4, 1, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)
        self.pushButton_32.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_32.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_32.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_32, 4, 2, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)
        self.pushButton_34.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_34.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_34.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_34, 4, 3 , 1, 1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)
        self.pushButton_36.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_36.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_36.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_36, 4, 4, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_37.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_37.setObjectName("pushButton_33")
        self.gridLayout.addWidget(self.pushButton_37, 4, 5, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        self.pushButton_38.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_38.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_38.setObjectName("pushButton_34")
        self.gridLayout.addWidget(self.pushButton_38, 4, 6, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy)
        self.pushButton_39.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_39.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_39.setObjectName("pushButton_35")
        self.gridLayout.addWidget(self.pushButton_39, 4, 7, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy)
        self.pushButton_40.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_40.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_40.setObjectName("pushButton_36")
        self.gridLayout.addWidget(self.pushButton_40, 4, 8, 1, 1)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy)
        self.pushButton_41.setMaximumSize(QtCore.QSize(50, 50))
        #self.pushButton_2.setIcon(QIcon("image : url(cal1.png);"))
        self.pushButton_41.setStyleSheet("background-color:white;\n"
        "image : url(lin1.png);")
        self.pushButton_41.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_41, 1, 9, 1, 1)

        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_42.sizePolicy().hasHeightForWidth())
        self.pushButton_42.setSizePolicy(sizePolicy)
        self.pushButton_42.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_42.setStyleSheet("background-color:white;\n"
        "image : url(lin2.png);")
        self.pushButton_42.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_42, 1, 10, 1, 1)
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_43.sizePolicy().hasHeightForWidth())
        self.pushButton_43.setSizePolicy(sizePolicy)
        self.pushButton_43.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_43.setStyleSheet("background-color:white;\n"
        "image : url(lin3.png);")
        self.pushButton_43.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_43, 2, 9, 1, 1)
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy)
        self.pushButton_44.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_44.setStyleSheet("background-color:white;\n"
        "image : url(lin4.png);")
        self.pushButton_44.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_44, 2, 10, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy)
        self.pushButton_45.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_45.setStyleSheet("background-color:white;\n"
        "image : url(lin5.png);")
        self.pushButton_45.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_45, 3, 9, 1, 1)
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy)
        self.pushButton_46.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_46.setStyleSheet("background-color:white;\n"
        "image : url(lin6.png);")
        self.pushButton_46.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_46, 3, 10, 1, 1)
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        self.pushButton_47.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_47.setStyleSheet("background-color:white;\n"
        "image : url(lin7.png);")
        self.pushButton_47.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_47, 4, 9, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy)
        self.pushButton_48.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_48.setStyleSheet("background-color:white;\n"
        "image : url(lin8.png);")
        self.pushButton_48.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_48, 4, 10, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        self.pushButton_49.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_49.setStyleSheet("background-color:white;\n"
        "image : url(lin9.png);")
        self.pushButton_49.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_49, 5, 0, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy)
        self.pushButton_50.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_50.setStyleSheet("background-color:white;\n"
        "image : url(lin10.png);")
        self.pushButton_50.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_50, 5, 1, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy)
        self.pushButton_51.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_51.setStyleSheet("background-color:white;\n"
        "image : url(lin11.png);")
        self.pushButton_51.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_51, 5, 2, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy)
        self.pushButton_52.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_52.setStyleSheet("background-color:white;\n"
        "image : url(lin12.png);")
        self.pushButton_52.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_52, 5, 3, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy)
        self.pushButton_54.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_54.setStyleSheet("background-color:white;\n"
        "image : url(lin13.png);")
        self.pushButton_54.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_54, 5, 4, 1, 1)
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy)
        self.pushButton_55.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_55.setStyleSheet("background-color:white;\n"
        "image : url(lin14.png);")
        self.pushButton_55.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_55, 5, 5, 1, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_56.sizePolicy().hasHeightForWidth())
        self.pushButton_56.setSizePolicy(sizePolicy)
        self.pushButton_56.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_56.setStyleSheet("background-color:white;\n"
        "image : url(lin15.png);")
        self.pushButton_56.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_56, 5, 6, 1, 1)
        #self.pushButton_16.clicked.connect(self.powba)
        self.pushButton_57 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_57.sizePolicy().hasHeightForWidth())
        self.pushButton_57.setSizePolicy(sizePolicy)
        self.pushButton_57.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_57.setStyleSheet("background-color:white;\n"
        "image : url(lin16.png);")
        self.pushButton_57.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_57, 5, 7, 1, 1)
        self.pushButton_57.clicked.connect(self.powba)
        self.pushButton_58 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_58.sizePolicy().hasHeightForWidth())
        self.pushButton_58.setSizePolicy(sizePolicy)
        self.pushButton_58.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_58.setStyleSheet("background-color:white;\n"
        "image : url(lin17.png);")
        self.pushButton_58.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_58, 5, 8, 1, 1)
        self.pushButton_58.clicked.connect(self.base)
        self.pushButton_59 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_59.sizePolicy().hasHeightForWidth())
        self.pushButton_59.setSizePolicy(sizePolicy)
        self.pushButton_59.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_59.setStyleSheet("background-color:white;\n"
        "image : url(lin18.png);")
        self.pushButton_59.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_59, 5, 9, 1, 1)
        self.pushButton_59.clicked.connect(self.base)
        self.pushButton_60 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_60.sizePolicy().hasHeightForWidth())
        self.pushButton_60.setSizePolicy(sizePolicy)
        self.pushButton_60.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_60.setStyleSheet("background-color:white;\n"
        "image : url(lin19.png);")
        self.pushButton_60.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_60, 5, 10, 1, 1)
        self.pushButton_60.clicked.connect(self.base)

        self.pushButton61 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton61.sizePolicy().hasHeightForWidth())
        self.pushButton61.setSizePolicy(sizePolicy)
        self.pushButton61.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton61.setStyleSheet("background-color:white;\n"
        "image : url(lin20.png);")
        self.pushButton61.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton61, 6, 0, 1, 1)

        self.pushButton_62 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_62.sizePolicy().hasHeightForWidth())
        self.pushButton_62.setSizePolicy(sizePolicy)
        self.pushButton_62.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_62.setStyleSheet("background-color:white;\n"
        "image : url(lin21.png);")
        self.pushButton_62.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_62, 6, 1, 1, 1)
        self.pushButton_62.clicked.connect(self.powba)
        self.pushButton_63 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_63.sizePolicy().hasHeightForWidth())
        self.pushButton_63.setSizePolicy(sizePolicy)
        self.pushButton_63.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_63.setStyleSheet("background-color:white;\n"
        "image : url(lin22.png);")
        self.pushButton_63.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_63, 6, 2, 1, 1)
        self.pushButton_63.clicked.connect(self.powba)
        self.pushButton_64 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_64.sizePolicy().hasHeightForWidth())
        self.pushButton_64.setSizePolicy(sizePolicy)
        self.pushButton_64.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_64.setStyleSheet("background-color:white;\n"
        "image : url(lin23.png);")
        self.pushButton_64.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_64, 6, 3, 1, 1)
        self.pushButton_64.clicked.connect(self.base)
        self.pushButton_66 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_66.sizePolicy().hasHeightForWidth())
        self.pushButton_66.setSizePolicy(sizePolicy)
        self.pushButton_66.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_66.setStyleSheet("background-color:white;\n"
        "image : url(lin24.png);")
        self.pushButton_66.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_66, 6, 4, 1, 1)
        self.pushButton_66.clicked.connect(self.base)
        self.pushButton_67 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_67.sizePolicy().hasHeightForWidth())
        self.pushButton_67.setSizePolicy(sizePolicy)
        self.pushButton_67.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_67.setStyleSheet("background-color:white;\n"
        "image : url(lin25.png);")
        self.pushButton_67.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_67, 6, 5, 1, 1)
        self.pushButton_68 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_68.sizePolicy().hasHeightForWidth())
        self.pushButton_68.setSizePolicy(sizePolicy)
        self.pushButton_68.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_68.setStyleSheet("background-color:white;\n"
        "image : url(lin26.png);")
        self.pushButton_68.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_68, 6, 6, 1, 1)
        self.pushButton_69 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_69.sizePolicy().hasHeightForWidth())
        self.pushButton_69.setSizePolicy(sizePolicy)
        self.pushButton_69.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_69.setStyleSheet("background-color:white;\n"
        "image : url(lin27.png);")
        self.pushButton_69.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_69, 6, 7, 1, 1)
        self.pushButton_70 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_70.sizePolicy().hasHeightForWidth())
        self.pushButton_70.setSizePolicy(sizePolicy)
        self.pushButton_70.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_70.setStyleSheet("background-color:white;\n"
        "image : url(lin28.png);")
        self.pushButton_70.setObjectName("pushButton_21")
        self.gridLayout.addWidget(self.pushButton_70, 6, 8, 1, 1)
        self.pushButton_71 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_71.sizePolicy().hasHeightForWidth())
        self.pushButton_71.setSizePolicy(sizePolicy)
        self.pushButton_71.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_71.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_71.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_71, 6, 9, 1, 1)
        self.pushButton_72 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_72.sizePolicy().hasHeightForWidth())
        self.pushButton_72.setSizePolicy(sizePolicy)
        self.pushButton_72.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_72.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_72.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_72, 6, 10, 1, 1)
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_74.sizePolicy().hasHeightForWidth())
        self.pushButton_74.setSizePolicy(sizePolicy)
        self.pushButton_74.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_74.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_74.setObjectName("pushButton_20")
        self.gridLayout.addWidget(self.pushButton_74, 7, 0 , 1, 1)
        self.pushButton_76 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_76.sizePolicy().hasHeightForWidth())
        self.pushButton_76.setSizePolicy(sizePolicy)
        self.pushButton_76.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_76.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_76.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_76, 7, 1, 1, 1)
        self.pushButton_77 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_77.sizePolicy().hasHeightForWidth())
        self.pushButton_77.setSizePolicy(sizePolicy)
        self.pushButton_77.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_77.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_77.setObjectName("pushButton_33")
        self.gridLayout.addWidget(self.pushButton_77, 7, 2, 1, 1)
        self.pushButton_78 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_78.sizePolicy().hasHeightForWidth())
        self.pushButton_78.setSizePolicy(sizePolicy)
        self.pushButton_78.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_78.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_78.setObjectName("pushButton_34")
        self.gridLayout.addWidget(self.pushButton_78, 7, 3, 1, 1)
        self.pushButton_79 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_79.sizePolicy().hasHeightForWidth())
        self.pushButton_79.setSizePolicy(sizePolicy)
        self.pushButton_79.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_79.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_79.setObjectName("pushButton_35")
        self.gridLayout.addWidget(self.pushButton_79, 7, 4, 1, 1)
        self.pushButton_80 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_80.sizePolicy().hasHeightForWidth())
        self.pushButton_80.setSizePolicy(sizePolicy)
        self.pushButton_80.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_80.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_80.setObjectName("pushButton_36")
        self.gridLayout.addWidget(self.pushButton_80, 7, 5, 1, 1)

        self.pushButton_81 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_81.sizePolicy().hasHeightForWidth())
        self.pushButton_81.setSizePolicy(sizePolicy)
        self.pushButton_81.setMaximumSize(QtCore.QSize(50, 50))
        #self.pushButton_2.setIcon(QIcon("image : url(cal1.png);"))
        self.pushButton_81.setStyleSheet("background-color:white;\n"
        "image : url(lin15.png);")
        self.pushButton_81.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_81, 7, 6, 1, 1)
        self.pushButton_82 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_82.sizePolicy().hasHeightForWidth())
        self.pushButton_82.setSizePolicy(sizePolicy)
        self.pushButton_82.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_82.setStyleSheet("background-color:white;\n"
        "image : url(lin16.png);")
        self.pushButton_82.setObjectName("pushButton_26")
        self.gridLayout.addWidget(self.pushButton_82, 7, 7, 1, 1)
        self.pushButton_83 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_83.sizePolicy().hasHeightForWidth())
        self.pushButton_83.setSizePolicy(sizePolicy)
        self.pushButton_83.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_83.setStyleSheet("background-color:white;\n"
        "image : url(lin17.png);")
        self.pushButton_83.setObjectName("pushButton_29")
        self.gridLayout.addWidget(self.pushButton_83, 7, 8, 1, 1)
        self.pushButton_84 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_84.sizePolicy().hasHeightForWidth())
        self.pushButton_84.setSizePolicy(sizePolicy)
        self.pushButton_84.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_84.setStyleSheet("background-color:white;\n"
        "image : url(lin18.png);")
        self.pushButton_84.setObjectName("pushButton_18")
        self.gridLayout.addWidget(self.pushButton_84, 7, 9, 1, 1)
        self.pushButton_85 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_85.sizePolicy().hasHeightForWidth())
        self.pushButton_85.setSizePolicy(sizePolicy)
        self.pushButton_85.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_85.setStyleSheet("background-color:white;\n"
        "image : url(lin19.png);")
        self.pushButton_85.setObjectName("pushButton_28")
        self.gridLayout.addWidget(self.pushButton_85, 7, 10, 1, 1)
        self.pushButton_86 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_86.sizePolicy().hasHeightForWidth())
        self.pushButton_86.setSizePolicy(sizePolicy)
        self.pushButton_86.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_86.setStyleSheet("background-color:white;\n"
        "image : url(cal1.png);")
        self.pushButton_86.setObjectName("pushButton_31")
        self.gridLayout.addWidget(self.pushButton_86, 8, 0, 1, 1)
        self.pushButton_87 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_87.sizePolicy().hasHeightForWidth())
        self.pushButton_87.setSizePolicy(sizePolicy)
        self.pushButton_87.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_87.setStyleSheet("background-color:white;\n"
        "image : url(cal2.png);")
        self.pushButton_87.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_87, 8, 1, 1, 1)
        self.pushButton_88 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_88.sizePolicy().hasHeightForWidth())
        self.pushButton_88.setSizePolicy(sizePolicy)
        self.pushButton_88.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_88.setStyleSheet("background-color:white;\n"
        "image : url(cal3.png);")
        self.pushButton_88.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_88, 8, 2, 1, 1)
        self.pushButton_89 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_89.sizePolicy().hasHeightForWidth())
        self.pushButton_89.setSizePolicy(sizePolicy)
        self.pushButton_89.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_89.setStyleSheet("background-color:white;\n"
        "image : url(pro1.png);")
        self.pushButton_89.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_89, 8, 3, 1, 1)
        self.pushButton_90 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_90.sizePolicy().hasHeightForWidth())
        self.pushButton_90.setSizePolicy(sizePolicy)
        self.pushButton_90.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_90.setStyleSheet("background-color:white;\n"
        "image : url(pro2.png);")
        self.pushButton_90.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_90, 8, 4, 1, 1)
        self.pushButton_91 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_91.sizePolicy().hasHeightForWidth())
        self.pushButton_91.setSizePolicy(sizePolicy)
        self.pushButton_91.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_91.setStyleSheet("background-color:white;\n"
        "image : url(pro3.png);")
        self.pushButton_91.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_91, 8, 5, 1, 1)
        self.pushButton_92 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_92.sizePolicy().hasHeightForWidth())
        self.pushButton_92.setSizePolicy(sizePolicy)
        self.pushButton_92.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_92.setText("⋂")
        self.pushButton_92.setStyleSheet("background-color:white;\n"
        "font-size: 20px;")
        self.pushButton_92.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_92, 8, 6, 1, 1)
    #    self.pushButton_92.clicked.connect(self.write)

        self.pushButton_94 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_94.sizePolicy().hasHeightForWidth())
        self.pushButton_94.setSizePolicy(sizePolicy)
        self.pushButton_94.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_94.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
    )
        self.pushButton_94.setObjectName("pushButton_19")
        self.gridLayout.addWidget(self.pushButton_94, 8, 7, 1, 1)
        self.pushButton_95 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_95.sizePolicy().hasHeightForWidth())
        self.pushButton_95.setSizePolicy(sizePolicy)
        self.pushButton_95.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_95.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_95.setObjectName("pushButton_23")
        self.gridLayout.addWidget(self.pushButton_95, 8, 8, 1, 1)
        self.pushButton_96 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_96.sizePolicy().hasHeightForWidth())
        self.pushButton_96.setSizePolicy(sizePolicy)
        self.pushButton_96.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_96.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_96.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_96, 8, 9, 1, 1)
        self.pushButton_97 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_97.sizePolicy().hasHeightForWidth())
        self.pushButton_97.setSizePolicy(sizePolicy)
        self.pushButton_97.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_97.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_97.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_97, 8, 10, 1, 1)
        self.pushButton_98 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_98.sizePolicy().hasHeightForWidth())
        self.pushButton_98.setSizePolicy(sizePolicy)
        self.pushButton_98.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_98.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_98.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_98, 9, 0, 1, 1)
        self.pushButton_99 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_99.sizePolicy().hasHeightForWidth())
        self.pushButton_99.setSizePolicy(sizePolicy)
        self.pushButton_99.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_99.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
    )
        self.pushButton_99.setObjectName("pushButton_25")
        self.gridLayout.addWidget(self.pushButton_99, 9, 1, 1, 1)
        self.pushButton_100 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_100.sizePolicy().hasHeightForWidth())
        self.pushButton_100.setSizePolicy(sizePolicy)
        self.pushButton_100.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_100.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_100.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_100, 9, 2, 1, 1)
        self.pushButton101 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton101.sizePolicy().hasHeightForWidth())
        self.pushButton101.setSizePolicy(sizePolicy)
        self.pushButton101.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton101.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton101.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton101, 9, 3, 1, 1)
        #self.pushButton_12.clicked.connect(self.write)
        self.pushButton_102 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_102.sizePolicy().hasHeightForWidth())
        self.pushButton_102.setSizePolicy(sizePolicy)
        self.pushButton_102.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_102.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_102.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_102, 9, 4, 1, 1)
        self.pushButton_103 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_103.sizePolicy().hasHeightForWidth())
        self.pushButton_103.setSizePolicy(sizePolicy)
        self.pushButton_103.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_103.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
    )
        self.pushButton_103.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_103, 9, 5, 1, 1)
        self.pushButton_104 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_104.sizePolicy().hasHeightForWidth())
        self.pushButton_104.setSizePolicy(sizePolicy)
        self.pushButton_104.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_104.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_104.setObjectName("pushButton_24")
        self.gridLayout.addWidget(self.pushButton_104, 9, 6, 1, 1)
        self.pushButton_106 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_106.sizePolicy().hasHeightForWidth())
        self.pushButton_106.setSizePolicy(sizePolicy)
        self.pushButton_106.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_106.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_106.setObjectName("pushButton_32")
        self.gridLayout.addWidget(self.pushButton_106, 9, 7, 1, 1)
        self.pushButton_107 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_107.sizePolicy().hasHeightForWidth())
        self.pushButton_107.setSizePolicy(sizePolicy)
        self.pushButton_107.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_107.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_107.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_107, 9, 8, 1, 1)
        self.pushButton_108 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_108.sizePolicy().hasHeightForWidth())
        self.pushButton_108.setSizePolicy(sizePolicy)
        self.pushButton_108.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_108.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_108.setObjectName("pushButton_27")
        self.gridLayout.addWidget(self.pushButton_108, 9, 9, 1, 1)
        self.pushButton_109 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_109.sizePolicy().hasHeightForWidth())
        self.pushButton_109.setSizePolicy(sizePolicy)
        self.pushButton_109.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_109.setStyleSheet("background-color:white;\n"
        "font-size: 20px;"
        )
        self.pushButton_109.setObjectName("pushButton_30")
        self.gridLayout.addWidget(self.pushButton_109, 9, 10, 1, 1)


        #self.s = self.write(self.pushButton_31)
        #self.write(self.pushButton_31)
        self.pushButton_31.clicked.connect(self.write)
        self.pushButton_32.clicked.connect(self.write1)
        self.pushButton_7.clicked.connect(self.powba)
        self.pushButton_67.clicked.connect(self.matrix)
        self.pushButton_41.clicked.connect(self.opensqare)
        #self.pushButton_109.clicked.connect(self.doit)
        #self.p = self.pushButton_31.text()
        #print(self.p.encode("Utf-8"))

        #if self.p == "ε":
        #    print('helo')


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def opensqare(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Square()
        self.ui.setupUi(self.window)
        self.window.show()

    def powba(self):
        self.window = QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def matrix(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Matrix()
        self.ui.setupUi(self.window)
        self.window.show()

    #@qtc.pyqtSlot(str, str)
    #def powbass(self, p, b):
    #    print("helo")
    #    self.p = p
    #    self.b = b
    #    self.pushButton_32.setText(self.p)
        #print("helo")
        #self.send.emit(self.p, self.b)
        #print("helo")
        #self.cursor = self.editor.textCursor()
        #self.cursor.insertText(self.p)

    def power(self):
        self.window = QMainWindow()
        self.ui = Ui_power()
        self.ui.setupUi(self.window)
        self.window.show()

    def base(self):
        self.window = QMainWindow()
        self.ui = Ui_base()
        self.ui.setupUi(self.window)
        self.window.show()

    def write1(self):
        self.submitted.emit(self.pushButton_32.text())

    def write(self):
        self.submitted.emit(self.pushButton_31.text())
        #self.close()
        #self.read = self.pushButton_31.text()
        #print(self.read.encode('Utf-8'))
        #self.d = self.read.encode('Utf-8')
        #print(self.d)
        #self.window = QMainWindow()
        #ui = MainApp()
        #app = QtWidgets.QApplication(sys.argv)
        #self.editor.setText(self.read)
        #self.signal.editor.setText(self.read)
        #self.signal.
        #self.editor.setText(self.read)
        #print('he')
        #self.w = Ui_keyboard(MainApp)

        #self.window = MainApp()
        #self.window.show()
        #self.window.editor.setText(self.read)
        #MainApp.editor.setText(self.read)
        #self.editor.setText(self.read)
        #self.mainwin.editor.setText(self.read)
        #self.MainWindow.editor.setText(self.read)

    #def doit(self):
    #    self.w = subclass(self)
        #self.w.setGeometry(QRect(100, 100, 400, 200))
        #self.w.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Virtual Mathematics Symbol Keyboard"))
        MainWindow.setWindowIcon(QIcon("Splashlogo.png"))

        #self.pushButton_31.setText(_translate("MainWindow", "ε"))
        self.pushButton_32.setText(_translate("MainWindow", "δ"))
        self.pushButton_34.setText(_translate("MainWindow", "∞"))
        self.pushButton_36.setText(_translate("MainWindow", "∇"))
        self.pushButton_37.setText(_translate("MainWindow", "∂"))
        self.pushButton_38.setText(_translate("MainWindow", "ω"))
        self.pushButton_39.setText(_translate("MainWindow", "θ"))
        self.pushButton_40.setText(_translate("MainWindow", "→"))
        self.pushButton_71.setText(_translate("MainWindow", "π"))
        self.pushButton_72.setText(_translate("MainWindow", "φ"))
        self.pushButton_74.setText(_translate("MainWindow", "γ"))
        self.pushButton_76.setText(_translate("MainWindow", "∆"))
        self.pushButton_77.setText(_translate("MainWindow", "∘"))
        self.pushButton_78.setText(_translate("MainWindow", "⊗"))
        self.pushButton_79.setText(_translate("MainWindow", "∝"))
        self.pushButton_80.setText(_translate("MainWindow", "∞"))
        self.pushButton_94.setText(_translate("MainWindow", "⋃"))
        self.pushButton_95.setText(_translate("MainWindow", "|"))
        self.pushButton_96.setText(_translate("MainWindow", "μ"))
        self.pushButton_97.setText(_translate("MainWindow", "σ"))
        self.pushButton_98.setText(_translate("MainWindow", "~"))
        self.pushButton_99.setText(_translate("MainWindow", "λ"))
        self.pushButton_100.setText(_translate("MainWindow", "!"))
        self.pushButton101.setText(_translate("MainWindow", "⇒"))
        self.pushButton_102.setText(_translate("MainWindow", "↔"))
        self.pushButton_103.setText(_translate("MainWindow", "∴"))
        self.pushButton_104.setText(_translate("MainWindow", "∵"))
        self.pushButton_106.setText(_translate("MainWindow", "∫"))
        self.pushButton_107.setText(_translate("MainWindow", "⊗"))
        self.pushButton_108.setText(_translate("MainWindow", "∝"))
        self.pushButton_109.setText(_translate("MainWindow", "∞"))
###########################################################################

class Ui_Dialog(MainApp):
    submitt = qtc.pyqtSignal(str, str)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 210)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 47, 13))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 47, 13))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(140, 30, 81, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 90, 81, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.Okbtn = QtWidgets.QPushButton(Dialog)
        self.Okbtn.setText("OK")
        self.Okbtn.setGeometry(QtCore.QRect(100, 150, 100, 35))
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


        self.Okbtn.clicked.connect(self.clickOk)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #def call(self):
    #    self.window = MainApp()
    #    self.submitt.connect(self.window.update())

    def clickOk(self):
        self.pow = self.textEdit.toPlainText()
        self.bas = self.textEdit_2.toPlainText()
        #print("helo")
        #self.window = MainApp()
        #print("helo")
        #self.window.update(self.pow, self.bas)
        #self.window.show()
        #self.update(self.pow,self.bas)

        self.submitt.emit(self.pow,self.bas)
        self.submitt.connect(window.update)
        #self.
        #print("helo")



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Symbols Power and base"))
        Dialog.setWindowIcon(QIcon("Splashlogo.png"))
        self.label.setText(_translate("Dialog", "Power"))
        self.label_2.setText(_translate("Dialog", "Base"))


##################################################################

class Ui_Matrix(MainApp):
    pick = qtc.pyqtSignal(str)

    def setupUi(self, Matrix):
        Matrix.setObjectName("Matrix")
        Matrix.resize(400, 250)
        self.label = QtWidgets.QLabel(Matrix)
        self.label.setGeometry(QtCore.QRect(60, 40, 80, 13))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Matrix)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 120, 25))
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.textEdit = QtWidgets.QTextEdit(Matrix)
        self.textEdit.setGeometry(QtCore.QRect(150, 30, 60, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Matrix)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 30, 60, 41))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(Matrix)
        self.textEdit_3.setGeometry(QtCore.QRect(150, 100, 200, 41))
        self.textEdit_3.setObjectName("textEdit_3")

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
        self.Okbtn.clicked.connect(self.arrclick)
        self.retranslateUi(Matrix)
        QtCore.QMetaObject.connectSlotsByName(Matrix)

    def arrclick(self):
        self.d1 = int(self.textEdit.toPlainText())
        self.d2 = int(self.textEdit_2.toPlainText())
        self.arrmat = self.textEdit_3.toPlainText()
        self.matarry = self.arrmat.split(',')
        self.finalarr = np.array(self.matarry).reshape((self.d1, self.d2))
        self.res = str(self.finalarr)[1:-1]
        #self.pick.emit(str(self.finalarr))
        #self.mati = Matrix(self.finalarr)
        #pprint(self.mati)
        self.pick.emit(self.res)
        self.pick.connect(window.matrixupdate)



    def retranslateUi(self, Matrix):
        _translate = QtCore.QCoreApplication.translate
        Matrix.setWindowTitle(_translate("Matrix", "Dimension of the Array"))
        Matrix.setWindowIcon(QIcon("Splashlogo.png"))
        self.label.setText(_translate("Matrix", "Dimension"))
        self.label_2.setText(_translate("Matrix", "Enter an Array"))

################################################################

class Ui_Square(MainApp):
    quare = qtc.pyqtSignal(str)
    def setupUi(self, Sqaure):
        Sqaure.setObjectName("Sqaure")
        Sqaure.resize(292, 170)
        self.label = QtWidgets.QLabel(Sqaure)
        self.label.setGeometry(QtCore.QRect(60, 40, 47, 13))
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(Sqaure)
        self.textEdit.setGeometry(QtCore.QRect(140, 30, 81, 41))
        self.textEdit.setObjectName("textEdit")

        self.Okbtn = QtWidgets.QPushButton(Sqaure)
        self.Okbtn.setText("OK")
        self.Okbtn.setGeometry(QtCore.QRect(100, 110, 100, 35))
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
        self.Okbtn.clicked.connect(self.sqquare)
        self.retranslateUi(Sqaure)
        QtCore.QMetaObject.connectSlotsByName(Sqaure)

    def sqquare(self):
        self.sq = self.textEdit.toPlainText()
        #self.a = 3
        #self.sqq = sqrt(self.sq)
        #self.b = symbols('b')
        #self.expr = 1/self.b
        #print(self.expr)
        #print(self.sqq)
        #print(self.sqq)
        #self.quare.emit(str(self.sqq))
        self.quare.emit(self.sq)
        self.quare.connect(window.squpdate)


    def retranslateUi(self, Sqaure):
        _translate = QtCore.QCoreApplication.translate
        Sqaure.setWindowTitle(_translate("Dialog", "Symbols Power and base"))
        Sqaure.setWindowIcon(QIcon("Splashlogo.png"))
        self.label.setText(_translate("Dialog", "Value"))


##############################################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
