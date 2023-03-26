import requests
from bs4 import BeautifulSoup
import re
import pyrebase
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
import time

#config 的資料須待最終儲存位置修改
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


def getComData(comNo):
    qFinal = []
    roeFinal = []
    url = 'https://goodinfo.tw/tw/StockFinDetail.asp?RPT_CAT=XX_M_QUAR_ACC&STOCK_ID={}'.format(comNo)
    browser=webdriver.Chrome()
    browser.get(url) 
    years = ["20224", "20202",]
    for year in years:
        Select(browser.find_element(By.ID,'RPT_CAT')).select_by_value('XX_M_QUAR')
        time.sleep(6)
        Select(browser.find_element(By.ID,'QRY_TIME')).select_by_value(year)
        time.sleep(5)
        # try:
        #     # 等待當季字樣出現
        #     WebDriverWait(browser, 3, 0.1).until(
        #         expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[contains(@style, 'color:gray;font-size:9pt;') and text()='(當季)']"), "(當季)")
        #     )
           
        # except:
        #     # 處理異常
        #     # ...
        #     print("未抓取")
        #     break
        soup=BeautifulSoup(browser.page_source,"html.parser")
        try:
            main = soup.select_one('table.b1.p4_4.r0_10.row_mouse_over')
            main_str = str(main)
            pattern = re.compile(r"滑鼠在此點一下, 可顯示公式說明")
            main_list = pattern.split(main_str)
            q = main_list[0]
            roe = main_list[9]
            tempQ = q.split(r'</nobr></th>')
            tempRoe = roe.split(r'nobr>')
            q2 = []
            roe2 = []
            for i in tempQ:
                if len(i) == len(tempQ[1]):
                    q2.append(i.replace(r'<th><nobr>', ''))
            qFinal.append(q2)
            for i in tempRoe:
                if len(i) <= 9:
                    roe2.append(i.replace(r'</', ''))
            roeFinal.append(roe2[1:])
    
            time.sleep(5)
        except:
            print([comNo, year])
            continue
    return qFinal, roeFinal
        
# -----------------------------------

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
# print(colum)#產業名稱跟屬性容器

   

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

#------------------------------------------
for i in data:
    if "-KY" in i["公司名稱"]:
        continue
    else:
        period, roeVaule = getComData(int(i["股票代碼"]))
        data1 = {}
        try:
            for j in range(len(period)):
                for k in range(len(period[j])):
                    data1[str(period[j][k])] = str(roeVaule[j][k])
            data1["股票代碼"] = i
            database.child('RoeValue').push(data1)
        except:
            continue
print("上傳完畢")





    



