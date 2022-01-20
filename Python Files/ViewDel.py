from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
#from Modify import *
import source
from question import *
from ualreadyexist import *


class Ui_View(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 516)
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

        self.col = ['Questions', 'QDescription']

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setColumnCount(2)
        self.tableView.setHorizontalHeaderLabels(self.col)
        self.tableView.setGeometry(QtCore.QRect(410, 130, 411, 341))
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


        self.selectType = QtWidgets.QComboBox(self.centralwidget)
        self.selectType.setGeometry(QtCore.QRect(210, 220, 151, 22))
        self.selectType.setObjectName("comboBox_2")
        self.selectType.addItem("Subjective")
        self.selectType.addItem("Objective")
        self.selectType.setStyleSheet("border: 1px solid gray;\n"
"border-radius: 3px;\n"
"padding: 1px 18px 1px 3px;\n"
"min-width: 9em;\n"
"min-height: 2em;\n")


        self.TitleS = QtWidgets.QLabel(self.centralwidget)
        self.TitleS.setGeometry(QtCore.QRect(430, 70, 125, 25))
        self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.TitleS.setObjectName("Title")
        self.TypeS = QtWidgets.QLabel(self.centralwidget)
        self.TypeS.setGeometry(QtCore.QRect(560, 70, 100, 25))
        self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.TypeS.setObjectName("Type")
        self.Ques = QtWidgets.QLabel(self.centralwidget)
        self.Ques.setGeometry(QtCore.QRect(655, 70, 90, 25))
        self.Ques.setStyleSheet("font: 14pt \"Arial\";\n"
        "color: rgb(2, 114, 118);\n")
        self.Ques.setObjectName("Ques")


        self.ViewData = QtWidgets.QPushButton(self.centralwidget)
        self.ViewData.setGeometry(QtCore.QRect(90, 360, 80, 35))
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
        self.ViewDelete.setGeometry(QtCore.QRect(220, 360, 80, 35))
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


        self.Modify = QtWidgets.QPushButton(self.centralwidget)
        self.Modify.setGeometry(QtCore.QRect(160, 410, 80, 35))
        self.Modify.setObjectName("modify")
        self.Modify.setStyleSheet("QPushButton#modify{\n"
"  background-color: rgb(2, 114, 118);\n"
"  font: 10pt \"Arial\";\n"
"  color: rgba(255, 255, 255, 200);\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton#modify:pressed{\n"
"  padding-left:5px;\n"
"  padding-top:5px;\n"
"  background-color:rgba(255, 107, 107, 255);\n"
"  background-position:calc(100% . 10px)center;\n"
"}\n"
"\n"
"QPushButton#modify:hover{\n"
"  background-color: rgba(255, 255, 255, 255);\n"
"  color:rgb(2, 114, 118);\n"
"  border:2px solid;\n"
"  border-color:rgb(2, 114, 118);\n"
"}\n"
"\n"
"")
        self.Modify.clicked.connect(self.modifyques)


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def modifyques(self):
        self.tt = self.username.text()
        print('s')
        self.sub = self.selectSub.currentText()
        print('s')
        self.typ = self.selectType.currentText()
        print('s')
        window = MainS()
        print('s')
        window.ee.setText(self.tt)
        window.setWindowTitle("Modify a Question")
        #window.show()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        if self.sub == "Linear Algebra" and self.typ == "Subjective":
            self.res = cur.execute(f"SELECT Question, QDes FROM LinearSub WHERE Email = '{self.tt}';")

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

        elif self.sub == "Linear Algebra" and self.typ == "Objective":
            self.res = cur.execute(f"SELECT Question, QDes FROM LinearOb WHERE Email = '{self.tt}';")
            print(self.res)
            for row in enumerate (self.res):
                print('h')
                if row[0] == self.tableView.currentRow():
                    print('h')
                    self.qq = row[1]
                    self.quest = self.qq[1]
                    print(self.quest)
                    self.comma = self.quest.count(',')
                    print(self.comma)
                    self.dic = self.quest.split(',', self.comma)
                    print(self.dic)
                    if self.comma == 2:
                        window.editor.setText(self.dic[0])
                        window.optionedit6.setText(self.dic[1])
                        window.optionedit7.setText(self.dic[2])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 3:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 4:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.optionedit4.setText(self.dic[4])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 5:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.optionedit4.setText(self.dic[4])
                        window.optionedit5.setText(self.dic[5])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()


        elif self.sub == "Calculus" and self.typ == "Subjective":
            self.res = cur.execute(f"SELECT Question, QDes FROM CalculusSub WHERE Email = '{self.tt}';")

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

        elif self.sub == "Calculus" and self.typ == "Objective":
            self.res = cur.execute(f"SELECT Question, QDes FROM CalculusOb WHERE Email = '{self.tt}';")
            print(self.res)
            for row in enumerate (self.res):
                print('h')
                if row[0] == self.tableView.currentRow():
                    print('h')
                    self.qq = row[1]
                    self.quest = self.qq[1]
                    print(self.quest)
                    self.comma = self.quest.count(',')
                    print(self.comma)
                    self.dic = self.quest.split(',', self.comma)
                    print(self.dic)
                    if self.comma == 2:
                        window.editor.setText(self.dic[0])
                        window.optionedit6.setText(self.dic[1])
                        window.optionedit7.setText(self.dic[2])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 3:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 4:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.optionedit4.setText(self.dic[4])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 5:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.optionedit4.setText(self.dic[4])
                        window.optionedit5.setText(self.dic[5])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

        elif self.sub == "Probability" and self.typ == "Subjective":
            self.res = cur.execute(f"SELECT Question, QDes FROM ProbabilitySub WHERE Email = '{self.tt}';")

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

        elif self.sub == "Probability" and self.typ == "Objective":
            self.res = cur.execute(f"SELECT Question, QDes FROM ProbabilityOb WHERE Email = '{self.tt}';")
            print(self.res)
            for row in enumerate (self.res):
                print('h')
                if row[0] == self.tableView.currentRow():
                    print('h')
                    self.qq = row[1]
                    self.quest = self.qq[1]
                    print(self.quest)
                    self.comma = self.quest.count(',')
                    print(self.comma)
                    self.dic = self.quest.split(',', self.comma)
                    print(self.dic)
                    if self.comma == 2:
                        window.editor.setText(self.dic[0])
                        window.optionedit6.setText(self.dic[1])
                        window.optionedit7.setText(self.dic[2])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 3:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 4:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.optionedit4.setText(self.dic[4])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

                    elif self.comma == 5:
                        window.editor.setText(self.dic[0])
                        window.optionedit1.setText(self.dic[1])
                        window.optionedit2.setText(self.dic[2])
                        window.optionedit3.setText(self.dic[3])
                        window.optionedit4.setText(self.dic[4])
                        window.optionedit5.setText(self.dic[5])
                        window.save.hide()
                        window.update.show()
                        window.up.setText(str(self.quest))
                        window.show()

        conn.commit()
        conn.close()

    def deleteBrowse(self):
        self.tt = self.username.text()
        self.sub = self.selectSub.currentText()
        self.typ = self.selectType.currentText()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        print('h')
        if self.sub == "Linear Algebra" and self.typ == "Subjective":
            self.res = cur.execute(f"SELECT Question, QDes FROM LinearSub WHERE Email = '{self.tt}';")
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
                    cur.execute("DELETE FROM LinearSub WHERE Question = ? AND QDes = ? AND Email = ?", (self.quest, self.desc, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())
        #conn.commit()
        #conn.close()

        elif self.sub == "Linear Algebra" and self.typ == "Objective":
            self.res = cur.execute(f"SELECT Question, QDes FROM LinearOb WHERE Email = '{self.tt}';")
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
                    cur.execute("DELETE FROM LinearOb WHERE Question = ? AND QDes = ? AND Email = ?", (self.quest, self.desc, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())
        #conn.commit()
        #conn.close()

        elif self.sub == "Calculus" and self.typ == "Subjective":
            self.res = cur.execute(f"SELECT Question, QDes FROM CalculusSub WHERE Email = '{self.tt}';")
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
                    cur.execute("DELETE FROM CalculusSub WHERE Question = ? AND QDes = ? AND Email = ?", (self.quest, self.desc, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())
        #conn.commit()
        #conn.close()

        elif self.sub == "Calculus" and self.typ == "Objective":
            self.res = cur.execute(f"SELECT Question, QDes FROM CalculusOb WHERE Email = '{self.tt}';")
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
                    cur.execute("DELETE FROM CalculusOb WHERE Question = ? AND QDes = ? AND Email = ?", (self.quest, self.desc, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())

        elif self.sub == "Probability" and self.typ == "Subjective":
            self.res = cur.execute(f"SELECT Question, QDes FROM ProbabilitySub WHERE Email = '{self.tt}';")
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
                    cur.execute("DELETE FROM ProbabilitySub WHERE Question = ? AND QDes = ? AND Email = ?", (self.quest, self.desc, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())

        elif self.sub == "Probability" and self.typ == "Objective":
            self.res = cur.execute(f"SELECT Question, QDes FROM ProbabilityOb WHERE Email = '{self.tt}';")
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
                    cur.execute("DELETE FROM ProbabilityOb WHERE Question = ? AND QDes = ? AND Email = ?", (self.quest, self.desc, self.tt))
                    self.tableView.removeRow(self.tableView.currentRow())

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
        self.typ = self.selectType.currentText()
        self.tt = self.username.text()
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()

        if self.sub == "Linear Algebra" and self.typ == "Subjective":
            self.TitleS.setText("Linear Algebra")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Subjective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM LinearSub WHERE Email = '{self.tt}';")
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

        elif self.sub == "Linear Algebra" and self.typ == "Objective":
            self.TitleS.setText("Linear Algebra")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Objective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM LinearOb WHERE Email = '{self.tt}';")
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


        elif self.sub == "Calculus" and self.typ == "Subjective":
            self.TitleS.setText("Calculus")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Subjective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM CalculusSub WHERE Email = '{self.tt}';")
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

        elif self.sub == "Calculus" and self.typ == "Objective":
            self.TitleS.setText("Calculus")
            self.TitleS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            self.TypeS.setText("Objective")
            self.TypeS.setStyleSheet("font: 14pt \"Arial\";\n"
            "color: rgb(2, 114, 118);\n")
            try:
                cur.execute(f"SELECT Question, QDes FROM CalculusOb WHERE Email = '{self.tt}';")
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
                cur.execute(f"SELECT Question, QDes FROM ProbabilitySub WHERE Email = '{self.tt}';")
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
                cur.execute(f"SELECT Question, QDes FROM ProbabilityOb WHERE Email = '{self.tt}';")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "View, Delete, and Update Questions"))
        MainWindow.setWindowIcon(QIcon("Splashlogo.png"))
        self.subj.setText(_translate("MainWindow", "Select Subject"))
        self.type.setText(_translate("MainWindow", "Select Questions Type"))
        self.TitleS.setText(_translate("MainWindow", "Linear Algebra"))
        self.TypeS.setText(_translate("MainWindow", "Subjective"))
        self.Ques.setText(_translate("MainWindow", "Questions"))
        self.ViewData.setText(_translate("MainWindow", "View"))
        self.ViewDelete.setText(_translate("MainWindow", "Delete"))
        self.Modify.setText(_translate("MainWindow", "Modify"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_View()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
