import requests
from bs4 import BeautifulSoup
import re
import pyrebase
import pandas as pd
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
import time
import threading

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
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # 啟用隱藏模式
    options.add_argument('--disable-gpu') # 禁用 GPU
    options.add_argument('--no-sandbox') # 在 Docker 中運行 Chrome 時需要加上此參數
    options.add_argument('--disable-dev-shm-usage') # 在 Docker 中運行 Chrome 時需要加上此參數
    browser = webdriver.Chrome(options=options)
 
    browser.get(url)
        
    time.sleep(8)
    # 找到下拉式選單元素
    try:
        select_element = browser.find_element(By.ID, "QRY_TIME")
    except:
        print("{}網頁異常".format(comNo))
        database.child("網頁異常").push(comNo)
        return
    # 創建 Select 物件
    select = Select(select_element)
    # 取得下拉式選單中所有的選項值
    options = [option.get_attribute("value") for option in select.options]

    for a in range ((len(options) // 10)+1):
        Select(browser.find_element(By.ID,'QRY_TIME')).select_by_value(options[a])
        time.sleep(20)
        try:
            soup = BeautifulSoup(browser.page_source,"html.parser")
        except:
            print("{}網頁異常".format(comNo))
            database.child("網頁異常2").push(comNo)
            return qFinal, roeFinal
        try:
            main = soup.select_one("table.b1.p4_4.r0_10.row_mouse_over")
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
            try:
                if re.search("股東權益報酬率", roe):
                    # print("{}股東權益報酬率".format(comNo))
                    tempRoe = roe.split(r'nobr>')           
                    roe2 = []
                    for j in tempRoe:
                        if len(j) <= 9:
                            roe2.append(j.replace(r'</', ''))
                    roeFinal.append(roe2[1:])
                else:
                    print("{}無股東權益報酬率".format(comNo))
                    for k in range(len(qFinal)):
                        roeFinal.append("-")
            except:
                print("{}ROE異常".format(comNo))
        except:
            print("{}的資料異常".format(comNo))
        
        time.sleep(7)
    return qFinal, roeFinal
def rorToCom(data, roedata):
    try:
        for i3 in data.keys():
            for j3 in datas[i3].keys():            
                b3 = int(datas[i3][j3]['股票代碼'])
                # for i4 in ref2.values():
                if len(datas[i3][j3]) > 4:
                    print(b3, "不用抓")
                    continue
                else:
                    if datas[i3][j3]['股票代碼'] == roedata["股票代碼"]:
                        ref = db.reference("公司資料/{}/{}".format(i3, j3))
                        if "Q" not in ref.get():
                            ref.update(roedata)
                            print(datas[i3][j3]['股票代碼'])
                    else:
                        data4 = {"股票代碼": b3}
                        database.child('ROE缺漏2').push(data4)
                        # print(b3, "抓不到")
                        continue
        return
    except:
        print(roedata["股票代碼"], "rorToCom執行失敗")
        return

      

if not firebase_admin._apps:
    # 設定 Firebase Admin SDK 的認證憑證
    cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    })

ref = db.reference('ROE缺漏')
ref2 = db.reference('公司資料')
datas = ref.get()
datas2 = ref2.get()
a = []
count = 0
for i in datas.keys():
    a.append(datas[i]["股票代碼"])  
b = set(a)
c = list(b)

for z in c[0: 100]:
    period, roeVaule = getComData(int(z))
    data1 = {}
    data1["股票代碼"] = z
    try:
        for y in range(len(period)):
            if len(period[y]) == len(roeVaule[y]):
                for x in range(len(period[y])):
                    data1[str(period[y][x])] = str(roeVaule[y][x])
            else:
                print("{}資料不匹配".format(z))
        database.child('RoeValue累季-2').push(data1)
        rorToCom(datas2, data1)
    except:
        print("{}未成功上傳".format(z) )
        continue
print("上傳完畢")






    



