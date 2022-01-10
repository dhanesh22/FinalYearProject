import requests
import pandas as pd
from bs4 import BeautifulSoup

# GETTING DATE AND TIME OF NEWS POSTED
data2 =[]
    # pd.read_excel('Date-Time.xlsx').values.tolist()
for i in range(280):
    resp = requests.get('https://www.welivesecurity.com/page/'+ str(i+1)+'/')
    soup = BeautifulSoup(resp.text, 'html.parser')
    DateTime = soup.select('[id="news-feed"] time')
    # print(len(Category))
    # print(len(ShortSummary))
    len(DateTime)
    for Dtime in DateTime:
        GetDateTime = Dtime.getText()
        if  len(GetDateTime)==0:
            data2.append("none")
        else:
            data2.append([GetDateTime])
    df = pd.DataFrame(data2)
    df.columns= ['DateTime']
    print(df)
    df.to_excel('dateTime.xlsx', index=False, header = True)