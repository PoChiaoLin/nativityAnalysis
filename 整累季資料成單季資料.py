# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:02:43 2023

@author: user
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# 檢查 Firebase Admin SDK 是否已經初始化
# if not firebase_admin._apps:
#     # 設定 Firebase Admin SDK 的認證憑證
#     cred = credentials.Certificate("test1-bfab0-firebase-adminsdk-1gtyi-b1c5698522.json")
#     firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://test1-bfab0-default-rtdb.firebaseio.com/'
    # })
def roeSvalue(dict_temp): #轉換成單季
    dict_temp_new = {}
    o = ""
    p = 0
    for x2, y2 in dict_temp.items():
        if "Q" in x2 and len(y2) > 2:
            z2 = x2.split("Q")
            if z2[0] == o:
                dict_temp_new[x2] = str(eval(y2) - p)
                p = eval(y2)
            elif z2[0] != o:
                o = z2[0]
                p = 0
                dict_temp_new[x2] = str(eval(y2) - p)
                p = eval(y2)
            else:
                print(x2)
        elif "Q" in x2:
            print(x2,y2)
        elif "股票代碼" == x2:
            dict_temp_new[x2] = y2
    # print(dict_temp_new)
    return dict_temp_new
            
        
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
    # print(newDatas[n].values())
    return newDatas, newDatasQ4
    # print(newDatas)
    # print(newDatasQ4)
def roeAVG(newDatas):
    roeTemp1 = []  
    for s in newDatas.values():   
        for t in s.values():
            roeTemp1.append(eval(t))
    roeTemp = sorted(roeTemp1)
    if len(roeTemp) % 2 == 0:
        v = len(roeTemp) // 2
        if v < 2:            
            avgRoeTemp = sum(roeTemp[:])/len(roeTemp[:])
        else:
            avgRoeTemp = sum(roeTemp[v-2:v+2])/len(roeTemp[v-2:v+2])
    else:
        v = len(roeTemp) // 2
        if v < 1:
            avgRoeTemp = sum(roeTemp[:])/len(roeTemp[:])
        else:
            avgRoeTemp = sum(roeTemp[v-1:v+2])/len(roeTemp[v-1:v+2])
    # print(avgRoeTemp)
    return avgRoeTemp

    

# # 讀取資料
# ref = db.reference('RoeValue累季')
# datas = ref.get()
#測試用datas
datas =  {'-NRaNeqJxyftzsjv5NTl': {'2018Q4': '-75.05', '2019Q1': '-26.99', '2019Q2': '-44.74', '2019Q3': '-70.79', '2019Q4': '-165', '2020Q1': '-143.2', '2020Q2': '-335', '2020Q3': '-137.6', '2020Q4': '-155.4', '2021Q1': '-6.66', '2021Q2': '-18.61', '2021Q3': '19.35', '2021Q4': '19.72', '2022Q1': '-7.51', '2022Q2': '-11.64', '2022Q3': '-10.98', '股票代碼': '3085'}}

a = []
b = []
for i in datas.values():
    roeS = roeSvalue(i)
    newDatas, newDatasQ4 = roeDataSortOut(roeS)
    avgRoe = roeAVG(newDatas)
    a.append(newDatas)
    b.append(newDatasQ4)



        










