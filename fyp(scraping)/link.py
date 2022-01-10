from bs4 import BeautifulSoup
import requests
import pandas as pd

All_links =[]
for i in range(280):
    url = 'https://www.welivesecurity.com/page/' + str(i + 1) + '/'

# url = 'https://www.welivesecurity.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    # print("The href links are :")
    resp1 = soup.select('[class="text-wrapper col-sm-9 col-xs-8 no-padding"] h2 a', href=True)
    print(len(resp1))
    # print(resp1)
    for link in resp1:
        links =link.get('href')
        print(links)
        All_links.append([links])
    df = pd.DataFrame(All_links)
    print(df)
    df.columns = ['Href']
    df.to_excel('Articles_Links.xlsx', index=False, header=True)