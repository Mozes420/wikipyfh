import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QDesktopWidget, QSpacerItem, QSizePolicy, QGridLayout, QGroupBox
import PyQt5.QtCore 
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

import sys
import random
from random import choice
from crawlerlib import getSoup
#from gtrends import gtrend
import numpy as np

# for gtrends
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

# for plotting in qt
#import pyqtgraph as pg
#from pyqtgraph import PlotWidget, plot

# for crawlerlib
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import re
import urllib


class GroupBox(QtWidgets.QWidget):

    #Initialisieren der Klasse
    def __init__(self):
        super().__init__()

        # Anfangsfenster setzen, Größe auswählen und zentrieren

        self.setWindowTitle("WikiPy")
        screen = QDesktopWidget().screenGeometry()
        self.resize(int(screen.width() / 2), int(screen.height() / 2))
        form = self.geometry()
        x_move_step = (screen.width() - form.width()) / 2
        y_move_step = (screen.height() - form.height()) / 2
        self.move(int(x_move_step), int(y_move_step))
    
        self.layout = QGridLayout(self)
        self.groupbox = QGroupBox("Start you Knowledge!", checkable=False)
        self.layout.addWidget(self.groupbox)

        # Einfügen von Text Input Feld

        self.input = QLineEdit("Suchanfrage eingeben")
        self.input.setMaximumHeight(100)
        self.input.setMaximumWidth(200)

        # Einfügen von Button der Anfragen mit Input des Line Edit startet

        self.button = QPushButton("Suchen!")
        self.button.setParent(self)
        self.button.clicked.connect(self.readInput)
        self.button.setMaximumHeight(100)
        self.button.setMaximumWidth(400)

        # Einfügen von Layout Funktionen
        #############################################
        self.canvas = FigureCanvas(Figure())
        self.canvas.setParent(self)

        

        self.grid = QGridLayout()
        self.groupbox.setLayout(self.grid)
        self.grid.addWidget(self.input, 1,1, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.button, 1,2, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.canvas, 2,1, PyQt5.QtCore.Qt.AlignCenter)

        # Spacer Items



    # Funktion muss in die Klasse

    def gtrend(self, input):
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
        keywords = pytrends.suggestions(keyword=input[0])
        df = pd.DataFrame(keywords)
        df.drop(columns= 'mid')
        dfg = pytrends.interest_over_time()
        #fig = plt.figure()
        self.canvas = FigureCanvas(Figure())
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.axes.clear()
        self.canvas.axes.set_title('Relative search term frequency')
        self.canvas.axes.plot(dfg)
        self.canvas.axes.legend((""),loc='lower left')
        self.canvas.draw()
        self.grid.addWidget(self.canvas, 2, 1, PyQt5.QtCore.Qt.AlignCenter)
    


    def readInput(self):  # this function can be used to read user input and call a function based on the input                                                                                   
        print('' + self.input.text())
        text = [self.input.text()]
        self.gtrend(text)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WikiPy = GroupBox()
    WikiPy.show()
    sys.exit(app.exec_())