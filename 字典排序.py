# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
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
data = ref.get()

# 一層一層抽出股票代號
for i, j in zip(range(1), data.keys()):
    k = []
    for l in data[j].keys():
        k.append(l)
    print(k)
    sorted(k)
    k.reverse()
    print(k)
    print(data[j].keys())

        