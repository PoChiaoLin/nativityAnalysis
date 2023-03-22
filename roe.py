# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:02:40 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import re

myHeaders = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

r = requests.get('https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=2330',headers = myHeaders)
r.encoding = 'utf-8'
if r.status_code == 200:
    print(r.text)
    
    soup = BeautifulSoup(r.text,'html.parser')
    # print(type(soup))
    # titles = soup.select('table#tblFinDetail nobr')
    titles = soup.select_one('div#txtFinBody')
    print(titles)
    # print(type(titles))
    for title in titles:
        print(title.text)
    
    # import pandas as pd
    # dfs = pd.read_html(titles.prettify())
    # df = dfs[0]
    # print(df)
        
    # titles2 = soup.find_all('tr',class_='bg_h1')
    # for title in titles2:
    #     print(title.text)
        
        
        
        
        
#     __VIEWSTATEGENERATOR = soup.select_one('input#__VIEWSTATEGENERATOR').get('value')
#     __EVENTVALIDATION = soup.select_one('input#__EVENTVALIDATION').get('value')
#     __VIEWSTATE = soup.select_one('input#__VIEWSTATE').get('value')

# for year in range(103,113):
#     for month in range(1, 13):

#         myData = {'__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
#                   '__EVENTVALIDATION': __EVENTVALIDATION,
#                   '__VIEWSTATE':__VIEWSTATE,
#                   '__VIEWSTATEENCRYPTED':'',
#                   '__EVENTTARGET':'',
#                   '__EVENTARGUMENT':'',
#                   '__LASTFOCUS':'',   
#                     'forma': '請選擇遊戲',
#                   'SuperLotto638Control_history1$chk': 'radYM',
#                   'SuperLotto638Control_history1$dropYear': year,
#                   'SuperLotto638Control_history1$dropMonth': month,
#                   'SuperLotto638Control_history1$btnSubmit': '查詢'}
        
        
#         r = requests.post('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx',headers = myHeaders, data = myData)
#         r.encoding = 'utf-8'
#         if r.status_code == 200:
#             # print(r.text)
                     
#             soup = BeautifulSoup(r.text,'html.parser')
#             num =  soup.find_all('span',id=re.compile('SuperLotto638Control_history1_dlQuery_DrawTerm_\d'))
#             number = soup.find_all('span',id=re.compile('SuperLotto638Control_history1_dlQuery_SNo\d_\d'))
            
#             for index,n1 in enumerate(number):
#                 if (index) % 7 == 0:
#                     print(num[index//7].text+":",end=' ')
#                 print(n1.text,end=' ')
#                 if (index+1) % 7 == 0:
#                     print()