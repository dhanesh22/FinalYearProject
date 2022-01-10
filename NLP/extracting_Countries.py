import pandas as pd
import pycountry
import openpyxl
import xlsxwriter

file_path = 'Handled_Empty_Columns.xlsx'
df = pd.read_excel(file_path,engine='openpyxl')
# import pycountry


def get_country(text):
    cc = []
    for country in pycountry.countries:
        if country.name in text:
           print(cc.append(country.name))
           cc = list(set(cc))
            # print([cc])
    #
    #     if len(cc) > 0:
    #         u = cc[0]
    #         return u
    #     else:
    #         return 'null'
    # else:
    #     return 'null'


df["Country"] = df["Long_Summary"].apply(lambda text: get_country(text))
# print(df['Country'])