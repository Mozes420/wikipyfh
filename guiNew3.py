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
from dropdownList import getDropdownList
from PyQt5 import uic

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
from gtrends import gtrend

from vis1 import getBlankText, getURL
import wikipedia
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# Einstiegsbildschirm

class WelcomeScreen(QtWidgets.QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        uic.loadUi('welcomeScreen.ui', self)

        self.checkerWelcome = False

        self.testBox = GroupBox()

        #Festlegen von Params 
        self.setWindowTitle("WikiPy")
        self.resize(800,600)

        #Finden der UI-Widgets
        self.inputQuery = self.findChild(QComboBox, 'comboBox')
        self.buttonOne = self.findChild(QPushButton, 'pushButton')
        self.buttonOne.clicked.connect(self.setDropdownItems)
        self.buttonTwo = self.findChild(QPushButton, 'pushButton_2')
        self.buttonTwo.clicked.connect(self.call)


    def setDropdownItems(self):
        print("searching results for: " + self.inputQuery.currentText())
        list = getDropdownList(self.inputQuery.currentText())
        self.inputQuery.addItems(list)
        self.checkerWelcome = True
        print("done")
        

    def setIndexToOne(self):
        print('set index to one function call')
        WikiPy.setCurrentIndex(1)
        self.callFunctions()
        

    def callFunctions(self):
        #WikiPy.setCurrentIndex(0)
        print(self.inputQuery.currentText())
        inp = self.inputQuery.currentText()
        text = getBlankText(inp)[0]
        #WikiPy.setCurrentIndex(1)
        self.testBox.callFunctions(text, inp)



    def call(self):
        if(self.checkerWelcome):
            #self.buttonTwo.clicked.connect(self.setIndexToOne)
            print("creating...")
            self.setIndexToOne()
        else: print("You need to get search results first!")



# Dashboard Bildschirm

class GroupBox(QtWidgets.QWidget):

    #Initialisieren der Klasse
    def __init__(self):
        super().__init__()

        # Anfangsfenster setzen, Größe auswählen und zentrieren

        self.checker = False

        self.setWindowTitle("WikiPy")
        screen = QDesktopWidget().screenGeometry()
        self.resize(int(screen.width()/2), int(screen.height()/2))
        form = self.geometry()
        x_move_step = (screen.width() - form.width())
        y_move_step = (screen.height() - form.height())
        self.move(int(x_move_step/2), int(y_move_step/2))
    
        self.layout = QGridLayout(self)
        self.groupbox = QGroupBox("Start you Knowledge!", checkable=False)
        self.layout.addWidget(self.groupbox)

        # Einfügen von Text Input Feld

        self.input = QLineEdit("Type your search ...")
        self.input.setMaximumHeight(100)
        self.input.setMaximumWidth(400)

        # Einfügen von Button der Anfragen mit Input des Line Edit startet

        self.button = QPushButton("Get Search Results")
        self.button.setParent(self)
        #self.button.clicked.connect(self.readInput)
        self.button.clicked.connect(self.setDropdownItems)
        self.button.setMaximumHeight(25)
        self.button.setMaximumWidth(200)

        self.comboBox = QComboBox(self)
        self.comboBox.setEditable(True)
        self.comboBox.setMinimumWidth(300)

        self.button2 = QPushButton("Go!")
        self.button2.setParent(self)
        #self.button2.clicked.connect(self.readInput)
        self.button2.setMaximumHeight(25)
        self.button2.setMaximumWidth(200)
        self.button2.clicked.connect(self.call)
            

        # Einfügen von befüllten Widgets
        #############################################
        self.canvasTrend = FigureCanvas(Figure())
        self.canvasTrend.setParent(self)
        self.canvasTrend.setMaximumWidth(400)
        self.canvasTrend.setMaximumHeight(300)

        self.canvasCloud = FigureCanvas(Figure())
        self.canvasCloud.setParent(self)
        self.canvasCloud.setMaximumWidth(400)
        self.canvasCloud.setMaximumHeight(300)

        self.blankText = QTextEdit(self) ################ WORK IN PROGRESS
        self.blankText.setMinimumWidth(300)
        self.blankText.setMinimumHeight(400)
        self.blankText.setParent(self)

        self.grid = QGridLayout()
        self.groupbox.setLayout(self.grid)
        #self.grid.addWidget(self.input, 0,0,1,3, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.button, 0,0,1,2, PyQt5.QtCore.Qt.AlignRight)
        self.grid.addWidget(self.button2, 0,1,1,2, PyQt5.QtCore.Qt.AlignRight)
        self.grid.addWidget(self.canvasTrend, 1,0, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.canvasCloud, 1,1, PyQt5.QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.blankText, 1,2, PyQt5.QtCore.Qt.AlignCenter) ####################### WIP
        self.grid.addWidget(self.comboBox, 0,0,1,2, PyQt5.QtCore.Qt.AlignCenter)

    # Funktion aufrufen Welcome Screen

    def start(self):
        welcomeScreen = WelcomeScreen()
        if welcomeScreen.exec_():
            self.show()
        else:
            welcomeScreen.exec_()

    # Funktion muss in die Klasse

    def setDropdownItems(self):
        print("searching results for: " + self.comboBox.currentText())
        list = getDropdownList(self.comboBox.currentText())
        self.comboBox.addItems(list)
        self.button2.clicked.connect(self.callFunctions)
        self.checker = True
        print("done")


    def gtrend(self, input):
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
        keywords = pytrends.suggestions(keyword=input[0])
        df = pd.DataFrame(keywords)
        df.drop(columns= 'mid')
        dfg = pytrends.interest_over_time().drop(labels=['isPartial'],axis='columns')
        self.canvasTrend = FigureCanvas(Figure())
        self.canvasTrend.axes = self.canvasTrend.figure.add_subplot(111)
        self.canvasTrend.axes.clear()
        self.canvasTrend.axes.set_title('Relative Search Term Frequency')
        self.canvasTrend.axes.plot(dfg)
        self.canvasTrend.axes.legend((dfg[0:0]),loc='upper right')
        self.canvasTrend.draw()
        self.canvasTrend.axes.set_xlabel('Time')
        self.canvasTrend.axes.set_ylabel('Frequency')
        self.canvasTrend.axes.set_xticklabels(labels=dfg.index[:,], rotation=45)
        self.canvasTrend.setMaximumWidth(400)
        self.canvasTrend.setMaximumHeight(300)
        self.grid.addWidget(self.canvasTrend, 1,0, PyQt5.QtCore.Qt.AlignCenter)
    

    # def drawWordCloud(self, text):
    #     stopwords = set(STOPWORDS)
    #     stopwords.update(["e.g"])
    #     wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
    #     self.canvasCloud = FigureCanvas(Figure())
    #     self.axes = self.canvasCloud.figure.add_subplot()
    #     self.axes.axis('off')
    #     self.axes.imshow(wordcloud)
    #     self.canvasCloud.setMaximumWidth(400)
    #     self.canvasCloud.setMaximumHeight(300)
    #     self.grid.addWidget(self.canvasCloud, 1,1, PyQt5.QtCore.Qt.AlignCenter)


    def writeTextWiki(self, text): ########################### WIP 
         self.blankText.setText(text)
         print('writetextwiki')
         self.grid.addWidget(self.blankText, 1,2, PyQt5.QtCore.Qt.AlignCenter)
        

    def callFunctions(self, text, inp):
        self.gtrend([inp])
        #self.drawWordCloud(text)
        self.writeTextWiki(text)

    def call(self):
        if(self.checker):
            self.button2.clicked.connect(self.callFunctions)
            print("creating...")
        else: print("You need to get search results first!")
        



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WikiPy = QtWidgets.QStackedWidget()
    welcomescreen = WelcomeScreen()
    #groupbox = GroupBox()
    WikiPy.addWidget(welcomescreen)
    WikiPy.addWidget(welcomescreen.testBox)
    print(WikiPy.currentIndex())
    WikiPy.show()

    sys.exit(app.exec_())