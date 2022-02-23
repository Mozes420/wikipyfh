#imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import re
import urllib
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import difflib
import wikipedia
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
import matplotlib as mpl

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
				#print(z)
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
	
def getImages(wikipage):
			
	soup = getSoup(wikipage)
	body = soup.select('#mw-content-text > div.mw-parser-output')[0]
	ref_id = ['"References"', '"Notes"', '"Sources"', '"External_links"','"Notes,_citations,_and_references"', '"Bibliography"', '"See_also"', '"Further_reading"', '"Works_cited"']
	for id in ref_id:
		try:
			body_str = str(body).split(f'<span class="mw-headline" id={id}')[0]
			body = BeautifulSoup(body_str, 'html.parser')
			#body.find('span', {'class':'mw-headline', 'id':id}).decompose()
		except:
			print(id+': No such element found!')
			

	imgs = body.findAll('img')
	img_links = {}
	for img in imgs:
		try:
			r = requests.get('http://'+(img['src'].strip('/')), stream=True)
			img_link = 'http://'+(img['src'].strip('/'))
			img_title = img['alt']
			img_links[img_title] = img_link
			with open(f'images/{img_title}.jpg', 'wb') as f:
				r.raw.decode_content = True
				shutil.copyfileobj(r.raw,f)

			img = mpimg.imread(f'images/{img_title}.jpg')
			imgplot = plt.imshow(img)
			plt.show()

		except:
			pass
	return img_links
	
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
	revsperday = df.groupby(df['timestamp'].astype(datetime.date).apply(lambda x: x.strftime('%Y-%m-%d'))).count()['revid']
	revsperday = revsperday.reset_index()		
	revsperday = revsperday.rename(columns={'revid':'count'})
	return revsperday


def getRevsPerUser(wikititle):
	rev_df = getRevisions(wikititle)
	rev_df['timestamp'] = rev_df['timestamp'].apply(lambda x: x.strftime('%Y-%m-%d'))
	rev_dates = np.sort(rev_df['timestamp'].unique())
	result_df = pd.DataFrame(columns=['Date', 'RevsPerUser'])
	input = {'Date': None, 'RevsPerUser':None}
	for date in rev_dates:
		input['Date'] = date
		window_df = rev_df.loc[rev_df['timestamp']<=date]
		input['RevsPerUser'] = window_df['revid'].count()/len(window_df['user'].unique())
			
		result_df = result_df.append(input, ignore_index=True)
	return result_df

# get whole url of first articleversion with pagetitle (wikititle)
def getOldSoup(wikititle):
	soup = requests.get("https://en.wikipedia.org/w/index.php?title="+wikititle+"&dir=prev&action=history")
	soup = BeautifulSoup(soup.content, 'html.parser')
	soup = soup.findAll("a", {"class": "mw-changeslist-date"})[0]['href']
	return 'https://en.wikipedia.org/'+soup

# get whole url of recent articleversion with pagetitle (wikititle)
def getRecentSoup(wikititle):
	wiki = 'https://en.wikipedia.org/wiki/'
	recent = wiki+wikititle
	return recent

# get original text and recent text per article
def getTextDF(urlis):
    textdf = pd.DataFrame(columns=['page_title', 'original', 'recent'])
    for i in range(len(urlis)):
        if str(getTextBody(urlis[i][0])).startswith('Redirect to'):
            continue
        else:
            s1 = str(getTextBody(urlis[i][0]))
            s2 = str(getTextBody(urlis[i][1]))
            textdf = textdf.append({'page_title' : str.rsplit(urlis[i][1], '/', 1)[-1], 'original' : s1, 'recent' : s2}, ignore_index=True)
    return textdf

# get vocabularity density for given text
def getVD(text):
  tokens = nltk.word_tokenize(text)
  tagged = nltk.pos_tag(tokens)
  nn = []
  ok = 'NN' 
  for i in tagged:
    if ok == i[1]:
      nn.append(i[0])
  nn1 = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in nn]
  nn2 = []
  for i in nn1:
    if len(i) > 2:
      nn2.append(i)
    else:
      nn2.append('no text')
  try:
    VD = len(np.unique(nn2)) / len(nn2)
  except ZeroDivisionError:
    VD = 1
  return VD

# get words per sentence for given text
def getWPS(text):
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
    wps = sum(len(s) for s in sentences)/len(sentences)
    #print("average words per sentence: ", wps)
    return wps

# get words per text for given text
def getWPT(text):
    tokens = nltk.word_tokenize(text)
    words = tokens
    sentences = [[]]
    for word in words:
        sentences.append([word])
    wpt = len(sentences)
    return wpt

# function to tokenize and equalize 2 given texts
def tokenize(s):
    return re.split('\s+', s)
def untokenize(ts):
    return ' '.join(ts)
        
def equalize(s1, s2):
    l1 = tokenize(s1)
    l2 = tokenize(s2)
    res1 = []
    res2 = []
    prev = difflib.Match(0,0,0)
    for match in difflib.SequenceMatcher(a=l1, b=l2).get_matching_blocks():
        if (prev.a + prev.size != match.a):
            for i in range(prev.a + prev.size, match.a):
                res2 += ['_' * len(l1[i])]
            res1 += l1[prev.a + prev.size:match.a]
        if (prev.b + prev.size != match.b):
            for i in range(prev.b + prev.size, match.b):
                res1 += ['_' * len(l2[i])]
            res2 += l2[prev.b + prev.size:match.b]
        res1 += l1[match.a:match.a+match.size]
        res2 += l2[match.b:match.b+match.size]
        prev = match
    return untokenize(res1), untokenize(res2)

# function to visualize comparison of texts human-readable
def insert_newlines(string, every=40, window=10):
    result = []
    from_str = string
    while len(from_str) > 0:
        cut_off = every
        if len(from_str) > every:
            while (from_str[cut_off - 1] != ' ') and (cut_off > (every-window)):
                cut_off -= 1
        else:
            cut_off = len(from_str)
        part = from_str[:cut_off]
        result += [part]
        from_str = from_str[cut_off:]
    return result

# tokenize, equalize and show comparison of texts
def show_comparison(s1, s2, width=40, margin=10, sidebyside=True, compact=False):
    s1, s2 = equalize(s1,s2)

    if sidebyside:
        s1 = insert_newlines(s1, width, margin)
        s2 = insert_newlines(s2, width, margin)
        if compact:
            for i in range(0, len(s1)):
                lft = re.sub(' +', ' ', s1[i].replace('_', '')).ljust(width)
                rgt = re.sub(' +', ' ', s2[i].replace('_', '')).ljust(width) 
                print(lft + ' | ' + rgt + ' | ')        
        else:
            for i in range(0, len(s1)):
                lft = s1[i].ljust(width)
                rgt = s2[i].ljust(width)
                print(lft + ' | ' + rgt + ' | ')
    else:
        print(s1)
        print(s2)

# gets original and recent texts from wikipedia-articles by iterating through the urls
# that are extracted from the dataframe into a zipped list ("urlis")
def getTextDF(urlis):
    textdf = pd.DataFrame(columns=['page_title', 'original', 'recent'])
    for i in range(len(urlis)):
        if str(getTextBody(urlis[i][0])).startswith('Redirect to'):
            continue
        else:
            s1 = str(getTextBody(urlis[i][0]))
            s2 = str(getTextBody(urlis[i][1]))
            textdf = textdf.append({'page_title' : str.rsplit(urlis[i][1], '/', 1)[-1], 'original' : s1, 'recent' : s2}, ignore_index=True)
    return textdf