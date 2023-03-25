import requests
from bs4 import BeautifulSoup

t_list = []#產業類別容器
linkData = []#連結容器

#第一步請求url
#並產生 產業類別容器
resp = requests.get("https://statementdog.com/taiex")
soup = BeautifulSoup(resp.text,"lxml")
titles= soup.find_all('h2',class_ = 'industry-item-title')
#print(titles)測試
for title in titles:
    t_list.append(title.text)

#第2步產生連結容器    
links = soup.find("div",class_="industries-list").find_all("a")
for link in links:
    linkData.append("https://statementdog.com/"+link.get("href"))



#print(linkData)
resp2_1 = requests.get(linkData[0]) 
#print(resp2_1)
soup2_1 = BeautifulSoup(resp2_1.text,"lxml")   
#print(soup2_1)

    
colum = soup2_1.find("div",class_="industry-ranking-list-header").text.replace("\n",",").strip(",").split(",")    

del colum[2:4]
colum[0] = "股票代碼"
print(colum)#產業名稱跟屬性容器

   

#第3部 產生 綜合容器
colums = {}
for d1 in colum:
    colums[d1]=[]
colums


#第四部 上帝創造一切

for t, url in zip(t_list, linkData):
    resp2 = requests.get(url)
    soup2 = BeautifulSoup(resp2.text, "lxml")

    uls = soup2.find("div", class_="industry-ranking-list-body").find_all("ul")
    for ul in uls:
        li1 = ul.find_all("li")[1].text.strip().split(" ")
        li2 = ul.find_all("li")[4].text
        colums['股票代碼'].append(li1[0])
        colums['公司名稱'].append(li1[1])
        colums['所屬產業'].append(t+"_"+li2) 
      
import pandas as pd

df = pd.DataFrame(colums)
data = df.to_dict(orient='records')

df2 = pd.read_excel('產業分類.xlsx')
data2 = df2.to_dict(orient='records')

data3 = []
for dict_a in data:
    if "-KY" in dict_a["公司名稱"]:
        continue
    else:
        for dict_b in data2:
            if dict_a['所屬產業'] == dict_b['所屬產業']:
                dict_a['godOfJoy'] = dict_b['godOfJoy']
                data3.append(dict_a)
                break

import pyrebase

config = {
  'apiKey': "AIzaSyCE-vHKK0MNrCcy-KAtK__0HW9hrRXM_M4",
  'authDomain': "test1-bfab0.firebaseapp.com",
  'projectId': "test1-bfab0",
  'storageBucket': "test1-bfab0.appspot.com",
  'messagingSenderId': "863152004967",
  'appId': "1:863152004967:web:85cd44c032569b84d799c2",
  'measurementId': "G-8ED4G9L00T",
  'databaseURL': "https://test1-bfab0-default-rtdb.firebaseio.com",}

firebase = pyrebase.initialize_app(config)

database = firebase.database()

for dict_c in data3:
    for i in dict_c["godOfJoy"].split(","):
        if i == "金" :
            database.child('公司資料').child("金").push(dict_c)
        elif i == "木" :
            database.child('公司資料').child("木").push(dict_c)
        elif i == "水" :
            database.child('公司資料').child("水").push(dict_c)
        elif i == "火" :
            database.child('公司資料').child("火").push(dict_c)
        elif i == "土" :
            database.child('公司資料').child("土").push(dict_c)
        else:
            print(i)
            print("無匹配")






    

