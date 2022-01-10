import requests
import pandas as pd
from bs4 import BeautifulSoup


data = []
# GETTING HEADLINES OF THE NEWS
for i in range(280):
     resp = requests.get('https://www.welivesecurity.com/page/'+ str(i+1)+'/')
     soup = BeautifulSoup(resp.text, 'html.parser')
     top_stories = soup.select('[id="news-feed"] h2')
     print(len(top_stories))

     for top_story in top_stories:
         headline = top_story.getText()
         if len(headline) == 0:
             data.append("null")
         else:
             data.append([headline])
     df = pd.DataFrame(data)
     df.columns = ['Headline']
     print(df)
     df.to_excel('Headlines.xlsx', index=False, header=True)

