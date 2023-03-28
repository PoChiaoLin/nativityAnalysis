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
options = webdriver.ChromeOptions()
options.add_argument('--headless') # 啟用隱藏模式
options.add_argument('--disable-gpu') # 禁用 GPU
options.add_argument('--no-sandbox') # 在 Docker 中運行 Chrome 時需要加上此參數
options.add_argument('--disable-dev-shm-usage') # 在 Docker 中運行 Chrome 時需要加上此參數
browser = webdriver.Chrome(options=options)
browser.get(url)
time.sleep(15)
# 找到下拉式選單元素
select_element = browser.find_element(By.ID, "QRY_TIME")

# 創建 Select 物件
select = Select(select_element)
# 取得下拉式選單中所有的選項值
options = [option.get_attribute("value") for option in select.options]

for a in range ((len(options) // 10)+1):
    Select(browser.find_element(By.ID,'QRY_TIME')).select_by_value(options[a])
    time.sleep(30)
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
        print(roe)
        try:
            if re.search("股東權益報酬率", roe):
                # print("{}股東權益報酬率".format(comNo))
                tempRoe = roe.split(r'nobr>')
                print(tempRoe)
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
            print("{}ROE異常".format(comNo))
    except:
        print("{}的資料異常".format(comNo))
    
    time.sleep(15)
