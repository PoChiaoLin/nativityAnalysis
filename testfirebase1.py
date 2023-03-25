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

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")

# check if default app has already been initialized
if not firebase_admin._apps:
    default_app = firebase_admin.initialize_app(cred, name='myApp1', options={
        'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    })
else:
    # if default app has been initialized, initialize a new app with a unique name
    firebase_admin.initialize_app(cred, name='myApp2', options={
        'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    })

# get database reference from the default app
ref = db.reference('/')
data = ref.get()

print(data)




