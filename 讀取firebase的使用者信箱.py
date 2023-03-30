# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:02:43 2023

@author: user
"""        
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

# 檢查 Firebase Admin SDK 是否已經初始化
if not firebase_admin._apps:
    # 設定 Firebase Admin SDK 的認證憑證
    cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    })

# 取得Firebase Authentication的使用者ID
user_id = "user-id"
user = auth.get_user(user_id)

# 取得使用者的email
email = user.email
print(email)








