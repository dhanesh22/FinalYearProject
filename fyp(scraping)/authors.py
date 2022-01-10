import requests
import pandas as pd
from bs4 import BeautifulSoup

data3 = []
for i in range(280):
    resp = requests.get('https://www.welivesecurity.com/page/'+ str(i+1)+'/')
    # resp = requests.get('https://www.welivesecurity.com/')
    soup = BeautifulSoup(resp.text, 'html.parser')
    author = soup.select('[id="news-feed"] [class="text-wrapper col-sm-9 col-xs-8 no-padding"] span')
    print(author)
    print(len(author))
    for athr in author:
         value = athr.select('a')
         Text = ''
         for a in value:
             Text = Text + (a.getText())
         data3.append([Text])
    df = pd.DataFrame(data3)
    df.columns= ['Author']
    print(df)
    df.to_excel('Authors1.xlsx', index=False, header=True)