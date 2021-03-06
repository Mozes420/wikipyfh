#{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"getrevplot.py","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyPVS9ncCfsZc2iMl/mM9HMp"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"6_R7Disu9J1J"},"outputs":[],"source":["def getrevplot(wikititle):\n","  revplot = getRevisions(wikititle)\n","  revplot0 = revplot.drop(columns = ['revid', 'parentid', 'minor', 'comment', 'anon', 'commenthidden'])\n","  revplot1 = revplot0[revplot.timestamp.between('2015-01-01', '2021-12-31', inclusive=False)]\n","  revplot2 = revplot1.set_index('timestamp')\n","  revplot3 = revplot2.groupby(pd.Grouper(freq='M')).count()\n","  plt.figure()\n","  plt.plot(revplot3, 'k')"]}]}
import pandas as pd
import matplotlib.pyplot as plt
from crawlerlib import getRevisions

def getrevplot(wikititle):
  revplot = getRevisions(wikititle)
  revplot0 = revplot.drop(columns = ['revid', 'parentid', 'minor', 'comment', 'anon', 'commenthidden'])
  revplot1 = revplot0[revplot.timestamp.between('2015-01-01', '2021-12-31', inclusive=False)]
  revplot2 = revplot1.set_index('timestamp')
  revplot3 = revplot2.groupby(pd.Grouper(freq='M')).count()
  plt.figure()
  plt.plot(revplot3, 'k')