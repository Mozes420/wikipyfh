import requests
from tkinter import *
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.wikidata.org/w/api.php"

VALUES = []

while True:
    OPTIONS = []
    query = input("Enter name : ")
    if query == "quit":
        break
    else:
        params = {
        "action" : "wbsearchentities",
        "language" : "en",
        "format" : "json",
        "search" : query, 
        "limit":10
        }
        
        try:
            OPTIONS = []
            VALUES = []

            data = requests.get(url,params=params)
            par = len(data.json()["search"])

            for i in range(par):
                djs = data.json()["search"][i]
                lendjs = len(djs)
                #print(djs)
                for j in djs:
                    #print(j)
                    if j == 'description':
                      if data.json()["search"][i]["description"] == 'Wikimedia disambiguation page':
                        continue
                      OPTIONS.append(data.json()["search"][i]["description"])
                      VALUES.append(data.json()["search"][i])
                    elif j == 'label':
                      OPTIONS.append(data.json()["search"][i]["label"])
                      VALUES.append(data.json()["search"][i])
                    else: 
                      continue
                
        except:
            print("Invalid Input try again !!!")
            
            
        master = Tk()

        variable = StringVar(master)
        variable.set(OPTIONS[0]) # default value

        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()
        
        def get_scraping_link(dropdown):
            wikipage = []
            selected = 'o'
            for i in VALUES:
                if i["description"] == dropdown:
                    selected = i
            page = requests.get(selected['concepturi'])
            soup = BeautifulSoup(page.content, 'html.parser')
            mydivs = soup.find_all("li", {"class": "wikibase-sitelinkview wikibase-sitelinkview-enwiki listview-item"})
            for i in mydivs:
                print(i)
                wikipage.append(soup.find_all("span", {"class": "wikibase-sitelinkview-link wikibase-sitelinkview-link-enwiki"}))
            return wikipage
        
        def change_dropdown(*args):
            global dropdown
            dropdown = str(variable.get())
            return dropdown

        variable.trace('w', change_dropdown)
        
        dropdown = change_dropdown()
        wikipage = get_scraping_link(dropdown)
        print(wikipage)

        mainloop()
