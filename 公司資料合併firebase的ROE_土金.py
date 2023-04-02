# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 09:41:39 2023

@author: user
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
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

# 檢查 Firebase Admin SDK 是否已經初始化
if not firebase_admin._apps:
    # 設定 Firebase Admin SDK 的認證憑證
    cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    })
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

# 取得 Firebase Realtime Database 的根節點
ref = db.reference('公司資料')
ref2 = db.reference('RoeValue累季-1')

# 讀取資料
datas = ref.get()
datas2 = ref2.get()
x = ["土", "金"]
# 一層一層抽出股票代號
for i3 in x:
    for j3 in datas[i3].keys():
        b3 = int(datas[i3][j3]['股票代碼'])
        # for i4 in ref2.values():
        if len(datas[i3][j3]) > 4:
            print(b3, "不用抓")
            continue
        else:
            for i4 in datas2.values():
                if datas[i3][j3]['股票代碼'] == i4["股票代碼"]:
                    ref = db.reference("公司資料/{}/{}".format(i3, j3))
                    if "Q" not in ref.get():
                        ref.update(i4)
                        print(datas[i3][j3]['股票代碼'])
                else:
                    data4 = {"股票代碼": b3}
                    database.child('ROE缺漏').push(data4)
                    # print(b3, "抓不到")
                    continue
                    
                    
                
