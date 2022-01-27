pip install pysummarization

from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

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
