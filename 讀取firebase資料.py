# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:02:43 2023

@author: user
"""
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# if not firebase_admin._apps:
#     cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
#     default_app = firebase_admin.initialize_app(cred)


# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json") #取得金鑰
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/' #專案網址
# })

# # 確保 Firebase SDK 已經初始化後，再取得 database reference
# ref = db.reference('公司資料')
# data = ref.get()

# print(data.key)

#------------------------------------------------

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# if not firebase_admin._apps:
#     cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
#     default_app = firebase_admin.initialize_app(cred)


# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json") #取得金鑰
# firebase_admin.initialize_app(cred, name='myApp', options={
#     'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
# })

# # 確保 Firebase SDK 已經初始化後，再取得 database reference
# ref = db.reference('公司資料')
# data = ref.get()

# print(data.key)

#------------------------------------------------

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# if not firebase_admin._apps:
#     cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
#     default_app = firebase_admin.initialize_app(cred)


# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json") #取得金鑰
# options = {
#     'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/' #專案網址
# }
# firebase_admin.initialize_app(cred, name='myApp', options=options)

# # 確保 Firebase SDK 已經初始化後，再取得 database reference
# ref = db.reference('公司資料')
# data = ref.get()

# print(data.key)

#------------------------------------------------

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")

# # check if default app has already been initialized
# if not firebase_admin._apps:
#     default_app = firebase_admin.initialize_app(cred, name='myApp1', options={
#         'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
#     })
# else:
#     # if default app has been initialized, initialize a new app with a unique name
#     firebase_admin.initialize_app(cred, name='myApp2', options={
#         'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
#     })

# # get database reference from the default app
# ref = db.reference('公司資料')
# data = ref.get()

# print(data.key)

#------------------------------------------------

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
# if not firebase_admin._apps:
#     firebase_admin.initialize_app(cred)


# # check if default app has already been initialized
# if not firebase_admin._apps:
#     default_app = firebase_admin.initialize_app(cred, name='myApp1', options={
#         'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
#     })
# else:
#     # if default app has been initialized, initialize a new app with a unique name
#     firebase_admin.initialize_app(cred, name='myApp2', options={
#         'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
#     })

# # get database reference from the default app
# ref = db.reference('/')
# data = ref.get()

# for i in data.keys():
#     print(i)
#     for j in i.keys():
#         print(j)
#         for k in j.items():
#             print(k)
 
#------------------------------------------------

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
# firebase_admin.initialize_app(cred, {
#      'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
# })


# # check if default app has already been initialized
# try:
#     default_app = firebase_admin.get_app()
# except ValueError:
#     default_app = firebase_admin.initialize_app(cred)

# # get database reference from the default app
# ref = db.reference('/')
# data = ref.get()

# for i in data.keys():
#     print(i)
#     for j in i.keys():
#         print(j)
#         for k in j.items():
#             print(k)

#------------------------------------------------
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db


# try:
#     default_app = firebase_admin.get_app()
# except ValueError:
#     cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
#     firebase_admin.initialize_app(cred, {
#          'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
#     })
#     default_app = firebase_admin.get_app()
# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'ttps://test1-bfab0-default-rtdb.firebaseio.com/'})
    
# # get database reference from the default app
# ref = db.reference('公司資料')
# data = ref.get()

# for i in data.keys():
#     print(i)
#     for j in i.keys():
#         print(j)
#         for k in j.items():
#             print(k)

#-------
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db

# # 設定 Firebase Admin SDK 的認證憑證
# cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
# })

# # 取得 Firebase Realtime Database 的根節點
# ref = db.reference('公司資料')

# # 讀取資料
# data = ref.get()

# # 輸出資料
# for i in data.keys():
#     print(data[i])
#     a = data[i]
#     for j in data[i].keys():
#         print(a[j])
#         b = a[j]
#         for k, l in b.items():
#             print([k, l])
#--------------------------------------------- 
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

# 讀取資料
data = ref.get()

# 輸出資料
for i in data.keys():
    print(data[i])
    a = data[i]
    for j in data[i].keys():
        print(a[j])
        b = a[j]
        for k, l in b.items():
            print([k, l])
            
#-------------------------------------
#配合爬蟲帶入股票代號的程式:
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

# 讀取資料
data = ref.get()

# 一層一層抽出股票代號
for i in data.keys():
    a = data[i]
    for j in data[i].keys():
        b = a[j] # b['股票代碼']即可得到股票號碼









