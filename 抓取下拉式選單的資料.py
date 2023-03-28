# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 09:26:43 2023

@author: user
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 初始化 webdriver
browser = webdriver.Chrome()

# 打開網頁
browser.get("https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID=2330")

# 找到下拉式選單元素
select_element = browser.find_element(By.ID, "QRY_TIME")

# 創建 Select 物件
select = Select(select_element)

# 取得下拉式選單中所有的選項值
options = [option.get_attribute("value") for option in select.options]

a = (len(options) // 10)+1


# 關閉瀏覽器
browser.quit()

