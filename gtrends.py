import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def gtrend(input):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(input, cat=0, timeframe='2020-01-01 2022-01-31', geo='US', gprop='')
    keywords = pytrends.suggestions(keyword=input[0])
    df = pd.DataFrame(keywords)
    df.drop(columns= 'mid')
    dfg = pytrends.interest_over_time()
    print(pd.DataFrame.head(dfg.iloc[:, 0]))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    dfg.plot(ax=ax)
    plt.ylabel('Relative search term frequency')
    plt.xlabel('Date')
    plt.ylim((0,100))
    plt.legend(loc='lower left')
    #plt.plot(dfg, 'k')
    return plt.show()

gtrend(['NLP'])
