# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:02:40 2023

@author: USER
"""

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

comNo = int(input())

qFinal = []
roeFinal = []
url = 'https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID={}'.format(comNo)

browser=webdriver.Chrome()
browser.get(url)
time.sleep(6)

Select(browser.find_element(By.ID,'RPT_CAT')).select_by_value('XX_M_QUAR')

time.sleep(10)
soup = BeautifulSoup(browser.page_source,"html.parser")
try:
    main = soup.select_one('table.b1.p4_4.r0_10.row_mouse_over')
    main_str = str(main)
    pattern = re.compile(r"滑鼠在此點一下, 可顯示公式說明")
    main_list = pattern.split(main_str)
    q = main_list[0]
    tempQ = q.split(r'</nobr></th>')
    q2 = []
    for i in tempQ:
        if len(i) == len(tempQ[1]):
            q2.append(i.replace(r'<th><nobr>', ''))
    qFinal.append(q2)
    roe = main_list[9]
    if re.search("股東權益報酬率", roe):
        # print("{}股東權益報酬率".format(comNo))
        tempRoe = roe.split(r'nobr>')           
        roe2 = []
        for j in tempRoe:
            if len(j) <= 9:
                roe2.append(j.replace(r'</', ''))
        roeFinal.append(roe2[1:])
        time.sleep(5)
    else:
        print("{}無股東權益報酬率".format(comNo))
        for k in range(len(qFinal)):
            roeFinal.append("-")
except:
    print("{}的資料異常".format(comNo))
