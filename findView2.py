import sys
import os
from gtrends import gtrend
from crawlerlib import getSoup
import PyQt5.QtCore as Qt
from PyQt5 import uic
from webbrowser import get
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QDesktopWidget,
    QGridLayout,
    QHBoxLayout,
    QSplitter,
    QGroupBox,
    QTextEdit,
    QComboBox,
    QFrame,
    QTextBrowser,
    QLayout
)
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from pytrends.request import TrendReq
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import re
import urllib
from dropdownList import getDropdownList
from vis1 import getBlankText, getURL
import wikipedia
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


class DashboardView(QtWidgets.QWidget):
    def __init__(self):
        super(DashboardView, self).__init__()
        uic.loadUi('dashboardView.ui', self)

        self.checker = False


        self.inputQuery_D = self.findChild(QComboBox, 'comboBox')
        self.buttonThree = self.findChild(QPushButton, 'pushButton')
        self.buttonFour = self.findChild(QPushButton, 'pushButton_2')
        self.logo = self.findChild(QTextBrowser, 'textBrowser')

        self.blankText = self.findChild(QTextEdit, 'textEdit') 
        self.revsPerUser = self.findChild(QTextEdit, 'textEdit_2')
        self.revsPerDay = self.findChild(QTextEdit, 'textEdit_3')
        self.imgCount = self.findChild(QTextEdit, 'textEdit_4')
        self.canvasTrend = self.findChild(QWidget, 'widget_2')
        self.canvasTrend = FigureCanvas(Figure())
        self.canvasCloud = self.findChild(QWidget, 'widget_3')
        self.canvasCloud = FigureCanvas(Figure())
        self.canvasRevs = self.findChild(QWidget, 'widget_5')
        self.canvasRevs = FigureCanvas(Figure())
        self.canvasBlank = self.findChild(QWidget, 'widget_4')
        self.canvasBlank = FigureCanvas(Figure())
        self.buttonThree.clicked.connect(self.setDropdownItems)
        self.buttonFour.clicked.connect(self.call)

        self.view = QGridLayout()
        self.view.addWidget(self.buttonThree)
        self.view.addWidget(self.buttonFour)
        self.view.addWidget(self.inputQuery_D)
        self.view.addWidget(self.logo)
        self.view.addWidget(self.revsPerUser)
        self.view.addWidget(self.revsPerDay)
        self.view.addWidget(self.imgCount)
        self.view.addWidget(self.canvasTrend)
        self.view.addWidget(self.canvasRevs)
        self.view.addWidget(self.canvasBlank)
        self.view.addWidget(self.canvasCloud)
        self.setLayout(self.view)


    def setDropdownItems(self):
        print("searching results for: " + self.inputQuery_D.currentText())
        list = getDropdownList(self.inputQuery_D.currentText())
        self.inputQuery_D.addItems(list)
        self.buttonFour.clicked.connect(self.callFunctions)
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
        self.view.addWidget(self.canvasTrend)
    

    def drawWordCloud(self, text):
         stopwords = set(STOPWORDS)
         stopwords.update(["e.g"])
         wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)
         self.canvasCloud = FigureCanvas(Figure())
         self.axes = self.canvasCloud.figure.add_subplot()
         self.axes.axis('off')
         self.axes.imshow(wordcloud)
         self.canvasCloud.setMaximumWidth(400)
         self.canvasCloud.setMaximumHeight(300)
         self.canvasCloud.draw()
         self.view.addWidget(self.canvasCloud)

    def writeTextWiki(self, text):
         self.blankText.setText(text)
         print('writetextwiki')
         self.view.addWidget(self.blankText)
        

    def callFunctions(self):
        print(self.inputQuery_D.currentText())
        inp = self.inputQuery_D.currentText()
        text = getBlankText(inp)[0]
        #self.callFunctions(text, inp)


    def call(self):
        if(self.checker):
            self.buttonFour.clicked.connect(self.callFunctions)
            print("creating...")
        else: print("You need to get search results first!")
        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WikiPy = QtWidgets.QStackedWidget()
    dashboardview = DashboardView()
    WikiPy.addWidget(dashboardview)
    print(WikiPy.currentIndex())
    WikiPy.show()
    sys.exit(app.exec_())