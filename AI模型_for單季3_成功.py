# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:23:44 2023

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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
    
        # 輸出模型係數
        print("模型係數：", model.coef_)
        print("截距：", model.intercept_)
        # 繪製模型圖表
        x_range = np.array([min(X), max(X)])
        y_range = model.predict(x_range.reshape(-1, 1))
        plt.plot(x_range, y_range, color='red')
    
        # 繪製散佈圖
        plt.scatter(X, y)
    
        # 設定圖表標題與座標軸標籤
        plt.title('Linear Regression Model')
        plt.xlabel('Quarter')
        plt.ylabel('Value')
    
        # 顯示圖表
        plt.show()
    
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

a = {'2022Q3': '0.6600000000000001', '2022Q2': '-4.130000000000001', '2022Q1': '-7.51', '2021Q4': '0.36999999999999744', '2021Q3': '37.96', '2021Q2': '-11.95', '2021Q1': '-6.66', '2020Q4': '-17.80000000000001', '2020Q3': '197.4', '2020Q2': '-191.8', '2020Q1': '-143.2', '2019Q4': '-94.21', '2019Q3': '-26.050000000000004', '2019Q2': '-17.750000000000004', '2019Q1': '-26.99', '2018Q4': '-75.05'}

nextValue = aiModel(a)