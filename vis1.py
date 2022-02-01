import requests
import wikipedia
import nltk
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

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
  print('vis1')
  print(page)
  #print(content[0:50],'...')
  return content, textFull

#page1 = getBlankText('nlp')

#stopwords = set(STOPWORDS)
#stopwords.update(["e.g"])

# wordcloud = WordCloud(stopwords=stopwords, max_font_size=50, max_words=100, background_color="white").generate(page1)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()