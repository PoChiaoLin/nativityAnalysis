import re
import requests
from bs4 import BeautifulSoup

session = requests.session()
myHeaders = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

payload1 = {
    "_Year": "1969",
    "_Month": "1",
    "_Day": "14",
    "_Hour": "9",
    "_sex": "M",
    "_earth": "N",
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

if a.status_code == 200:
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
        
    horoscope_bytes = horoscope.encode('utf-8')
    nativityAnalysis_bytes = nativityAnalysis.encode('utf-8')
    godOfJoy_bytes = str(godOfJoy).encode('utf-8')

    with open("ccc.txt", "wb") as f:
        f.write(horoscope_bytes)
    with open("ddd.txt", "wb") as f:
        f.write(nativityAnalysis_bytes)
    with open("eee.txt", "wb") as f:
        f.write(godOfJoy_bytes)




