# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:02:43 2023

@author: user
"""
#測試成功的讀取程式:         
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 檢查 Firebase Admin SDK 是否已經初始化
if not firebase_admin._apps:
    # 設定 Firebase Admin SDK 的認證憑證
    cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    })

# 取得 Firebase Realtime Database 的根節點
ref = db.reference('公司資料')
ref2 = db.reference('RoeValue累季-1')

# 讀取資料
datas = ref.get()

# 一層一層抽出股票代號
for i3 in datas.values():
    # for j3 in i3.values():
    for j3, test1 in zip(i3.values(), range(1)):
        b3 = j3['股票代碼']
        print(b3)
        # for i4 in ref2.values():
        for i4, test2 in zip(i3.values(), range(1)):
            b4 = ["股票代碼"]
            # if j3['股票代碼'] == i4["股票代碼"]:
                









