'''
def getBlankText(keyword):
  url = getURL(keyword)
  x = url.split(sep="/", maxsplit=-1)[-1:]
  page = wikipedia.page(x[-1:])
  content = page.content.replace('\n', '')
  print(page)
  print(content[0:50],'...')
  return content
'''

'''
pip install pysummarization

from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor
'''

def getSummary(keyword):
  Summary = []
  doc = getBlankText(keyword)
  aa = AutoAbstractor()
  aa.tokenizable_doc = SimpleTokenizer()
  aa.delimiter_list = ['.', '\n']
  adoc = TopNRankAbstractor()
  result_dict = aa.summarize(doc, adoc)
  for sentence in result_dict['summarize_result']:
    print(sentence)
    Summary.append(sentence)
    
# getSummary('natural language processing')
