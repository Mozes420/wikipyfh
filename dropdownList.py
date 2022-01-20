import requests

def getDropdownList(query): 
    #query = input("Enter term : ")

    OPTIONS = []
    VALUES = []

    url = "https://www.wikidata.org/w/api.php"

    params = {
            "action" : "wbsearchentities",
            "language" : "en",
            "format" : "json",
            "search" : query, 
            "limit":50
            }

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
    return OPTIONS
