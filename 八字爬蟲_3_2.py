# import sqlite3
import re
import requests
from bs4 import BeautifulSoup
import pyrebase

# # 連接到資料庫，如果不存在就會建立一個新的
# conn = sqlite3.connect('horoscopedatabase.db')

# 建立資料表，不存在需要建立
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE horoscopetable (dataIndex TEXT, horoscope TEXT, nativityAnalysis TEXT, godOfJoy TEXT)')

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
#
# database.child('nativitydata')

session = requests.session()
myHeaders = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
sexAll = ["M", "F"]
earthAll = ["N", "S"]

for year in range(2023-54, 2023+1):
    for month in range(1, 13):
        for day in range(1, 32):
            for hour in range(0, 24):
                for sex in sexAll:
                    for earth in earthAll:
                        payload1 = {
                            "_Year": str(year),
                            "_Month": str(month),
                            "_Day": str(day),
                            "_Hour": str(hour),
                            "_sex": sex,
                            "_earth": earth,
                            "txt_eight": "",
                            "txt_twelve": "",
                            "txt_sun_date": "",
                            "txt_moon_date": "",
                            "txt_act": "",
                            "job_kind": "A1",
                        }
                        
                        a = session.post("https://www.dearmoney.com.tw/eightwords/result_eight_words_page", data=payload1, headers=myHeaders)
                        a.encoding = 'utf-8'
                        soup1 = BeautifulSoup(a.text, 'html.parser')
                        temp = a.text
                        
                        if a.status_code == 200 and "重新查詢" not in a.text:
                            dataIndex = str(year)+"-"+str(month)+"-"+str(day)+"-"+str(hour)+"-"+sex+"-"+earth
                            main = soup1.select_one("div.ResultContent")
                            main_str = str(main)
                            pattern = re.compile(r'<tr align="center"><td bgcolor="#FFFFFF" height="30"><span style="font-size: 13px"><font color="#660033">劍靈命理網<\/font><\/span> <span style="font-size: 13px"><font color="#330066">https:\/\/www\.dearmoney\.com\.tw\/<\/font><\/span><\/td><\/tr>')
                            main_str = pattern.sub('', main_str)
                            pattern1 = re.compile(r'劍靈八字命盤批算結果</span>\n</div>')
                            main_list = pattern1.split(main_str)
                            main_str = main_list[-1]
                            pattern2 = re.compile(r'<div class="row justify-content-center m-0 p-0 my-3">')
                            main_list = pattern2.split(main_str)
                            horoscope = "{}\n</div>\n</div>".format(main_list[0])
                            pattern3 = re.compile(r'<div class="row m-0 justify-content-center mt-5 mb-3">')
                            main_list2 = pattern3.split(main_list[1])
                            nativityAnalysis = '<div class="row m-0 justify-content-center mt-5 mb-3">{}'.format(main_list2[1])
                            pattern4 = re.compile(r'</font>運，忌')
                            main_list3 = pattern4.split(main_list2[2])
                            pattern5 = re.compile(r'行運喜<font color="#FF3300">')
                            main_list4 = pattern5.split(main_list3[0])
                            tmepGod = main_list4[1]
                            godOfJoy = []
                            for i in tmepGod:
                                godOfJoy.append(i)
                            godOfJoy_str = ','.join(godOfJoy)  
                            
                            data1 = {"dataIndex": dataIndex,
                                     "horoscope": horoscope,
                                     "nativityAnalysis": nativityAnalysis,
                                     "godOfJoy": godOfJoy_str}
                            database.child('nativitydata').push(data1)
                            
                            # horoscope_bytes = horoscope.encode('utf-8')
                            # nativityAnalysis_bytes = nativityAnalysis.encode('utf-8')
                            # godOfJoy_bytes = str(godOfJoy).encode('utf-8')
                        
                            # with open("ccc.txt", "wb") as f:
                            #     f.write(horoscope_bytes)
                            # with open("ddd.txt", "wb") as f:
                            #     f.write(nativityAnalysis_bytes)
                            # with open("eee.txt", "wb") as f:
                            #     f.write(godOfJoy_bytes)
                            # 將變數存入資料表
                            # dataIndex = '2022-01-01-0-M-N'
                            # horoscope = '八字命盤'
                            # nativityAnalysis = '命盤分析'
                            # godOfJoy = '喜用神'
                            # cursor.execute('INSERT INTO horoscopetable (dataIndex, horoscope, nativityAnalysis, godOfJoy) VALUES (?, ?, ?, ?)', (dataIndex, horoscope, nativityAnalysis, godOfJoy_str))

                            # conn.commit()
                            # 讀取資料表
                            # cursor.execute('SELECT * FROM mytable')
                            # for row in cursor.fetchall():
                            #     print(row)
                        else:
                            continue
                            # print("超過可抓取範圍")
# # 關閉資料庫連線
# conn.close()




