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

session = requests.session()
myHeaders = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

url = 'https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=2330'
browser=webdriver.Chrome()
browser.get(url) 

Select(browser.find_element(By.ID,'RPT_CAT')).select_by_value('XX_M_QUAR')
Select(browser.find_element(By.ID,'QRY_TIME')).select_by_value('20224')

time.sleep(5)
element = WebDriverWait(browser, 3, 0.1).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, 'b1.p4_4.r0_10.row_mouse_over'))
)
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
for i in tempRoe:
    if len(i) <= len(tempRoe[3]):
        roe2.append(i.replace(r'</', ''))
roeFinal = roe2[1:]

time.sleep(2)

Select(browser.find_element(By.ID,'QRY_TIME')).select_by_value('20224')

time.sleep(5)
element = WebDriverWait(browser, 3, 0.1).until(
    expected_conditions.presence_of_element_located((By.CLASS_NAME, 'b1.p4_4.r0_10.row_mouse_over'))
)
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
for i in tempRoe:
    if len(i) <= len(tempRoe[3]):
        roe2.append(i.replace(r'</', ''))
roeFinal = roe2[1:]

