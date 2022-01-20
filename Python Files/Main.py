import sys
import platform
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from SplashScreen import Ui_SplashScreen
from SignupScreen import Ui_SignupScreen
from LoginScreen import Ui_LoginScreen
import source


## ==> GLOBALS
counter = 0

# YOUR APPLICATION


# SPLASH SCREEN
class SplashWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)


        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.SplashProgressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # CLOSE SPLASH SCREEN
            self.close()

            # SHOW Login WINDOW
            self.log = QtWidgets.QMainWindow()
            self.l = Ui_LoginScreen()
            self.l.setupUi(self.log)
            #self.l.pushButton1.clicked.connect(self.sig.show)

            # SHOW Signup WINDOW
            self.sig = QtWidgets.QMainWindow()
            self.s = Ui_SignupScreen()
            self.s.setupUi(self.sig)
            self.s.label_5.clicked.connect(self.log.show)
            self.s.label_5.clicked.connect(self.sig.close)
            self.sig.show()

            self.l.pushButton1.clicked.connect(self.sig.show)
            self.l.pushButton1.clicked.connect(self.log.show)



        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashWindow()
    sys.exit(app.exec_())
