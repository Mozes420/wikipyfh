import sys
import os
import random
from random import choice
from crawlerlib import getSoup
#from gtrends import gtrend
import PyQt5.QtCore as Qt
from PyQt5 import uic
import PyQt5.uic.Loader

from webbrowser import get
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QDesktopWidget,
    QGridLayout,
    QGroupBox,
    QTextEdit,
    QComboBox
)
import PyQt5.QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
 






class WelcomeScreen(QtWidgets.QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        uic.loadUi('welcomeScreen.ui', self)

        self.inputQuery = self.findChild(QComboBox, 'inputQuery')
        #self.inputQuery.setEditable(True)
        self.buttonOne = self.findChild(QPushButton, 'buttonOne')
        #self.buttonOne.clicked.connect(self.)
        self.buttonTwo = self.findChild(QPushButton, 'buttonTwo')
        



# class Dashboard(QtWidgets.QDialog):
#     def __init__(self):
#         super(Screen2):
# main
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    WikiPy = WelcomeScreen()
    WikiPy.show()
    sys.exit(app.exec_())
