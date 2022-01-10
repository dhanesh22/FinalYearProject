import requests
import pandas as pd
from bs4 import BeautifulSoup


#getting acaegories
data3 = []
for i in range(280):
        resp = requests.get('https://www.welivesecurity.com/page/'+ str(i+1)+'/')
        soup = BeautifulSoup(resp.text, 'html.parser')
        category = soup.select('[id="news-feed"] [class="img-wrapper col-sm-3 col-xs-4 no-padding"]')
        print(category)
        print(len(category))
        for cat in category:
             GetCategory = cat.getText()
             if len(GetCategory) == 0:
                 data3.append("null")
             else:
                 data3.append([GetCategory])
        df = pd.DataFrame(data3)
        df.columns= ['Category']
        print(df)
        df.to_excel('categories.xlsx', index=False, header=True)