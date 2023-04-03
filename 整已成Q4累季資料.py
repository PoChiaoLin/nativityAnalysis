# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:02:43 2023

@author: user
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# # 檢查 Firebase Admin SDK 是否已經初始化
# if not firebase_admin._apps:
#     # 設定 Firebase Admin SDK 的認證憑證
#     cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
#     firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
#     })

def roeDataSortOut(datas): #整理ROE資料
    newDatas = {}
    newDatasQ4 = {}
    j =[]
    for k in datas.keys():
        j.append(k)
    sorted(j)
    j.reverse()    
    for l in j:        
        if l == '股票代碼':
            n = 0
            newDatas[datas[l]] = {}
            newDatasQ4[datas[l]] = {}
            n = datas[l]
        elif "Q4" in l:
            if len(datas[l]) > 2:
                newDatas[n][l] = datas[l]
                newDatasQ4[n][l] = datas[l]
        else:
            if len(datas[l]) > 2:
                newDatas[n][l] = datas[l]
    return newDatas, newDatasQ4
    # print(newDatas)
    # print(newDatasQ4)

# # 讀取資料
# ref = db.reference('RoeValue累季')
# datas = ref.get()
#測試用datas
datas =  {'-NRaNeqJxyftzsjv5NTl': {'2018Q4': '-75.05', '2019Q1': '-26.99', '2019Q2': '-44.74', '2019Q3': '-70.79', '2019Q4': '-165', '2020Q1': '-143.2', '2020Q2': '-335', '2020Q3': '-137.6', '2020Q4': '-155.4', '2021Q1': '-6.66', '2021Q2': '-18.61', '2021Q3': '19.35', '2021Q4': '19.72', '2022Q1': '-7.51', '2022Q2': '-11.64', '2022Q3': '-10.98', '股票代碼': '3085'},'-NRaNeqJxyftzsjv5NTk': {'2018Q4': '-75.05', '2019Q1': '-', '2019Q2': '-44.74', '2019Q3': '-70.79', '2019Q4': '_', '2020Q1': '-143.2', '2020Q2': '-335', '2020Q3': '-137.6', '2020Q4': '-155.4', '2021Q1': '-6.66', '2021Q2': '-18.61', '2021Q3': '19.35', '2021Q4': '19.72', '2022Q1': '-7.51', '2022Q2': '-11.64', '2022Q3': '-10.98', '股票代碼': '3086'}}

a = []
b = []
for i in datas.values():
    newDatas, newDatasQ4 = roeDataSortOut(i)
    a.append(newDatas)
    b.append(newDatasQ4)
print(a)
print(b)


        










