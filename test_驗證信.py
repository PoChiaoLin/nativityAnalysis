# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:36:26 2023

@author: USER
"""
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
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

if not firebase_admin._apps:
    # 設定 Firebase Admin SDK 的認證憑證
    cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    })

ref2 = db.reference('email_t')
ref = db.reference('Humandata')
    # 讀取資料
data2 = ref2.get()
data = ref.get()
user_otp = {"modelin1112@gmail": 811805, "modelin8888@gmail": 349330}
for i in data2:
    email_t = i
    for m_t in data.keys():
        if m_t == email_t:
            for d_t in data[email_t].keys():
                otp = int(data[email_t][d_t]["otp"])
                temp_otp = int(user_otp[email_t])
                if otp == temp_otp:
                    print(otp)
                    # return render(request, "birthday.html")
                else:  # 加入刪除帳戶的程式碼
                    # user.delete()
                    print("錯誤")
                    # return HttpResponse("OTP不正確，請重新輸入")
        else:
            continue
    # return HttpResponse("無效的email")