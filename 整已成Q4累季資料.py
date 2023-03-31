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
ref = db.reference('RoeValue累季')

# 讀取資料
datas = ref.get()
newDatas = {}
# 重組個股票代號的Q4 list:
for i, z in zip(datas.keys(), range(2)):
# for i in datas.keys():
    j = []
    for k in datas[i].keys():
        j.append(k)
    sorted(j)
    j.reverse()    
    for l in j:        
        if l == '股票代碼':
            n = 0
            newDatas[datas[i][l]] = {}
            n = datas[i][l]
        elif "Q4" in l:
            c = datas[i][l]
            if eval(datas[i][l]):
                newDatas[n][l] = datas[i][l]
for i in newDatas.keys():
    if len(newDatas[i]) >= 3:
        










