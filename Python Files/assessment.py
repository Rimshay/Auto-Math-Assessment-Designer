
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import textract
import source
import csv
import sqlite3
import shutil
import os
import webbrowser
import platform
import subprocess
import numpy as np
import pandas as pd
from ualreadyexist import *


class Ui_NewAssessment(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.TitleS = QtWidgets.QLabel(self.centralwidget)
        self.TitleS.setGeometry(QtCore.QRect(470, 40, 125, 25))
        self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.TitleS.setObjectName("Title")
        self.TypeS = QtWidgets.QLabel(self.centralwidget)
        self.TypeS.setGeometry(QtCore.QRect(600, 40, 100, 25))
        self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.TypeS.setObjectName("Type")
        self.Ques = QtWidgets.QLabel(self.centralwidget)
        self.Ques.setGeometry(QtCore.QRect(695, 40, 90, 25))
        self.Ques.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.Ques.setObjectName("Ques")

        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setStyleSheet("color:rgb(255, 255, 255);")
        self.label0.setGeometry(QtCore.QRect(20, 20, 95, 18))
        self.label0.setObjectName("label0")

        self.label1 = QtWidgets.QLineEdit(self.centralwidget)
        self.label1.setStyleSheet("color:rgb(25, 25, 25);")
        self.label1.setGeometry(QtCore.QRect(200, 170, 133, 25))
        self.label1.setObjectName("label1")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("font: 11pt \"Arial\";")
        self.label.setGeometry(QtCore.QRect(80, 50, 95, 18))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 90, 180, 18))
        self.label_2.setStyleSheet("font: 11pt \"Arial\";")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 180, 18))
        self.label_3.setStyleSheet("font: 11pt \"Arial\";")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 170, 180, 18))
        self.label_4.setStyleSheet("font: 11pt \"Arial\";")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 210, 111, 18))
        self.label_5.setStyleSheet("font: 11pt \"Arial\";")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 250, 111, 18))
        self.label_6.setStyleSheet("font: 11pt \"Arial\";")
        self.label_6.setObjectName("label_6")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(80, 290, 111, 18))
        self.label_8.setStyleSheet("font: 11pt \"Arial\";")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 330, 111, 18))
        self.label_9.setStyleSheet("font: 11pt \"Arial\";")
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(80, 370, 111, 18))
        self.label_10.setStyleSheet("font: 11pt \"Arial\";")
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 410, 170, 18))
        self.label_11.setStyleSheet("font: 11pt \"Arial\";")
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(80, 450, 170, 18))
        self.label_12.setStyleSheet("font: 11pt \"Arial\";")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(80, 490, 170, 18))
        self.label_13.setStyleSheet("font: 11pt \"Arial\";")
        self.label_13.setObjectName("label_13")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(80, 530, 170, 18))
        self.label_15.setStyleSheet("font: 11pt \"Arial\";")
        self.label_15.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 580, 170, 18))
        self.label_14.setStyleSheet("font: 11pt \"Arial\";")
        self.label_14.setObjectName("label_13")


        self.col = ['Questions', 'QDescription']
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(450, 100, 391, 401))
        self.tableView.setColumnCount(2)
        self.tableView.setHorizontalHeaderLabels(self.col)
        self.tableView.setObjectName("tableWidget")
        #self.tableWidget.setColumnCount(0)
        #self.tableWidget.setRowCount(0)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 50, 151, 25))
        self.comboBox.addItem("Linear Algebra")
        self.comboBox.addItem("Calculus")
        self.comboBox.addItem("Probability")
        self.comboBox.setStyleSheet("border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 9em;\n"
"min-height: 2em;\n")
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 90, 151, 25))
        self.comboBox_2.addItem("Subjective")
        self.comboBox_2.addItem("Objective")
        self.comboBox_2.setStyleSheet("border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 9em;\n"
"min-height: 2em;\n")
        self.comboBox_2.setObjectName("comboBox_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 130, 133, 25))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_3 = QtWidgets.QDateEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 210, 133, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QTimeEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 250, 133, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")


        #self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_5.setGeometry(QtCore.QRect(200, 290, 133, 25))
        #self.lineEdit_5.setObjectName("lineEdit_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(200, 290, 133, 25))
        self.comboBox_6.addItem("Linear Algebra")
        self.comboBox_6.addItem("Calculus")
        self.comboBox_6.addItem("Probability")
        self.comboBox_6.setStyleSheet("border: 1px solid gray;\n"
    "border-radius: 3px;\n"
    "padding: 1px 18px 1px 3px;\n"
    "min-width: 9em;\n"
    "min-height: 2em;\n")
        self.comboBox_6.setObjectName("comboBox_6")

        #self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_6.setGeometry(QtCore.QRect(180, 330, 133, 25))
        #self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(180, 330, 133, 25))
        self.comboBox_5.addItem("CSN103, SEN103")
        self.comboBox_5.addItem("CSN102, SEN102")
        self.comboBox_5.addItem("CSN201, SEN201")
        self.comboBox_5.setStyleSheet("border: 1px solid gray;\n"
    "border-radius: 3px;\n"
    "padding: 1px 18px 1px 3px;\n"
    "min-width: 9em;\n"
    "min-height: 2em;\n")
        self.comboBox_5.setObjectName("comboBox_5")

        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(180, 370, 133, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")

        #self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        #self.lineEdit_9.setGeometry(QtCore.QRect(250, 410, 133, 25))
        #self.lineEdit_9.setObjectName("lineEdit_9")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(250, 410, 133, 25))
        self.comboBox_4.addItem("Midterm")
        self.comboBox_4.addItem("Finalterm")
        self.comboBox_4.setStyleSheet("border: 1px solid gray;\n"
    "border-radius: 3px;\n"
    "padding: 1px 18px 1px 3px;\n"
    "min-width: 9em;\n"
    "min-height: 2em;\n")
        self.comboBox_4.setObjectName("comboBox_4")

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 450, 133, 25))
        self.comboBox_3.addItem("Spring 2021")
        self.comboBox_3.addItem("Fall 2021")
        self.comboBox_3.addItem("Summer2021")
        self.comboBox_3.addItem("Spring 2022")
        self.comboBox_3.addItem("Fall 2022")
        self.comboBox_3.addItem("Summer 2022")
        self.comboBox_3.addItem("Spring 2023")
        self.comboBox_3.addItem("Fall 2023")
        self.comboBox_3.addItem("Summer 2023")
        self.comboBox_3.addItem("Spring 2024")
        self.comboBox_3.setStyleSheet("border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 9em;\n"
"min-height: 2em;\n")
        self.comboBox_3.setObjectName("comboBox_3")

        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(200, 490, 133, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")


        self.lineEdit_13 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_13.setGeometry(QtCore.QRect(200, 530, 133, 25))
        self.lineEdit_13.setObjectName("lineEdit_12")


        self.lineEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(200, 580, 220, 80))
        self.lineEdit_12.setObjectName("lineEdit_12")


        self.GenerateDoc = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateDoc.setGeometry(QtCore.QRect(650, 530, 170, 35))
        self.GenerateDoc.setObjectName("generate")
        self.GenerateDoc.setStyleSheet("QPushButton#generate{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#generate:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#generate:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")

        self.RandomSearch = QtWidgets.QPushButton(self.centralwidget)
        self.RandomSearch.setGeometry(QtCore.QRect(490, 530, 130, 35))
        self.RandomSearch.setObjectName("random")
        self.RandomSearch.setStyleSheet("QPushButton#random{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#random:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#random:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")

        self.AllFetch = QtWidgets.QPushButton(self.centralwidget)
        self.AllFetch.setGeometry(QtCore.QRect(560, 580, 130, 35))
        self.AllFetch.setObjectName("random")
        self.AllFetch.setStyleSheet("QPushButton#random{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#random:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#random:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")

        self.RandomSearch.clicked.connect(self.viewRandomly)
        self.GenerateDoc.clicked.connect(self.save_var_latex)
        self.AllFetch.clicked.connect(self.fullfecth)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save_var_latex(self):
        try:
            self.sub = str(self.comboBox.currentText())
            self.typ = str(self.comboBox_2.currentText())
            self.tn = str(self.label1.text())
            self.d = str(self.lineEdit_3.date().toPyDate())
            self.t = str(self.lineEdit_4.time().toPyTime())
            self.cc = str(self.comboBox_6.currentText())
            self.ct = str(self.comboBox_5.currentText())
            self.tm = str(self.lineEdit_8.text())
            self.et = str(self.comboBox_4.currentText())
            self.Sy = str(self.comboBox_3.currentText())
            self.est = str(self.lineEdit_11.text())
            self.ifs = str(self.lineEdit_12.toPlainText())

            paths = []
            self.selected = self.tableView.selectedItems()
            print(self.selected)
            if self.selected:
                print("go")
                for item in self.selected:
                    print("go")
                    print(item.column())
                    if item.column() == 1:
                        print(item.column())
                        print("go")
                        paths.append(item.data(0))
                        print("go")
                    else:
                        print('select the rows')
            print(paths)
            print(len(paths))

#\Objective \\\\\\\\\\\\\\\\\\\\\\\Objective \\\\\\\\\\\\\\\\\\\\\\\\\ Objective
 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 1 Row Selected

            if len(paths) == 1 and self.typ == "Objective":
                self.val1 = paths[0]
                print(self.val1)
                self.comma = self.val1.count(',')
                print(self.comma)
                self.dic = self.val1.split(',', self.comma)
                print(self.dic)
                self.spli = f'sj'
                self.tag = '{oneparchoices}'

                if self.comma == 2:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    else:
                        print('yes')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]}  \end{self.tag}'
                    dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                    'course title':self.ct,
                    'total marks':self.tm,
                    'exam type':self.et,
                    'semesteryear':self.Sy,
                    'estimated time':self.est,
                    'teachername':self.tn,
                    'instruction':self.ifs,
                    'question1':self.spli,
                    'options1':self.objec
                    }
                    file_path =  os.path.join(os.getcwd(),"object.dat")
                    with open(file_path,"w") as f:
                        for key in dict_var.keys():
                            print(key)
                            print(dict_var[key])
                            print('yes')
                            f.write(f"{key},{dict_var[key]}\n")
                            print('hogya')

                    try:
                        file = str(self.lineEdit_13.text())
                        file = file + '.tex'
                        try:
                            finalfile = open(file, 'x')
                            with open('object.tex','r') as firstfile, open(file,'w') as secondfile:
                                for line in firstfile:
                                    secondfile.write(line)
                            tex_filename = file
                            filename, ext = os.path.splitext(tex_filename)
                            pdf_filename = filename + '.pdf'
                            subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                            path = pdf_filename
                            webbrowser.open_new(path)
                            conn = sqlite3.connect("Database.db")
                            cur = conn.cursor()
                            self.ema = str(self.label0.text())

                            cur.execute("CREATE TABLE IF NOT EXISTS AssessmentOb (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                            cur.execute("INSERT INTO AssessmentOb (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                            cur.execute(f"SELECT PDFDOC FROM AssessmentOb WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                            result = cur.fetchall()
                            conn.commit()
                            conn.close()
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("Successfully Saved")
                            self.Dialog.setWindowTitle("Confimation Message!")
                            self.Dialog.show()
                        except Exception as e:
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("File with this name already exist")
                            self.Dialog.setWindowTitle("Alert!")
                            self.Dialog.show()
                    except Exception as e:
                        print(e)

                elif self.comma == 3:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]}  \end{self.tag}'
                    dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                    'course title':self.ct,
                    'total marks':self.tm,
                    'exam type':self.et,
                    'semesteryear':self.Sy,
                    'estimated time':self.est,
                    'teachername':self.tn,
                    'instruction':self.ifs,
                    'question1':self.spli,
                    'options1':self.objec
                    }
                    file_path =  os.path.join(os.getcwd(),"object.dat")
                    with open(file_path,"w") as f:
                        for key in dict_var.keys():
                            print(key)
                            print(dict_var[key])
                            print('yes')
                            f.write(f"{key},{dict_var[key]}\n")
                            print('hogya')

                    try:
                        file = str(self.lineEdit_13.text())
                        file = file + '.tex'
                        try:
                            finalfile = open(file, 'x')
                            with open('object.tex','r') as firstfile, open(file,'w') as secondfile:
                                for line in firstfile:
                                    secondfile.write(line)
                            tex_filename = file
                            filename, ext = os.path.splitext(tex_filename)
                            pdf_filename = filename + '.pdf'
                            subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                            path = pdf_filename
                            webbrowser.open_new(path)
                            conn = sqlite3.connect("Database.db")
                            cur = conn.cursor()
                            self.ema = str(self.label0.text())

                            cur.execute("CREATE TABLE IF NOT EXISTS AssessmentOb (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                            cur.execute("INSERT INTO AssessmentOb (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                            cur.execute(f"SELECT PDFDOC FROM AssessmentOb WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                            result = cur.fetchall()
                            conn.commit()
                            conn.close()
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("Successfully Saved")
                            self.Dialog.setWindowTitle("Confimation Message!")
                            self.Dialog.show()
                        except Exception as e:
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("File with this name already exist")
                            self.Dialog.setWindowTitle("Alert!")
                            self.Dialog.show()
                    except Exception as e:
                        print(e)

                elif self.comma == 4:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]} \choice {self.dic[4]} \end{self.tag}'
                    dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                    'course title':self.ct,
                    'total marks':self.tm,
                    'exam type':self.et,
                    'semesteryear':self.Sy,
                    'estimated time':self.est,
                    'teachername':self.tn,
                    'instruction':self.ifs,
                    'question1':self.spli,
                    'options1':self.objec
                    }
                    file_path =  os.path.join(os.getcwd(),"object.dat")
                    with open(file_path,"w") as f:
                        for key in dict_var.keys():
                            print(key)
                            print(dict_var[key])
                            print('yes')
                            f.write(f"{key},{dict_var[key]}\n")
                            print('hogya')

                    try:
                        file = str(self.lineEdit_13.text())
                        file = file + '.tex'
                        try:
                            finalfile = open(file, 'x')
                            with open('object.tex','r') as firstfile, open(file,'w') as secondfile:
                                for line in firstfile:
                                    secondfile.write(line)
                            tex_filename = file
                            filename, ext = os.path.splitext(tex_filename)
                            pdf_filename = filename + '.pdf'
                            subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                            path = pdf_filename
                            webbrowser.open_new(path)
                            conn = sqlite3.connect("Database.db")
                            cur = conn.cursor()
                            self.ema = str(self.label0.text())

                            cur.execute("CREATE TABLE IF NOT EXISTS AssessmentOb (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                            cur.execute("INSERT INTO AssessmentOb (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                            cur.execute(f"SELECT PDFDOC FROM AssessmentOb WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                            result = cur.fetchall()
                            conn.commit()
                            conn.close()
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("Successfully Saved")
                            self.Dialog.setWindowTitle("Confimation Message!")
                            self.Dialog.show()
                        except Exception as e:
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("File with this name already exist")
                            self.Dialog.setWindowTitle("Alert!")
                            self.Dialog.show()
                    except Exception as e:
                        print(e)

                elif self.comma == 5:
                    self.spli = self.dic[0]
                    print('ok')
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]}   \choice {self.dic[2]} \choice {self.dic[3]} \choice {self.dic[4]} \choice {self.dic[5]} \end{self.tag}'
                    dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                    'course title':self.ct,
                    'total marks':self.tm,
                    'exam type':self.et,
                    'semesteryear':self.Sy,
                    'estimated time':self.est,
                    'teachername':self.tn,
                    'instruction':self.ifs,
                    'question1':self.spli,
                    'options1':self.objec
                    }
                    file_path =  os.path.join(os.getcwd(),"object.dat")
                    with open(file_path,"w") as f:
                        for key in dict_var.keys():
                            print(key)
                            print(dict_var[key])
                            print('yes')
                            f.write(f"{key},{dict_var[key]}\n")
                            print('hogya')

                    try:
                        file = str(self.lineEdit_13.text())
                        file = file + '.tex'
                        try:
                            finalfile = open(file, 'x')
                            with open('object.tex','r') as firstfile, open(file,'w') as secondfile:
                                for line in firstfile:
                                    secondfile.write(line)
                            tex_filename = file
                            filename, ext = os.path.splitext(tex_filename)
                            pdf_filename = filename + '.pdf'
                            subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                            path = pdf_filename
                            webbrowser.open_new(path)
                            conn = sqlite3.connect("Database.db")
                            cur = conn.cursor()
                            self.ema = str(self.label0.text())

                            cur.execute("CREATE TABLE IF NOT EXISTS AssessmentOb (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                            cur.execute("INSERT INTO AssessmentOb (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                            cur.execute(f"SELECT PDFDOC FROM AssessmentOb WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                            result = cur.fetchall()
                            conn.commit()
                            conn.close()
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("Successfully Saved")
                            self.Dialog.setWindowTitle("Confimation Message!")
                            self.Dialog.show()
                        except Exception as e:
                            self.Dialog = QtWidgets.QDialog()
                            self.ui = Ui_Email()
                            self.ui.setupUi(self.Dialog)
                            self.ui.label.setText("File with this name already exist")
                            self.Dialog.setWindowTitle("Alert!")
                            self.Dialog.show()
                    except Exception as e:
                        print(e)

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 2 Rows Selected \\\\\\\\\\\\\\\\\\\\\\\\\\\\

            elif len(paths) == 2 and self.typ == "Objective":
                self.val1 = paths[0]
                self.val2 = paths[1]
                self.comma = self.val1.count(',')
                self.dic = self.val1.split(',', self.comma)
                self.objec = f'gha'
                self.objec1 = f'gha'
                self.spli = ''
                self.spli1 = ''
                self.comma2 = self.val2.count(',')
                self.dic2 = self.val2.split(',', self.comma2)
                self.tag = '{oneparchoices}'

                if self.comma == 2:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    else:
                        print('yes')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]}  \end{self.tag}'

                elif self.comma == 3:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]}  \end{self.tag}'


                elif self.comma == 4:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]} \choice {self.dic[4]} \end{self.tag}'


                elif self.comma == 5:
                    self.spli = self.dic[0]
                    print('ok')
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]} \choice {self.dic[4]} \choice {self.dic[5]} \end{self.tag}'


#///////////////// option 2

                if self.comma2 == 2:
                    self.spli1 = self.dic2[0]
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    else:
                        print('yes')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]}  \end{self.tag}'

                elif self.comma2 == 3:
                    self.spli1 = self.dic2[0]
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]} \choice {self.dic2[3]}  \end{self.tag}'


                elif self.comma2 == 4:
                    self.spli1 = self.dic2[0]
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]} \choice {self.dic2[3]} \choice {self.dic2[4]} \end{self.tag}'


                elif self.comma2 == 5:
                    self.spli1 = self.dic2[0]
                    print('ok')
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]} \choice {self.dic2[3]} \choice {self.dic2[4]} \choice {self.dic2[5]} \end{self.tag}'


                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.spli,
                'question2':self.spli1,
                'options1':self.objec,
                'options2':self.objec1,
                }
                file_path =  os.path.join(os.getcwd(),"object.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')

                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('object.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentOb (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentOb (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentOb WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 3 Rows Selected \\\\\\\\\\\\\\\\\\\\\\\\\

            elif len(paths) == 3 and self.typ == "Objective":
                self.val1 = paths[0]
                self.val2 = paths[1]
                self.val3 = paths[2]
                self.comma = self.val1.count(',')
                self.dic = self.val1.split(',', self.comma)
                self.comma2 = self.val2.count(',')
                self.dic2 = self.val2.split(',', self.comma2)
                self.comma3 = self.val3.count(',')
                self.dic3 = self.val3.split(',', self.comma3)
                self.objec = f'gha'
                self.objec1 = f'gha'
                self.objec2 = f'gha'
                self.spli = ''
                self.spli1 = ''
                self.spli2 = ''
                self.tag = '{oneparchoices}'

                if self.comma == 2:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    else:
                        print('yes')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]}  \end{self.tag}'

                elif self.comma == 3:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]}  \end{self.tag}'


                elif self.comma == 4:
                    self.spli = self.dic[0]
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]} \choice {self.dic[4]} \end{self.tag}'


                elif self.comma == 5:
                    self.spli = self.dic[0]
                    print('ok')
                    if '\*' in self.spli:
                        self.spli = self.spli.replace('\*', '\\\\')
                    self.objec = f'\\\\\\\\\\begin{self.tag} \choice {self.dic[1]} \choice {self.dic[2]} \choice {self.dic[3]} \choice {self.dic[4]} \choice {self.dic[5]} \end{self.tag}'


#///////////////// option 2

                if self.comma2 == 2:
                    self.spli1 = self.dic2[0]
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    else:
                        print('yes')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]}  \end{self.tag}'

                elif self.comma2 == 3:
                    self.spli1 = self.dic2[0]
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]} \choice {self.dic2[3]}  \end{self.tag}'


                elif self.comma2 == 4:
                    self.spli1 = self.dic2[0]
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]} \choice {self.dic2[3]} \choice {self.dic2[4]} \end{self.tag}'


                elif self.comma2 == 5:
                    self.spli1 = self.dic2[0]
                    print('ok')
                    if '\*' in self.spli1:
                        self.spli1 = self.spli1.replace('\*', '\\\\')
                    self.objec1 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic2[1]} \choice {self.dic2[2]} \choice {self.dic2[3]} \choice {self.dic2[4]} \choice {self.dic2[5]} \end{self.tag}'


#\\\\\\\\\\\\\\\\\\ option 3

                if self.comma3 == 2:
                    self.spli2 = self.dic3[0]
                    if '\*' in self.spli2:
                        self.spli2 = self.spli2.replace('\*', '\\\\')
                    else:
                        print('yes')
                    self.objec2 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic3[1]} \choice {self.dic3[2]}  \end{self.tag}'

                elif self.comma3 == 3:
                    self.spli2 = self.dic3[0]
                    if '\*' in self.spli2:
                        self.spli2 = self.spli2.replace('\*', '\\\\')
                    self.objec2 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic3[1]} \choice {self.dic3[2]} \choice {self.dic3[3]}  \end{self.tag}'


                elif self.comma3 == 4:
                    self.spli2 = self.dic3[0]
                    if '\*' in self.spli2:
                        self.spli2 = self.spli2.replace('\*', '\\\\')
                    self.objec2 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic3[1]} \choice {self.dic3[2]} \choice {self.dic3[3]} \choice {self.dic3[4]} \end{self.tag}'


                elif self.comma3 == 5:
                    self.spli2 = self.dic3[0]
                    print('ok')
                    if '\*' in self.spli2:
                        self.spli2 = self.spli2.replace('\*', '\\\\')
                    self.objec2 = f'\\\\\\\\\\begin{self.tag} \choice {self.dic3[1]} \choice {self.dic3[2]} \choice {self.dic3[3]} \choice {self.dic3[4]} \choice {self.dic3[5]} \end{self.tag}'


                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.spli,
                'question2':self.spli1,
                'question3':self.spli2,
                'options1':self.objec,
                'options2':self.objec1,
                'options3':self.objec2,
                }
                file_path =  os.path.join(os.getcwd(),"object.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')

                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('object.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentOb (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentOb (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentOb WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

            #else:
            #    self.Dialog = QtWidgets.QDialog()
            #    self.ui = Ui_Email()
            #    self.ui.setupUi(self.Dialog)
            #    self.Dialog.setWindowTitle("Alert!")
            #    self.ui.label.setText("Select within the range (3)")
            #    self.Dialog.show()
                #print("select within the range (3)")


#\Subjective \\\\\\\\\\\\\\\\\\\\\\\Subjective \\\\\\\\\\\\\\\\\\\\\\\\\ Subjective

            if len(paths) == 1 and self.typ == "Subjective":
                self.val1 = paths[0]
                if '\*' in self.val1:
                    self.val1 = self.val1.replace('\*', '\\\\')

                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.val1,
                'question2':'',
                'question3':'',
                'question4':'',
                'question5':'',
                'question6':'',
                }
                file_path =  os.path.join(os.getcwd(),"dot.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')
                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('dot.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentSub (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentSub (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentSub WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

            elif len(paths) == 2 and self.typ == "Subjective":
                self.val1 = paths[0]
                self.val2 = paths[1]
                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.val1,
                'question2':self.val2,
                'question3':'',
                'question4':'',
                'question5':'',
                'question6':'',
                }
                file_path =  os.path.join(os.getcwd(),"dot.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')

                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('dot.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentSub (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentSub (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentSub WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

            elif len(paths) == 3 and self.typ == "Subjective":
                self.val1 = paths[0]
                self.val2 = paths[1]
                self.val3 = paths[2]
                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.val1,
                'question2':self.val2,
                'question3':self.val3,
                'question4':'',
                'question5':'',
                'question6':'',
                }
                file_path =  os.path.join(os.getcwd(),"dot.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')

                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('dot.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentSub (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentSub (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentSub WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

            elif len(paths) == 4 and self.typ == "Subjective":
                self.val1 = paths[0]
                self.val2 = paths[1]
                self.val3 = paths[2]
                self.val4 = paths[3]
                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.val1,
                'question2':self.val2,
                'question3':self.val3,
                'question4':self.val4,
                'question5':'',
                'question6':''
                }
                file_path =  os.path.join(os.getcwd(),"dot.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')

                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('dot.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentSub (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentSub (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentSub WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

            elif len(paths) == 5 and self.typ == "Subjective":
                self.val1 = paths[0]
                self.val2 = paths[1]
                self.val3 = paths[2]
                self.val4 = paths[3]
                self.val5 = paths[4]
                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.val1,
                'question2':self.val2,
                'question3':self.val3,
                'question4':self.val4,
                'question5':self.val5,
                'question6':'',
                }
                file_path =  os.path.join(os.getcwd(),"dot.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')

                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('dot.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentSub (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentSub (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentSub WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

            elif len(paths) == 6 and self.typ == "Subjective":
                self.val1 = paths[0]
                self.val2 = paths[1]
                self.val3 = paths[2]
                self.val4 = paths[3]
                self.val5 = paths[4]
                self.val6 = paths[5]
                dict_var = {'date':self.d,'time':self.t,'course code':self.cc,
                'course title':self.ct,
                'total marks':self.tm,
                'exam type':self.et,
                'semesteryear':self.Sy,
                'estimated time':self.est,
                'teachername':self.tn,
                'instruction':self.ifs,
                'question1':self.val1,
                'question2':self.val2,
                'question3':self.val3,
                'question4':self.val4,
                'question5':self.val5,
                'question6':self.val6
                }
                file_path =  os.path.join(os.getcwd(),"dot.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')

                try:
                    file = str(self.lineEdit_13.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        with open('dot.tex','r') as firstfile, open(file,'w') as secondfile:
                            for line in firstfile:
                                secondfile.write(line)
                        tex_filename = file
                        filename, ext = os.path.splitext(tex_filename)
                        pdf_filename = filename + '.pdf'
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.label0.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS AssessmentSub (PDFDOC TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO AssessmentSub (PDFDOC, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT PDFDOC FROM AssessmentSub WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
                        result = cur.fetchall()
                        conn.commit()
                        conn.close()
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("Successfully Saved")
                        self.Dialog.setWindowTitle("Confimation Message!")
                        self.Dialog.show()
                    except Exception as e:
                        self.Dialog = QtWidgets.QDialog()
                        self.ui = Ui_Email()
                        self.ui.setupUi(self.Dialog)
                        self.ui.label.setText("File with this name already exist")
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()
                except Exception as e:
                    print(e)

        except Exception as e:
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Email()
            self.ui.setupUi(self.Dialog)
            self.Dialog.setWindowTitle("Alert!")
            self.ui.label.setText(e)
            self.Dialog.show()

    def generateD(self):
        #os.system("pdflatex dot.tex")
        #path = 'dot.pdf'
        #webbrowser.open_new(path)
        try:
            save_var_latex("helo", 20)
            save_var_latex("total_score", 30)
            # TeX source filename
            tex_filename = 'dash.tex'
            filename, ext = os.path.splitext(tex_filename)
            # the corresponding PDF filename
            pdf_filename = filename + '.pdf'
            # compile TeX file
            subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
            path = 'dash.pdf'
            webbrowser.open_new(path)

            # check
            #if PDF is successfully generated
            #if not os.path.exists(pdf_filename):
            #    raise RuntimeError('PDF output not found')
                # open PDF with platform - specific command
            #    if platform.system().lower() == 'darwin':
            #        subprocess.run(['open', pdf_filename])
            #    elif platform.system().lower() == 'windows':
            #        os.startfile(pdf_filename)
            #    elif platform.system().lower() == 'linux':
            #        subprocess.run(['xdg-open', pdf_filename])
            #    else :
            #        raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))
        #    f = open("dot.tex", "r")
        #    f.ope
        except Exception as e:
            print(e)



    def getImageLabelSub(self, image):
        try:
            imagelabel = QtWidgets.QLabel(self.centralwidget)
            imagelabel.setText("")
            imagelabel.setScaledContents(True)
            pixmap = QtGui.QPixmap()
            print("error")
            pixmap.loadFromData(image, 'png')
            print("error")
            imagelabel.setPixmap(pixmap)
            print("error")
            return imagelabel
        except Exception as e:
            print(e)


    def getImageLabelOb(self, image):
        try:
            imagelabel = QtWidgets.QLabel(self.centralwidget)
            imagelabel.setText("")
            imagelabel.setScaledContents(True)
            pixmap = QtGui.QPixmap()
            print("error")
            pixmap.loadFromData(image, 'JPEG')
            print("error")
            imagelabel.setPixmap(pixmap)
            print("error")
            return imagelabel
        except Exception as e:
            print(e)




    def fullfecth(self):
        #self.no = self.lineEdit.text()
        self.sub = self.comboBox.currentText()
        self.typ = self.comboBox_2.currentText()
        self.email = self.label0.text()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        if self.sub == 'Calculus' and self.typ == 'Subjective':
            self.TitleS.setText("Calculus")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Subjective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM CalculusSub WHERE EMAIL = '{self.email}';")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                print('e')
                for row_number, row_data in enumerate(result):
                    print('e')
                    self.tableView.insertRow(row_number)
                    print('e')
                    for column_number, data in enumerate(row_data):
                        print('e')
                        item = str(data)
                        print('e')
                        if column_number == 0:
                            print('e')
                            item = self.getImageLabelSub(data)
                            print('e')
                            self.tableView.setCellWidget(row_number, column_number, item)
                            print('e')
                        else:
                            self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                conn.commit()
                conn.close()
            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == 'Calculus' and self.typ == 'Objective':
            self.TitleS.setText("Calculus")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Objective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM CalculusOb WHERE EMAIL = '{self.email}';")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableView.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = str(data)
                        if column_number == 0:
                            item = self.getImageLabelOb(data)
                            self.tableView.setCellWidget(row_number, column_number, item)
                        else:
                            self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                conn.commit()
                conn.close()
            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == "Probability" and self.typ == "Subjective":
            self.TitleS.setText("Probability")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Subjective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM ProbabilitySub WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableView.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                       item = str(data)
                       if column_number == 0:
                          item = self.getImageLabelSub(data)
                          self.tableView.setCellWidget(row_number, column_number, item)
                       else:
                          self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                conn.commit()
                conn.close()

            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == "Probability" and self.typ == "Objective":
             self.TitleS.setText("Probability")
             self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             self.TypeS.setText("Objective")
             self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             try:
                 cur.execute(f"SELECT Question, QDes FROM ProbabilityOb WHERE Email = '{self.email}';")
                 result = cur.fetchall()
                 print(result)
                 self.tableView.setRowCount(0)
                 for row_number, row_data in enumerate(result):
                      self.tableView.insertRow(row_number)
                      for column_number, data in enumerate(row_data):
                          item = str(data)
                          if column_number == 0:
                              item = self.getImageLabelOb(data)
                              self.tableView.setCellWidget(row_number, column_number, item)
                          else:
                                self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                 conn.commit()
                 conn.close()
             except Exception as e:
                 self.Dialog = QtWidgets.QDialog()
                 self.ui = Ui_Email()
                 self.ui.setupUi(self.Dialog)
                 self.ui.label.setText(str(e))
                 self.Dialog.setWindowTitle("Sqlite3 Error")
                 self.Dialog.show()

        elif self.sub == "Linear Algebra" and self.typ == "Subjective":
             self.TitleS.setText("Linear Algebra")
             self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             self.TypeS.setText("Subjective")
             self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             try:
                 cur.execute(f"SELECT Question, QDes FROM LinearSub WHERE Email = '{self.email}';")
                 result = cur.fetchall()
                 print(result)
                 self.tableView.setRowCount(0)
                 for row_number, row_data in enumerate(result):
                     self.tableView.insertRow(row_number)
                     for column_number, data in enumerate(row_data):
                         item = str(data)
                         if column_number == 0:
                             item = self.getImageLabelSub(data)
                             self.tableView.setCellWidget(row_number, column_number, item)
                         else:
                             self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                 conn.commit()
                 conn.close()
             except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == "Linear Algebra" and self.typ == "Objective":
            self.TitleS.setText("Linear Algebra")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Objective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM LinearOb WHERE Email = '{self.email}';")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableView.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = str(data)
                        if column_number == 0:
                            item = self.getImageLabelOb(data)
                            self.tableView.setCellWidget(row_number, column_number, item)
                        else:
                            self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                conn.commit()
                conn.close()
            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()


    def viewRandomly(self):
        self.no = self.lineEdit.text()
        self.sub = self.comboBox.currentText()
        self.typ = self.comboBox_2.currentText()
        self.email = self.label0.text()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        if self.sub == 'Calculus' and self.typ == 'Subjective':
            self.TitleS.setText("Calculus")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Subjective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM CalculusSub WHERE EMAIL = '{self.email}' ORDER BY Random() LIMIT '{self.no}'")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                print('e')
                for row_number, row_data in enumerate(result):
                    print('e')
                    self.tableView.insertRow(row_number)
                    print('e')
                    for column_number, data in enumerate(row_data):
                        print('e')
                        item = str(data)
                        print('e')
                        if column_number == 0:
                            print('e')
                            item = self.getImageLabelSub(data)
                            print('e')
                            self.tableView.setCellWidget(row_number, column_number, item)
                            print('e')
                        else:
                            self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                #conn.commit()
                #conn.close()
            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == 'Calculus' and self.typ == 'Objective':
            self.TitleS.setText("Calculus")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Objective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM CalculusOb WHERE EMAIL = '{self.email}' ORDER BY Random() LIMIT '{self.no}'")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableView.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = str(data)
                        if column_number == 0:
                            item = self.getImageLabelOb(data)
                            self.tableView.setCellWidget(row_number, column_number, item)
                        else:
                            self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                #conn.commit()
                #conn.close()
            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == "Probability" and self.typ == "Subjective":
            self.TitleS.setText("Probability")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Subjective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM ProbabilitySub WHERE Email = '{self.email}'ORDER BY Random() LIMIT '{self.no}'")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableView.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                       item = str(data)
                       if column_number == 0:
                          item = self.getImageLabelSub(data)
                          self.tableView.setCellWidget(row_number, column_number, item)
                       else:
                          self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                #conn.commit()
                #conn.close()

            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == "Probability" and self.typ == "Objective":
             self.TitleS.setText("Probability")
             self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             self.TypeS.setText("Objective")
             self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             try:
                 cur.execute(f"SELECT Question, QDes FROM ProbabilityOb WHERE Email = '{self.email}'ORDER BY Random() LIMIT '{self.no}'")
                 result = cur.fetchall()
                 print(result)
                 self.tableView.setRowCount(0)
                 for row_number, row_data in enumerate(result):
                      self.tableView.insertRow(row_number)
                      for column_number, data in enumerate(row_data):
                          item = str(data)
                          if column_number == 0:
                              item = self.getImageLabelOb(data)
                              self.tableView.setCellWidget(row_number, column_number, item)
                          else:
                                self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                                #conn.commit()
                                #conn.close()
             except Exception as e:
                 self.Dialog = QtWidgets.QDialog()
                 self.ui = Ui_Email()
                 self.ui.setupUi(self.Dialog)
                 self.ui.label.setText(str(e))
                 self.Dialog.setWindowTitle("Sqlite3 Error")
                 self.Dialog.show()

        elif self.sub == "Linear Algebra" and self.typ == "Subjective":
             self.TitleS.setText("Linear Algebra")
             self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             self.TypeS.setText("Subjective")
             self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
             "color: rgb(2, 114, 118);\n")
             try:
                cur.execute(f"SELECT Question, QDes FROM LinearSub WHERE Email = '{self.email}'ORDER BY Random() LIMIT '{self.no}'")
                result = cur.fetchall()
                print(result)
                self.tableView.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableView.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        item = str(data)
                        if column_number == 0:
                            item = self.getImageLabelSub(data)
                            self.tableView.setCellWidget(row_number, column_number, item)
                        else:
                            self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                    #conn.commit()
                    #conn.close()
             except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

        elif self.sub == "Linear Algebra" and self.typ == "Objective":
            self.TitleS.setText("Linear Algebra")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Objective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                 cur.execute(f"SELECT Question, QDes FROM LinearOb WHERE Email = '{self.email}'ORDER BY Random() LIMIT '{self.no}'")
                 result = cur.fetchall()
                 print(result)
                 self.tableView.setRowCount(0)
                 for row_number, row_data in enumerate(result):
                     self.tableView.insertRow(row_number)
                     for column_number, data in enumerate(row_data):
                         item = str(data)
                         if column_number == 0:
                             item = self.getImageLabelOb(data)
                             self.tableView.setCellWidget(row_number, column_number, item)
                         else:
                             self.tableView.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(item))
                 conn.commit()
                 conn.close()
            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Assessment"))
        MainWindow.setWindowIcon(QIcon("Splashlogo.png"))
        self.label.setText(_translate("MainWindow", "Select Subject"))
        self.label_2.setText(_translate("MainWindow", "Select Question Type"))
        self.label_3.setText(_translate("MainWindow", "Enter No of Questions"))
        self.label_4.setText(_translate("MainWindow", "Instructor Name"))
        self.label_5.setText(_translate("MainWindow", "Date"))
        self.label_6.setText(_translate("MainWindow", "Time"))
        self.label_8.setText(_translate("MainWindow", "Course Code"))
        self.label_9.setText(_translate("MainWindow", "Course Title"))
        self.label_10.setText(_translate("MainWindow", "Total Marks"))
        self.label_11.setText(_translate("MainWindow", "Enter Examination Type"))
        self.label_12.setText(_translate("MainWindow", "Semester Type with Year"))
        self.label_13.setText(_translate("MainWindow", "Estimated Time"))
        self.label_14.setText(_translate("MainWindow", "Instruction for Students"))
        self.label_15.setText(_translate("MainWindow", "PDF Name"))
        self.TitleS.setText(_translate("MainWindow", "Linear Algebra"))
        self.TypeS.setText(_translate("MainWindow", "Subjective"))
        self.Ques.setText(_translate("MainWindow", "Questions"))
        self.RandomSearch.setText(_translate("MainWindow", "Randomly Fetch"))
        self.GenerateDoc.setText(_translate("MainWindow", "Generate Assessment Save"))
        self.AllFetch.setText(_translate("MainWindow", "ALL Fetch"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_NewAssessment()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
