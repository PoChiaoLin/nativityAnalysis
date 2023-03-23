# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:02:40 2023

@author: USER
"""

from bs4 import BeautifulSoup
import re
import pyrebase
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
import time

#config 的資料須待最終儲存位置修改
config = {
  'apiKey': "AIzaSyCE-vHKK0MNrCcy-KAtK__0HW9hrRXM_M4",
  'authDomain': "test1-bfab0.firebaseapp.com",
  'projectId': "test1-bfab0",
  'storageBucket': "test1-bfab0.appspot.com",
  'messagingSenderId': "863152004967",
  'appId': "1:863152004967:web:85cd44c032569b84d799c2",
  'measurementId': "G-8ED4G9L00T",
  #URL 路徑為資料庫網址
  'databaseURL': "https://test1-bfab0-default-rtdb.firebaseio.com",}

firebase = pyrebase.initialize_app(config)

database = firebase.database()


def getComData(comNo):
    qFinal = []
    roeFinal = []
    url = 'https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID={}'.format(comNo)
    browser=webdriver.Chrome()
    browser.get(url) 
    years = ["20224", "20202", "20174", "201502"]
    for year in years:
        Select(browser.find_element(By.ID,'RPT_CAT')).select_by_value('XX_M_QUAR')
        Select(browser.find_element(By.ID,'QRY_TIME')).select_by_value(year)
        time.sleep(5)
        try:
            # 等待當季字樣出現
            WebDriverWait(browser, 3, 0.1).until(
                expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[contains(@style, 'color:gray;font-size:9pt;') and text()='(當季)']"), "(當季)")
            )
           
        except:
            # 處理異常
            # ...
            print("未抓取")
            break
        soup=BeautifulSoup(browser.page_source,"html.parser")

        main = soup.select_one('table.b1.p4_4.r0_10.row_mouse_over')
        main_str = str(main)
        pattern = re.compile(r"滑鼠在此點一下, 可顯示公式說明")
        main_list = pattern.split(main_str)
        q = main_list[0]
        roe = main_list[9]
        tempQ = q.split(r'</nobr></th>')
        tempRoe = roe.split(r'nobr>')
        q2 = []
        roe2 = []
        for i in tempQ:
            if len(i) == len(tempQ[1]):
                q2.append(i.replace(r'<th><nobr>', ''))
        qFinal.append(q2)
        for i in tempRoe:
            if len(i) <= len(tempRoe[3]):
                roe2.append(i.replace(r'</', ''))
        roeFinal.append(roe2[1:])

        time.sleep(2)
    return qFinal, roeFinal
        
# -----------------------------------

for i in range(2330, 2332):
    period, roeVaule = getComData(i)
    data1 = dict(zip(period, roeVaule))
    data1["stockcode"] = i
    database.child('RoeValue').push(data1)



    



