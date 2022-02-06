import requests
import wikipedia
import nltk
nltk.download('stopwords')
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import spacy
en = spacy.load('en_core_web_sm')
from collections import Counter

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# Funktion zum Erhalten der Wikipedia-URL, erlaubt bis zu 2 Tippfehler und wirft bestes Ergebnis aus: 

def getURL(keyword):
  S = requests.Session()
  URL = "https://en.wikipedia.org/w/api.php"
  PARAMS = {
    "action": "opensearch",
    "search": keyword,
    "limit": "1",
    "format": "json", 
    'profile': 'fuzzy'
    }
  R = S.get(url=URL, params=PARAMS)
  got = R.json()
  wikititle = got[3]
  wt1 = ''.join(str(e) for e in wikititle)
  #print(wt1)
  return wt1

#wikiurl = getURL('NLP')

# vereinfachte Funktion zum Erhalten des reinen Seitentextes (ohne Rücksichtnahme auf Formeln, Verweise etc. -> werden mit NLTK-Funktion in Folge entfernt)

def getBlankText(keyword):
  url = getURL(keyword)
  x = url.split(sep="/", maxsplit=-1)[-1:]
  page = wikipedia.page(x[-1:])
  textFull = page.content
  content = page.content.replace('\n', '') 
  print(page)
  #print(content[0:50],'...')
  return content, textFull


def freqWords(keyword):
    text = getBlankText(keyword)[0]
    text_c = re.sub('[\W_]+', ' ', text)
    text_tokenized = nltk.tokenize.word_tokenize(text_c)
    stopwords = en.Defaults.stop_words
    stopwords.update(["e.g", "e", "g", "The"])
    text_sw = [word for word in text_tokenized if not word in stopwords]
    words = []
    for i in text_sw:
      if len(i) > 2:
        words.append(i)
    words_final = [x for x in words if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
    Count_words = Counter(words_final)
    most_frequent = Count_words.most_common(10)
    # wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(text)"""
    x_axis = []
    y_axis = []
    for i in most_frequent:
      x_axis.append(i[0])
      y_axis.append(i[1])
    tot_words = len(text_tokenized) # alle Wörter
    after_stopwords = len(words_final) # ohne stopwords
    stopword_count = tot_words - after_stopwords # nur stopwords
    word_percent = after_stopwords/tot_words # anteil an nicht stopwords
    stopword_number = 1-word_percent # anteil an stopwords
    stopword_percent = 100 * stopword_number # anteil an stopwords in prozent
    stop_per_round = round(stopword_percent, 2) # anteil an stopwords in prozent gerundet
    print(tot_words)
    print(after_stopwords)
    print(stopword_count)
    print(stop_per_round)
    return most_frequent, x_axis, y_axis, after_stopwords, stopword_count
    

#freqWords("Natural language Processing")
#freqWords("1198")
#freqWords("American Football")
#freqWords("Barack Obama")
#freqWords("China")
#freqWords("1")
#freqWords("Angela Merkel")

def WordPlot(keyword):
  most_frequent, x_axis, y_axis, after_stopwords, stopword_count = freqWords(keyword)
  plt.bar(x_axis, y_axis)
  plt.ylabel('Word Count')
  plt.show()
  
def StopWordPlot(keyword):
  most_frequent, x_axis, y_axis, after_stopwords, stopword_count = freqWords(keyword)
  labels = "normal Words", "Stopwords"
  sizes = [after_stopwords, stopword_count]
  plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
  plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.show() 

WordPlot("Angela Merkel")
StopWordPlot("Angela Merkel")
