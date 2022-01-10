# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
#
# summary=''
# data = []
# Full_summary = []
# for i in range(280):
#     url = 'https://www.welivesecurity.com/page/' + str(i + 1) + '/'
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, "html.parser")
#     resp1 = soup.select('[class="text-wrapper col-sm-9 col-xs-8 no-padding"] h2 a', href=True)
#     for link in resp1:
#         links =link.get('href')
#         req1 = requests.get(links)
#         soup1 = BeautifulSoup(req1.text,"html.parser")
#         resp2= soup1.select('[class="main"]')
#         for long_summary in resp2:
#             summary = long_summary.find_all('p')
#             Text=''
#             for p in summary:
#                 Text=Text +(p.getText())
#             if len(Text) == 0:
#                 Full_summary.append("NULL")
#             else:
#                 Full_summary.append([Text])
#         df = pd.DataFrame(Full_summary)
#         print(df)
#         df.columns = ['Long_Summary']
#         df.to_excel('long_Summary.xlsx', index=False, header=True)

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
#
# summary=''
# data = []
# Full_summary = []
# for i in range(280):
#     url = 'https://www.welivesecurity.com/page/' + str(i + 1) + '/'
#     # url = 'https://www.welivesecurity.com/'
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, "html.parser")
#     # print("The href links are :")
#     resp1 = soup.select('[class="text-wrapper col-sm-9 col-xs-8 no-padding"] h2 a', href=True)
#     #print(len(resp1))
#     # print(resp1)
#     for link in resp1:
#         links =link.get('href')
#         # print(links)
#         req1 = requests.get(links)
#         soup1 = BeautifulSoup(req1.text,"html.parser")
#         resp2= soup1.select('[class="main"]')
#         for long_summary in resp2:
#             summary = long_summary.find_all('p')
#             Text=''
#             for p in summary:
#                 Text=Text +(p.getText())
#             # if len(Text) == 0:
#             #     Full_summary.append(" ")
#             # else:
#             Full_summary.append([Text])
#         df = pd.DataFrame(Full_summary)
#         print(df)
#         df.columns = ['Long_Summary']
#         df.to_excel('Full_Summaryy.xlsx', index=False, header=True)


from bs4 import BeautifulSoup
import requests
import pandas as pd
# from pandas import
import xlsxwriter
summary=''
data = []
Full_summary = []
for i in range(280):
    url = 'https://www.welivesecurity.com/page/' + str(i + 1) + '/'
    # url = 'https://www.welivesecurity.com/'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    # print("The href links are :")
    resp1 = soup.select('[class="text-wrapper col-sm-9 col-xs-8 no-padding"] h2 a', href=True)
    #print(len(resp1))
    # print(resp1)
    for link in resp1:
        links =link.get('href')
        # print(links)
        req1 = requests.get(links)
        soup1 = BeautifulSoup(req1.text,"html.parser")
        resp2= soup1.select('[class="main"]')
        for long_summary in resp2:
            summary = long_summary.find_all('p')
            Text=''
            for p in summary:
                Text=Text +(p.getText())
            # if len(Text) == 0:
            #     Full_summary.append(" ")
            # else:
            Full_summary.append([Text])
        df = pd.DataFrame(Full_summary)
        print(df)
        df.columns = ['Long_Summary']
        df.to_excel('Full_Summary123.xlsx',engine='xlsxwriter', index=False, header=True)