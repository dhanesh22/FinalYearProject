import requests
import pandas as pd
from bs4 import BeautifulSoup

# Getting short summaries from WELIVESECURITY
data1 = []
for i in range(280):
     resp = requests.get('https://www.welivesecurity.com/page/'+ str(i+1)+'/')
     soup = BeautifulSoup(resp.text, 'html.parser')
     ShortSummary = soup.select('[class="news-feed-item col-xs-12 no-padding"]')
     print(len(ShortSummary))
     for shortSum in ShortSummary:
         summary = shortSum.select('[class="text-wrapper col-sm-9 col-xs-8 no-padding"] p')
         if len(summary) == 0:
               data1.append("Null")
         else:
               data1.append((summary[0].getText()).replace("\n", ""))
     df = pd.DataFrame(data1)
     df.columns= ['Short_Summary']
     print(df)
     df.to_excel('short-Summaryy.xlsx', index=False, header=True)