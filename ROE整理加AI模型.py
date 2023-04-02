# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 09:02:43 2023

@author: user
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pyrebase

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
            # print(x2,y2)
            continue
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
    # print(newDatas.values())
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
    return avgRoeTemp, roeTemp1[0]

def aiModel(a):
    # 將字典轉換為list
    values = list(map(float, a.values()))
    
    # 計算四分位距
    Q1 = np.percentile(values, 25)
    Q3 = np.percentile(values, 75)
    IQR = Q3 - Q1
    
    # 計算上下限
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    
    # # 繪製箱形圖
    # plt.boxplot(values)
    # plt.show()
    
    # 將離群值從原始資料中移除
    values_no_outliers = [value for value in values if value <= upper_bound and value >= lower_bound]
    
    # 確認是否有非離群值
    if len(values_no_outliers) == 0:
        print("資料集中沒有非離群值")
    else:
        # 建立X、y資料集
        quarters = list(a.keys())
        X = [i for i in range(len(quarters)) if float(a[quarters[i]]) in values_no_outliers]
        y = [float(a[quarters[i]]) for i in X]
    
        # 建立線性回歸模型
        model = LinearRegression()
        model.fit(np.array(X).reshape(-1, 1), np.array(y))
    
        # # 輸出模型係數
        # print("模型係數：", model.coef_)
        # print("截距：", model.intercept_)
        # # 繪製模型圖表
        # x_range = np.array([min(X), max(X)])
        # y_range = model.predict(x_range.reshape(-1, 1))
        # plt.plot(x_range, y_range, color='red')
    
        # # 繪製散佈圖
        # plt.scatter(X, y)
    
        # # 設定圖表標題與座標軸標籤
        # plt.title('Linear Regression Model')
        # plt.xlabel('Quarter')
        # plt.ylabel('Value')
    
        # # 顯示圖表
        # plt.show()
    
    # 預測下一個季度的值
    next_quarter = len(quarters)
    next_value = model.predict([[next_quarter]])[0]
    print("預測值為：{:.2f}".format(next_value))
    
    # 將預測值加入原本的資料集中
    a[f"{next_quarter}"] = str(next_value)
    
    # 重新取出資料集中的值
    values = list(map(float, a.values()))
    
    # 計算四分位距
    Q1 = np.percentile(values, 25)
    Q3 = np.percentile(values, 75)
    IQR = Q3 - Q1
    
    # 計算上下限
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    
    # 判斷是否為離群值
    outliers = [value for value in values if value > upper_bound or value < lower_bound]
    
    # 印出離群值
    # print("離群值：", outliers)
    
    # 計算成功率
    success_rate = (len(values) - len(outliers)) / len(values) * 100
    print("成功率：", "{:.2f}".format(success_rate)+"%")
    return next_value

# # 讀取資料---------------------------------------------------------------
# ref = db.reference('公司資料')
# datas = ref.get()

#測試用datas
datas =  {"土":{'-NRaNeqJxyftzsjv5NTl': {'2018Q4': '-75.05', '2019Q1': '-26.99', '2019Q2': '-44.74', '2019Q3': '-70.79', '2019Q4': '-165', '2020Q1': '-143.2', '2020Q2': '-335', '2020Q3': '-137.6', '2020Q4': '-155.4', '2021Q1': '-6.66', '2021Q2': '-18.61', '2021Q3': '19.35', '2021Q4': '19.72', '2022Q1': '-7.51', '2022Q2': '-11.64', '2022Q3': '-10.98', '股票代碼': '3085'}}}

# a = []
# b = []
for i3 in datas.keys():
    for j3 in datas[i3].keys():
        i = int(datas[i3][j3])
        roeS = roeSvalue(i)
        newDatas, newDatasQ4 = roeDataSortOut(roeS)
        dataDict = {"股票代碼": datas[i3][j3]["股票代碼"],
                    "公司名稱": datas[i3][j3]["公司名稱"],
                    "所屬產業": datas[i3][j3]["所屬產業"],
                    "屬性": i3,
                    "New_ROE": "",
                    "Next_ROE": "",
                    "statuses": "",}
        avgRoe, roeNew = roeAVG(newDatas) #ROE中位數平均值, 最新的ROE值
        dataDict["New_ROE"] = roeNew
        if roeNew < avgRoe:
            dataDict["statuses"] = "差於中位數平均值"
        else:
            dataDict["statuses"] = "優於中位數平均值"
        for temp1 in newDatas.values(): 
            nextValue = aiModel(temp1) # ROE預測值
            dataDict["Next_ROE"] = nextValue
        database.child('完整公司資料').push(dataDict)
    
    # a.append(newDatas)
    # b.append(newDatasQ4)



        










