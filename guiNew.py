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



        # self.canvas.axes = self.canvas.figure.add_subplot(111)
        # #self.setLayout(self.vertical_layout)

        # fs = 500
        # f = random.randint(1, 100)
        # ts = 1/fs
        # length_of_signal = 100
        # t = np.linspace(0,1,length_of_signal)

        # cosinus_signal = np.cos(2*np.pi*f*t)
        # sinus_signal = np.sin(2*np.pi*f*t)

        # self.canvas.axes.clear()
        # self.canvas.axes.plot(t, cosinus_signal)
        # self.canvas.axes.plot(t, sinus_signal)
        # self.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
        # self.canvas.axes.set_title('Cosinus - Sinus Signal')
        # self.canvas.draw()


        ################################################
        # self.pytrends = TrendReq(hl='en-US', tz=360)
        # self.pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
        # keywords = self.pytrends.suggestions(keyword=input[0])
        # df = pd.DataFrame(keywords)
        # df.drop(columns= 'mid')
        # dfg = self.pytrends.interest_over_time()
        # self.canvas = FigureCanvas(Figure())
        # self.canvas.axes = self.canvas.figure.add_subplot(111)
        # self.canvas.axes.clear()
        # self.canvas.axes.set_title('Relative search term frequency')
        # self.canvas.axes.plot(dfg)
        # self.canvas.axes.legend(loc='lower left')
        # self.canvas.draw()
        

        

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
        #print("Success")
        # ax = fig.add_subplot(111)
        # dfg.plot(ax=ax)
        # plt.ylabel('Relative search term frequency')
        # plt.xlabel('Date')
        # plt.ylim((0,120))
        # plt.legend(loc='lower left')
        # #plt.plot(dfg, 'k')
        # return plt.show()
    


    def readInput(self):  # this function can be used to read user input and call a function based on the input                                                                                   
        print('' + self.input.text())
        text = [self.input.text()]
        self.gtrend(text)

    def getSoup(wikipage):
	#get page to soup
        page = requests.get(wikipage)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup
	
    def getHeadline(wikipage):
        #article name / headline
        soup = getSoup(wikipage)
        headline = soup.findAll('h1')[0].getText()
        return headline
        
    def getTextBody(wikipage, setblock = True):
        #limit soup to actual article content
        soup = getSoup(wikipage)
        body = soup.select('#mw-content-text > div.mw-parser-output')[0]
        try:
            for tag in body.findAll('table'):
                tag.decompose()
        except:
            print('No table found')

        try:
            for tag in body.findAll('div', {'class':'shortdescription nomobile noexcerpt noprint searchaux'}):
                tag.decompose()
        except:
            print('No shortdescription found') 
            
        try:
            for tag in body.findAll('ol', {'class':'references'}):
                tag.decompose()
        except:
            print('No references found') 
            
        try:
            for tag in body.findAll('abbr'):
                tag.decompose()
        except:
            print('No abbriviation found') 
            
        x = str(body)
        body_headlines = []
        body_text = []

        c = 1

        z = x.split('h2')

        for i in z:
            if c%2 == 1:
                body_text.append(i)
            else:
                body_headlines.append(i)
            c+=1
        headlines = []

        for i in body_headlines:
            soup = BeautifulSoup(i, 'html.parser')
            headlines.append(soup.text)
        headlines_body = [i.replace(' id="mw-toc-heading">Contents</', 'Contents') for i in headlines]
        headlines_body = [i.replace('>', '') for i in headlines_body]
        headlines_body = [i.replace('[edit]</', '') for i in headlines_body]
        text = []

        for i in body_text:
            soup = BeautifulSoup(i, 'html.parser')
            text.append(soup.text)
        text_body = [i.replace('\n', '') for i in text]
        text_body = [i.replace('>', '') for i in text_body]
        text_body = [i.replace('<', '') for i in text_body]
        first_lines = text_body[0]
        #headlines_body
        ref_id = ['Contents', 'References', 'Notes', 'Sources', 'External link','Notes, citations, and references', 'Bibliography', 'Works cited']

        for i in ref_id:
            z = 0
            for e in headlines_body:
                if e == i:
                    headlines_body.remove(e)
                    print(z)
                    text_body.pop(z)
                else:
                    z += 1
        c = len(headlines_body)

        if c == 0:
            c = 1

        r = 0

        final_elements = []

        while r < c:
            if r == 0:
                final_elements.append(first_lines)
            if len(headlines_body) == 0 :
                break
            else:
                final_elements.append(headlines_body[r])
                final_elements.append(text_body[r])
            r += 1
        cleaned_list = [i.replace('[edit]', ' ') for i in final_elements]
        cleaned_list = [i.replace('\xa0', ' ') for i in cleaned_list]


        final_list =[]

        for i in cleaned_list:
            match = re.sub(r'\[\d{1,3}]', '', i)
            final_list.append(match)
            
        final = []
        
        if setblock:
            final = [i.replace(', ', ',') for i in final_list]
            final = [i.replace('. ', '.') for i in final]
            final = [i.replace('"', '') for i in final]
        else:
            for i in final_list:
                x = i + '\n\n'
                final.append(x)
        list1 = ' '.join(final)
        body2 = BeautifulSoup(list1, 'html.parser')
            
        return body2
        
    def getImgCnt(wikipage):
        soup = getSoup(wikipage)
        #drop content after 'References' section (for imagecount)
        body = soup.select('#mw-content-text > div.mw-parser-output')[0]
        ref_id = ['"References"', '"Notes"', '"Sources"', '"External_links"','"Notes,_citations,_and_references"', '"Bibliography"', '"See_also"', '"Further_reading"', '"Works_cited"']
        for id in ref_id:
            try:
                body_str = str(body).split(f'<span class="mw-headline" id={id}')[0]
                body = BeautifulSoup(body_str, 'html.parser')
                #body.find('span', {'class':'mw-headline', 'id':id}).decompose()
            except:
                print(id+': No such element found!')
            

        #get number of images in the article
        img_count = len(body.findAll('img'))
        return img_count
        
    def getRevisions(wikititle):
        url = "https://en.wikipedia.org/w/api.php?action=query&format=xml&prop=revisions&rvlimit=500&titles="+wikititle 
        revisions = []                                        #list of all accumulated revisions
        next = ''                                             #information for the next request

        while True:
            response = urllib.request.urlopen(url + next).read()     #web request

            response = str(response)

            revisions += re.findall('<rev [^>]*>', response)  #adds all revisions from the current request to the list

            cont = re.search('<continue rvcontinue="([^"]+)"', response)
            if not cont:                                      #break the loop if 'continue' element missing
                break

            next = "&rvcontinue=" + cont.group(1)             #gets the revision Id from which to start the next request
            
        rev_list = []
        rev_dict_list = []
        for rev_string in revisions:
            split_rev = rev_string.split(' ')[1:-1] 
            for i in range(len(split_rev)):
                if re.search('comment', split_rev[i]) != None:
                    split_rev[i] = " ".join(split_rev[i:])
                    split_rev = split_rev[:i+1]
                    rev_list.append(split_rev)
                    break
                
        for rev in rev_list:
            rev_attr_dict = {}
            for attr in rev:
                kv = kv_list = attr.split("=")
                try:
                    rev_attr_dict[kv[0]] = kv[1].strip('"')
                except:
                    pass
            rev_dict_list.append(rev_attr_dict)
                
        df = pd.DataFrame.from_dict(rev_dict_list)
        df = df.astype({'revid':'int64', 'parentid':'int64'})
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y%m%d %H:%M:%S')
        return df
        
    def getRevsPerDay(df):
        revsperday = df.groupby(df['timestamp'].apply(lambda x: x.strftime('%Y-%m-%d'))).count()['revid']
        revsperday = revsperday.reset_index()		
        revsperday = revsperday.rename(columns={'revid':'count'})
        return revsperday





# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# app.exec()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    WikiPy = GroupBox()
    WikiPy.show()
    sys.exit(app.exec_())

""" def gtrendQT(self, input):
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
        keywords = pytrends.suggestions(keyword=input[0])
        df = pd.DataFrame(keywords)
        df.drop(columns= 'mid')
        dfg = pytrends.interest_over_time()

        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.graphWidget.plot(dfg, pen) """