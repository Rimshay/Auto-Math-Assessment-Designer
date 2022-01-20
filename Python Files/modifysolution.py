from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import source
from solution import *
from ualreadyexist import *
import webbrowser
import os
import subprocess
#import webbrowser
#path = 'my_file.pdf'
#webbrowser.open_new(path)


class Ui_ViewA(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(90, 90, 91, 16))
        self.username.setStyleSheet("color: rgb(230, 230, 230)")
        self.username.setObjectName("user")
        self.subj = QtWidgets.QLabel(self.centralwidget)
        self.subj.setGeometry(QtCore.QRect(90, 135, 94, 18))
        self.subj.setObjectName("label")
        self.subj.setStyleSheet("font: 11pt \"Arial\";")
        self.type = QtWidgets.QLabel(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(40, 225, 181, 18))
        self.type.setObjectName("label_2")
        self.type.setStyleSheet("font: 11pt \"Arial\";")

        self.col = ['Solution', 'SDescription']

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setColumnCount(2)
        self.tableView.setHorizontalHeaderLabels(self.col)
        self.tableView.setGeometry(QtCore.QRect(410, 130, 370, 290))
        self.tableView.setObjectName("tableView")

        self.selectSub = QtWidgets.QComboBox(self.centralwidget)
        self.selectSub.setGeometry(QtCore.QRect(210, 130, 121, 22))
        self.selectSub.setObjectName("comboBox")
        self.selectSub.addItem("Linear Algebra")
        self.selectSub.addItem("Calculus")
        self.selectSub.addItem("Probability")
        self.selectSub.setStyleSheet("border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 9em;\n"
"min-height: 2em;\n")



        self.TitleS = QtWidgets.QLabel(self.centralwidget)
        self.TitleS.setGeometry(QtCore.QRect(400, 70, 125, 25))
        self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.TitleS.setObjectName("Title")
        self.Ques = QtWidgets.QLabel(self.centralwidget)
        self.Ques.setGeometry(QtCore.QRect(530, 70, 100, 25))
        self.Ques.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.Ques.setObjectName("Ques")

        self.lineEdit20 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit20.setGeometry(QtCore.QRect(250,200 , 90, 28))
        self.lineEdit20.setObjectName("lineEdit20")

        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setStyleSheet("color:rgb(255, 255, 255);")
        self.label0.setGeometry(QtCore.QRect(20, 20, 95, 18))
        self.label0.setObjectName("label0")

        self.label_30 = QLabel(self.centralwidget)
        self.label_30.setText("Document Name :")
        self.label_30.setStyleSheet("font: 11pt \"Arial\";")
        self.label_30.setGeometry(QtCore.QRect(100, 200, 120, 31))
        self.label_30.setObjectName("label_30")

        self.ViewData = QtWidgets.QPushButton(self.centralwidget)
        self.ViewData.setGeometry(QtCore.QRect(90, 270, 80, 35))
        self.ViewData.setObjectName("viewdata")
        self.ViewData.setStyleSheet("QPushButton#viewdata{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#viewdata:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#viewdata:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")
        self.ViewData.clicked.connect(self.browseData)

        self.ViewDelete = QtWidgets.QPushButton(self.centralwidget)
        self.ViewDelete.setGeometry(QtCore.QRect(220, 270, 80, 35))
        self.ViewDelete.setObjectName("delete")
        self.ViewDelete.setStyleSheet("QPushButton#delete{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#delete:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#delete:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")
        self.ViewDelete.clicked.connect(self.deleteBrowse)


        self.solOpenPDF = QtWidgets.QPushButton(self.centralwidget)
        self.solOpenPDF.setGeometry(QtCore.QRect(140, 325, 100, 35))
        self.solOpenPDF.setObjectName("PDF")
        self.solOpenPDF.setStyleSheet("QPushButton#PDF{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#PDF:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#PDF:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")
        self.solOpenPDF.clicked.connect(self.modify)

        self.generatepdf = QtWidgets.QPushButton(self.centralwidget)
        self.generatepdf.setGeometry(QtCore.QRect(130, 370, 130, 35))
        self.generatepdf.setObjectName("Generate PDF")
        self.generatepdf.setStyleSheet("QPushButton#viewdata{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#viewdata:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#viewdata:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")
        self.generatepdf.clicked.connect(self.save_var_latex)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def modify(self):
        self.tt = self.username.text()
        print('s')
        self.sub = self.selectSub.currentText()
        print('s')
        print('s')
        window = Sol()
        print('s')
        window.ee.setText(self.tt)
        window.setWindowTitle("Modify a Question")
        #window.show()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        if self.sub == "Linear Algebra":
            self.res = cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")

            for row in enumerate (self.res):

                if row[0] == self.tableView.currentRow():

                    self.qq = row[1]
                    self.quest = self.qq[1]
                    print(self.quest)

                    try:
                        window.editor.setText(str(self.quest))
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    except Exception as e:
                        print(e)



        elif self.sub == "Calculus":
            self.res = cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")

            for row in enumerate (self.res):

                if row[0] == self.tableView.currentRow():

                    self.qq = row[1]
                    self.quest = self.qq[1]

                    try:
                        window.editor.setText(str(self.quest))
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    except Exception as e:
                        print(e)



        elif self.sub == "Probability" :
            self.res = cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")

            for row in enumerate (self.res):

                if row[0] == self.tableView.currentRow():

                    self.qq = row[1]
                    self.quest = self.qq[1]

                    try:
                        window.editor.setText(str(self.quest))
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    except Exception as e:
                        print(e)


        conn.commit()
        conn.close()


    def save_var_latex(self):
        try:

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


#\Subjective \\\\\\\\\\\\\\\\\\\\\\\Subjective \\\\\\\\\\\\\\\\\\\\\\\\\ Subjective

            if len(paths) == 1:
                self.val1 = paths[0]
                if '\*' in self.val1:
                    self.val1 = self.val1.replace('\*', '\\\\')

                dict_var = {'solution':self.val1}

                file_path =  os.path.join(os.getcwd(),"sol.dat")
                with open(file_path,"w") as f:
                    for key in dict_var.keys():
                        print(key)
                        print(dict_var[key])
                        print('yes')
                        f.write(f"{key},{dict_var[key]}\n")
                        print('hogya')
                try:
                    file = str(self.lineEdit20.text())
                    file = file + '.tex'
                    try:
                        finalfile = open(file, 'x')
                        print('hoa')
                        with open('solution.tex','r') as firstfile, open(file,'w') as secondfile:
                            print('hoa')
                            for line in firstfile:
                                print('hoa')
                                secondfile.write(line)
                                print('hoa')
                        tex_filename = file
                        print('yes')
                        filename, ext = os.path.splitext(tex_filename)
                        print('hoa')
                        pdf_filename = filename + '.pdf'
                        print('hoa')
                        subprocess.run(['pdflatex', '-interaction=nonstopmode', tex_filename])
                        path = pdf_filename
                        webbrowser.open_new(path)
                        conn = sqlite3.connect("Database.db")
                        cur = conn.cursor()
                        self.ema = str(self.username.text())

                        cur.execute("CREATE TABLE IF NOT EXISTS Solutionpdf (Solution TEXT NOT NULL, Subject TEXT NOT NULL, Email TEXT NOT NULL, FOREIGN KEY (Email) REFERENCES user (Email))")

                        cur.execute("INSERT INTO Solutionpdf (Solution, Subject, Email) VALUES (?,?,?)", (path, self.sub, self.ema))

                        cur.execute(f"SELECT Solution FROM Solutionpdf WHERE Email = '{self.ema}' AND Subject = '{self.sub}';")
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
                        #self.ui.label.setText("File with this name already exist")
                        self.ui.label.setText(e)
                        self.Dialog.setWindowTitle("Alert!")
                        self.Dialog.show()

                except Exception as e:
                    print(e)

            else:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.Dialog.setWindowTitle("Alert!")
                self.ui.label.setText('Only one Solution can print at a time')
                self.Dialog.show()




        except Exception as e:
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Email()
            self.ui.setupUi(self.Dialog)
            self.Dialog.setWindowTitle("Alert!")
            self.ui.label.setText(e)
            self.Dialog.show()





    def deleteBrowse(self):
        self.tt = self.username.text()
        self.sub = self.selectSub.currentText()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        print('h')
        if self.sub == "Linear Algebra" :
            self.res = cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")
            print('h')
            for row in enumerate (self.res):
                print('h')
                if row[0] == self.tableView.currentRow():
                    print('h')
                    self.qq = row[1]
                    print('h')
                    self.quest = self.qq[0]
                    print('h')
                    self.desc = self.qq[1]
                    #print('h')
                    #mail = self.qq[1]
                    print(self.quest)
                    #path = 'dot.pdf'
                    #webbrowser.open_new(path)
                    cur.execute("DELETE FROM Solution WHERE Solution = ? AND SDes = ? AND Subject = ? AND Email = ?", (self.quest,self.desc, self.sub, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())
        #conn.commit()
        #conn.close()


        elif self.sub == "Calculus" :
            self.res = cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")
            print('h')
            for row in enumerate (self.res):
                print('h')
                if row[0] == self.tableView.currentRow():
                    print('h')
                    self.qq = row[1]
                    self.quest = self.qq[0]
                    self.desc = self.qq[1]
                    #mail = self.qq[1]
                    print(self.quest)
                    cur.execute("DELETE FROM Solution WHERE Solution = ? AND SDes = ? AND Subject = ? AND Email = ?", (self.quest,self.desc,self.sub, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())
        #conn.commit()
        #conn.close()


        elif self.sub == "Probability":
            self.res = cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")
            print('h')
            for row in enumerate (self.res):
                print('h')
                if row[0] == self.tableView.currentRow():
                    print('h')
                    self.qq = row[1]
                    self.quest = self.qq[0]
                    self.desc = self.qq[1]
                    #mail = self.qq[1]
                    print(self.quest)
                    cur.execute("DELETE FROM Solution WHERE Solution = ? AND SDes = ? AND Subject = ? AND Email = ?", (self.quest,self.desc, self.sub, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())

        else:
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Email()
            self.ui.setupUi(self.Dialog)
            self.ui.label.setText("Select the rows and subject")
            self.Dialog.setWindowTitle("Alert!")
            self.Dialog.show()

        conn.commit()
        conn.close()





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




    def browseData(self):
        self.sub = self.selectSub.currentText()
        self.tt = self.username.text()
        print("hhh")
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        if self.sub == "Linear Algebra":
            print("hhh")
            self.TitleS.setText("Linear Algebra")
            print("hhh")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                print("hhh")
                cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")
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

            except Exception as e:
                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Email()
                self.ui.setupUi(self.Dialog)
                self.ui.label.setText(str(e))
                self.Dialog.setWindowTitle("Sqlite3 Error")
                self.Dialog.show()

            conn.commit()
            conn.close()


        elif self.sub == "Calculus":
            self.TitleS.setText("Calculus")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")
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



        elif self.sub == "Probability" :
            self.TitleS.setText("Probability")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Solution, SDes FROM Solution WHERE Email = '{self.tt}' AND Subject = '{self.sub}';")
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







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modify Solution"))
        MainWindow.setWindowIcon(QIcon("Splashlogo.png"))
        self.subj.setText(_translate("MainWindow", "Select Subject"))
        self.TitleS.setText(_translate("MainWindow", "Linear Algebra"))
        self.Ques.setText(_translate("MainWindow", "Solution"))
        self.ViewData.setText(_translate("MainWindow", "View"))
        self.ViewDelete.setText(_translate("MainWindow", "Delete"))
        self.solOpenPDF.setText(_translate("MainWindow", "Modify"))
        self.generatepdf.setText(_translate("MainWindow", "Generate PDF and Save"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ViewA()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
