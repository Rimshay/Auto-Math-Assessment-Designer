from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import *
from question import *
from ViewDel import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from assessment import *
from ViewDelassessment import *
from solutionviewdel import *
from solution import *
from modifysolution import *
import sys
import source

class QLabelClickable(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)
        #QtWidgets.QLabel.__init__(self, parent)

    def mousePressEvent(self, event):
        self.ultimo = "Click"

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

    def mouseReleaseEvent(self, event):
        if self.ultimo == "Click":
            QTimer.singleShot(QApplication.instance().doubleClickInterval(), self.performSingleClickAction)
        else:
             #Realizar acción de doble clic.
            self.clicked.emit(self.ultimo)

    def mouseDoubleClickEvent(self, event):
        self.ultimo = "Double Click"


    def performSingleClickAction(self):
        if self.ultimo == "Click":
            self.clicked.emit(self.ultimo)


########################################## Main Class

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #MainWindow.setWindowFlags(Qt.WindowTitleHint | Qt.WindowMaximizeButtonHint | Qt.WindowSystemMenuHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(300, 550))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.971591, stop:0 rgba(14, 149, 133, 255), stop:1 rgba(124, 129, 135, 255));\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")

        self.labelspace = QtWidgets.QPushButton(self.frame)
        self.labelspace.setMaximumSize(QtCore.QSize(16777215, 60))
        self.labelspace.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(240, 240, 240);\n"
"font: 17pt \"Arial\";")
        #self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelspace.setObjectName("labelspace")
        self.verticalLayout.addWidget(self.labelspace)

        self.mail = QtWidgets.QPushButton(self.frame)
        self.mail.setMaximumSize(QtCore.QSize(16777215, 0))
        self.mail.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(124, 129, 135);\n"
"font: 17pt \"Arial\";")
        self.mail.setObjectName("label")
        self.verticalLayout.addWidget(self.mail)

        self.name = QtWidgets.QPushButton(self.frame)
        self.name.setMaximumSize(QtCore.QSize(16777215, 40))
        self.name.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 20pt \"Arial\";")
        self.name.setObjectName("label")
        self.verticalLayout.addWidget(self.name)


        self.label = QtWidgets.QPushButton(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(240, 240, 240);\n"
"font: 17pt \"Arial\";")
        #self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        #self.label.clicked.connect(self.changestate)
        self.label.clicked.connect(self.qpool)

        self.label1 = QtWidgets.QPushButton(self.frame)
        #self.label1.setGeometry(QtCore.QRect(10, 10, 10, 20))
        self.label1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(240, 240, 240);\n"
"font: 17pt \"Arial\";")
        #self.label1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label1.setObjectName("label1")
        self.verticalLayout.addWidget(self.label1)
        self.label1.clicked.connect(self.AD)

        self.label_2 = QtWidgets.QPushButton(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setStyleSheet("color: rgb(240, 240, 240);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 17pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.clicked.connect(self.solut)


        self.label_3 = QtWidgets.QPushButton(self.frame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setStyleSheet("color: rgb(240, 240, 240);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 17pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_3.clicked.connect(self.ab)

        self.label_5 = QtWidgets.QPushButton(self.frame)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_5.setStyleSheet("color: rgb(240, 240, 240);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 17pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_5.clicked.connect(self.help)


        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 10pt \"Arial\";")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addWidget(self.frame)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(600, 550)) #16777215
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.Minimize = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Minimize.sizePolicy().hasHeightForWidth())
        self.Minimize.setSizePolicy(sizePolicy)
        self.Minimize.setMaximumSize(QtCore.QSize(20, 30))
        self.Minimize.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Minimize.setStyleSheet("image: url(:/newPrefix/minimize.png);\n"
        "background: transparent;\n")
        self.Minimize.setText("")
        self.Minimize.clicked.connect(self.minimizewindow)
        self.Minimize.setObjectName("Minimize")
        self.horizontalLayout_2.addWidget(self.Minimize)
        self.Restore = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Restore.sizePolicy().hasHeightForWidth())
        self.Restore.setSizePolicy(sizePolicy)
        self.Restore.setMaximumSize(QtCore.QSize(30, 25))
        self.Restore.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Restore.setStyleSheet("image: url(:/newPrefix/restore.png);\n"
        "background: transparent;\n")
        self.Restore.setText("")
        self.Restore.clicked.connect(self.maxnormal)
        self.Restore.setObjectName("Restore")
        self.horizontalLayout_2.addWidget(self.Restore)
        self.close = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setMaximumSize(QtCore.QSize(20, 20))
        self.close.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.close.setStyleSheet("image: url(:/newPrefix/cross2.png);\n"
        "background: transparent;\n")
        self.close.setText("")
        self.close.clicked.connect(MainWindow.close)
        self.close.setObjectName("close")
        self.horizontalLayout_2.addWidget(self.close)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_6 = QtWidgets.QFrame(self.widget)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        #self.SearchBar = QtWidgets.QLineEdit(self.frame_6)
        #self.SearchBar.setGeometry(QtCore.QRect(50, 10, 500, 40))
        #self.SearchBar.setMaximumSize(QtCore.QSize(500, 40))
        #self.SearchBar.setStyleSheet("border-radius: 15px;\n"
#"border-color: rgb(60, 60, 60);\n"
#"background-color: rgb(230, 230, 230);")
#        self.SearchBar.setCursorPosition(0)
#        self.SearchBar.setClearButtonEnabled(True)
#        self.SearchBar.setObjectName("SearchBar")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setGeometry(QtCore.QRect(10, 10, 20, 20))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_2.addWidget(self.frame_6)

        ######################### Question pool

        self.frame_3 = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")

        self.add = QtWidgets.QPushButton(self.frame_3)

        self.add.setMaximumSize(QtCore.QSize(130, 130))
        self.add.setStyleSheet("image: url(:/newPrefix/add.png);\n"
        "border: 1px solid;\n"
        "border-color: rgb(170, 170, 170);\n"
        "text-align:center;\n"
        "padding: 40px;\n"

        "")
        self.add.setText("")
        self.add.setObjectName("add")
        self.add.clicked.connect(self.openaquestion)

        self.gridLayout.addWidget(self.add, 0, 0, 1, 1)

        self.view = QtWidgets.QPushButton(self.frame_3)
        self.view.setMaximumSize(QtCore.QSize(130, 130))
        self.view.setStyleSheet("image: url(:/newPrefix/view.png);\n"
        "border: 1px solid;\n"
        "border-color: rgb(170, 170, 170);\n"
        "text-align:center;\n"
        "padding: 40px;\n"
        "")

        self.view.setText("")
        self.view.setObjectName("add")
        self.view.clicked.connect(self.openView)
        self.gridLayout.addWidget(self.view, 0, 1, 1, 1)


        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setMaximumSize(QtCore.QSize(150, 30))
        self.label_4.setStyleSheet("font: 11pt \"Arial\";\n"
"text-align:center;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setMaximumSize(QtCore.QSize(150, 30))
        self.label_6.setStyleSheet("font: 11pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_3)


        ######################### Assessment Designer

        self.assess = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assess.sizePolicy().hasHeightForWidth())
        self.assess.setSizePolicy(sizePolicy)
        self.assess.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.assess.setFrameShadow(QtWidgets.QFrame.Raised)
        self.assess.setObjectName("assess")
        self.gridLayout = QtWidgets.QGridLayout(self.assess)
        self.gridLayout.setObjectName("gridLayout")

        self.newas = QtWidgets.QPushButton(self.assess)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newas.sizePolicy().hasHeightForWidth())
        self.newas.setSizePolicy(sizePolicy)
        self.newas.setMaximumSize(QtCore.QSize(130, 130))
        self.newas.setStyleSheet("image: url(:/newPrefix/newassess.png);\n"
        "border: 1px solid;\n"
        "border-color: rgb(170, 170, 170);\n"
        "text-align:center;\n"
        "padding: 40px;\n"
        "")

        self.newas.setText("")
        self.newas.setObjectName("add")
        self.newas.clicked.connect(self.openassessment)
        self.gridLayout.addWidget(self.newas, 1, 0, 5, 1)

        self.msol = QtWidgets.QPushButton(self.assess)
        self.msol.setMaximumSize(QtCore.QSize(130, 130))
        self.msol.setStyleSheet("image: url(:/newPrefix/view.png);\n"
        "border: 1px solid;\n"
        "border-color: rgb(170, 170, 170);\n"
        "text-align:center;\n"
        "padding: 40px;\n"
        "")
        self.msol.setObjectName("add")
        self.msol.clicked.connect(self.openViewAssess)
        self.gridLayout.addWidget(self.msol, 1, 2, 5, 1)

        self.newassess = QtWidgets.QLabel(self.assess)
        self.newassess.setMaximumSize(QtCore.QSize(150, 30))
        self.newassess.setStyleSheet("font: 11pt \"Arial\";\n"
"text-align:center;")
        self.newassess.setObjectName("label_4")
        self.gridLayout.addWidget(self.newassess, 6, 0, 1, 1)

        self.Modassess = QtWidgets.QLabel(self.assess)
        self.Modassess.setMaximumSize(QtCore.QSize(170, 40))
        self.Modassess.setStyleSheet("font: 11pt \"Arial\";")
        self.Modassess.setObjectName("label_6")
        self.gridLayout.addWidget(self.Modassess, 6, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.assess)

        ########################Solution

        self.soluti = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soluti.sizePolicy().hasHeightForWidth())
        self.soluti.setSizePolicy(sizePolicy)
        self.soluti.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.soluti.setFrameShadow(QtWidgets.QFrame.Raised)
        self.soluti.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.soluti)
        self.gridLayout.setObjectName("gridLayout")
        self.addsol = QtWidgets.QPushButton(self.soluti)
        self.addsol.setMaximumSize(QtCore.QSize(130, 130))
        self.addsol.setStyleSheet("font:36pt \"Adam\";\n"
"color: rgb(22, 148, 133);\n"
"border: 1px solid;\n"
"border-color: rgb(170, 170, 170);\n"
"text-align:center;\n"
"")
        self.addsol.setText("+")
        self.addsol.setObjectName("add")
        self.addsol.clicked.connect(self.opensolution)
        self.gridLayout.addWidget(self.addsol, 0, 0, 1, 1)

        self.viewsol = QtWidgets.QPushButton(self.soluti)
        self.viewsol.setMaximumSize(QtCore.QSize(130, 130))
        self.viewsol.setStyleSheet("image: url(:/newPrefix/modify.png);\n"
        "border: 1px solid;\n"
        "border-color: rgb(170, 170, 170);\n"
        "text-align:center;\n"
        "padding: 40px;\n"
        "")

        self.viewsol.setText("")
        self.viewsol.setObjectName("new")
        self.viewsol.clicked.connect(self.openViewSol)

        self.gridLayout.addWidget(self.viewsol, 0, 1, 1, 1)

        self.viewpdf = QtWidgets.QPushButton(self.soluti)
        self.viewpdf.setMaximumSize(QtCore.QSize(130, 130))
        self.viewpdf.setStyleSheet("image: url(:/newPrefix/view.png);\n"
        "border: 1px solid;\n"
        "border-color: rgb(170, 170, 170);\n"
        "text-align:center;\n"
        "padding: 40px;\n"
        "")

        self.viewpdf.setText("")
        self.viewpdf.setObjectName("new")
        self.viewpdf.clicked.connect(self.openpdfSol)

        self.gridLayout.addWidget(self.viewpdf, 0, 2, 1, 1)

        self.opsol = QtWidgets.QLabel(self.soluti)
        self.opsol.setMaximumSize(QtCore.QSize(150, 30))
        self.opsol.setStyleSheet("font: 11pt \"Arial\";\n"
"text-align:center;")
        self.opsol.setObjectName("label_4")
        self.gridLayout.addWidget(self.opsol, 1, 0, 1, 1)

        self.MSol = QtWidgets.QLabel(self.soluti)
        self.MSol.setMaximumSize(QtCore.QSize(150, 30))
        self.MSol.setStyleSheet("font: 11pt \"Arial\";")
        self.MSol.setObjectName("label_6")
        self.gridLayout.addWidget(self.MSol, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.soluti)

        self.VDSol = QtWidgets.QLabel(self.soluti)
        self.VDSol.setMaximumSize(QtCore.QSize(150, 30))
        self.VDSol.setStyleSheet("font: 11pt \"Arial\";")
        self.VDSol.setObjectName("label_6")
        self.gridLayout.addWidget(self.VDSol, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.soluti)



        ####################### About

        self.about = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about.sizePolicy().hasHeightForWidth())
        self.about.setSizePolicy(sizePolicy)
        self.about.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.about.setFrameShadow(QtWidgets.QFrame.Raised)
        self.about.setObjectName("assess")
        self.horizontalLayouts = QtWidgets.QVBoxLayout(self.about)
        self.horizontalLayouts.setObjectName("gridLayout")
        self.Des = QtWidgets.QLabel(self.about)
        self.Des.setWordWrap(True)
        self.Des.setMaximumSize(QtCore.QSize(600, 800))
        self.Des.setStyleSheet("font: 11pt \"Arial\";")
        self.Des.setObjectName("label_9")
        self.horizontalLayouts.addWidget(self.Des)
        self.verticalLayout_2.addWidget(self.about)

################################ help

        self.help = QtWidgets.QFrame(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.help.setFrameShadow(QtWidgets.QFrame.Raised)
        self.help.setObjectName("assess")
        self.horizontalLayouts = QtWidgets.QVBoxLayout(self.help)
        self.horizontalLayouts.setObjectName("gridLayout")
        self.ques = QtWidgets.QLabel(self.help)
        self.ques.setWordWrap(True)
        self.ques.setMaximumSize(QtCore.QSize(600, 800))
        self.ques.setStyleSheet("font: 11pt \"Arial\";")
        self.ques.setObjectName("label_9")
        self.horizontalLayouts.addWidget(self.ques)
        self.verticalLayout_2.addWidget(self.help)

        self.frame_4 = QtWidgets.QFrame(self.widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        #QtCore.QRect(0, 0, 640, 700)
        MainWindow.setGeometry(250, 50, 900, 600)
        #self.center()
        self.assess.hide()
        self.about.hide()
        self.help.hide()
        self.soluti.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def solut(self):
        self.assess.hide()
        self.about.hide()
        self.help.hide()
        self.frame_3.hide()
        self.soluti.show()

    def qpool(self):
        self.assess.hide()
        self.about.hide()
        self.help.hide()
        self.soluti.hide()
        self.frame_3.show()

    def AD(self):
        self.frame_3.hide()
        self.about.hide()
        self.help.hide()
        self.soluti.hide()
        self.assess.show()

    def ab(self):
        self.frame_3.hide()
        self.assess.hide()
        self.help.hide()
        self.soluti.hide()
        self.about.show()

    def help(self):
        self.frame_3.hide()
        self.assess.hide()
        self.about.hide()
        self.soluti.hide()
        self.help.show()




    #def changestate(self):
    #    self.label_4.setHidden(True)

    def openViewSol(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ViewA()
        self.ui.setupUi(self.MainWindow)
        self.ui.username.setText(self.mail.text())
        self.MainWindow.show()


    def openpdfSol(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ViewD()
        self.ui.setupUi(self.MainWindow)
        self.ui.username.setText(self.mail.text())
        self.MainWindow.show()

    def openaquestion(self):
        #self.window = QtWidgets.QMainWindow()
        window = MainS()
        window.ee.setText(self.mail.text())
        window.show()
        #self.ui.setupUi(self.window)
        #self.window.show()

    def opensolution(self):
        #self.window = QtWidgets.QMainWindow()
        window = Sol()
        window.ee.setText(self.mail.text())
        window.show()
        #self.ui.setupUi(self.window)
        #self.window.show()

    def openassessment(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_NewAssessment()
        self.ui.setupUi(self.MainWindow)
        self.ui.label0.setText(self.mail.text())
        self.ui.label1.setText(self.name.text())
        self.MainWindow.show()

    def openView(self):
         self.Window = QtWidgets.QMainWindow()
         self.ui = Ui_View()
         self.ui.setupUi(self.Window)
         self.ui.username.setText(self.mail.text())
         self.Window.show()

    def openViewAssess(self):
         self.Window = QtWidgets.QMainWindow()
         self.ui = Ui_ViewAssess()
         self.ui.setupUi(self.Window)
         self.ui.username.setText(self.mail.text())
         self.Window.show()

    def minimizewindow(self):
        MainWindow.showMinimized()

    def maxnormal(self):
        if MainWindow.isMaximized():
            MainWindow.showNormal()
            self.Restore.setMaximumSize(QtCore.QSize(30, 25))
            self.Restore.setStyleSheet("image: url(:/newPrefix/restore.png);\n"
            "background: transparent;\n")
        else:
            MainWindow.showMaximized()
            self.Restore.setMaximumSize(QtCore.QSize(30, 25))
            self.Restore.setStyleSheet("image: url(maximize.png);\n"
            "background: transparent;\n")


    def center(self):
        screen = QDesktopWidget().screenGeometry()
                 # Get window coordinates
        size = self.geometry()
                 # Calculate the center position
        newleft = (screen.width() - size.width())/2
        newTop = (screen.height() - size.height())/2
                 # Move to the center position
        self.move(newleft, newTop)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Question Pool"))
        self.label1.setText(_translate("MainWindow", "Assessment Designer"))
        self.label_2.setText(_translate("MainWindow", "Solution Designer"))
        self.label_3.setText(_translate("MainWindow", "About"))
        self.label_5.setText(_translate("MainWindow", "Help?"))
        self.label_4.setText(_translate("MainWindow", "     Add  Question"))
        self.label_6.setText(_translate("MainWindow", "   View/Delete/Modify"))
        self.opsol.setText(_translate("MainWindow", "     Add  Solution"))
        self.VDSol.setText(_translate("MainWindow", "   View/Delete Solution"))
        self.MSol.setText(_translate("MainWindow", "   Modify Solution"))
        self.newassess.setText(_translate("MainWindow", "   New Assessment"))
        self.Modassess.setText(_translate("MainWindow", "View/Delete Assessment"))
        self.Des.setText(_translate("MainWindow", "We have a tendency to square measure planning a user-friendly desktop based application(AUTO MATHEMATICS ASSESSMENT DESIGNER). This application can produce a page. On the prime of the page institute logo with its name, Student name space, Student ID space, Department space will appear automatically. subsequently, the application can have a keyboard having all symbols and needed information associated with Mathematics. Users are ready to create assessments by choosing symbols to form queries. Although the questions that the user writing will automatically save in the database and can be ready to use in any future assessment creating. The questions that is been saved is every which way display from the database to form a novel assessment for the consequent time. Like questions, the user is ready to write answers using the keyboard. For security functions, user can have a novel name or email address and the password so that only he/she create their assessments and make changes thereto, not the other individual."))
        self.ques.setText(_translate("MainWindow", "When we click on the modify button for modifying objectives, it dosen't show the options?\n\nYes, this won't show you have to check that how many options that question have and then you have to click on the objective radio button and enter the no of option then it will appear.\n\nHow we can add space during writing question?\n\nYou can write space by clicking on the space button which has placed on the right side of the text area.\n\nWhen user forget to generate the image of subjective part of question or objective part of question so the application can save it exactly the same?\n\nNo it won't save the exactly same there would chage like in subjective part will not save into the database or may be there would be some error so check before clicking on the save button. "))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
