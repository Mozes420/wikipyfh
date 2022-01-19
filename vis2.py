import requests
import wikipedia
import nltk
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
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

wikiurl = getURL('NLP')

# vereinfachte Funktion zum Erhalten des reinen Seitentextes (ohne Rücksichtnahme auf Formeln, Verweise etc. -> werden mit NLTK-Funktion in Folge entfernt)

def getBlankText(keyword):
  url = getURL(keyword)
  x = url.split(sep="/", maxsplit=-1)[-1:]
  page = wikipedia.page(x[-1:])
  content = page.content.replace('\n', '')
  print(page)
  print(content[0:50],'...')
  return content

page1 = getBlankText('natural langage processing')


  # Funktion zum Erhalten der Wörter pro Satz; 

##### TODO: Kontrolle, ob weitere Satzenden definiert werden müssen #####

def getWIA(keyword):
  url = getURL(keyword)
  text = getBlankText(keyword)
  tokens = nltk.word_tokenize(text)
  words = tokens
  sentences = [[]]
  ends = set(".?!;:")
  for word in words:
    if word in ends: 
      sentences.append([])
    else: 
      sentences[-1].append(word)
  if sentences[0]:
    if not sentences[-1]: sentences.pop()
    wia = sum(len(s) for s in sentences)
    print("average words per document: ", wia)
    return wia

wia = getWIA('natural language processing')

def AvgReadingSpeed(keyword, wia):
  Average200 = wia/200
  Average250 = wia/250
  Average300 = wia/300
  print(Average200, Average250, Average300)
  Average1 = (Average200 + Average250 + Average300)/3
  print(Average1)
  return Average200, Average250, Average300, Average1

AvgReadingSpeed('natural language processing', wia)
