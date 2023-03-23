import requests
from bs4 import BeautifulSoup
data = {}
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

#第三步產生一個dict

#print(linkData)
resp2_1 = requests.get(linkData[0]) 
#print(resp2_1)
soup2_1 = BeautifulSoup(resp2_1.text,"lxml")   
#print(soup2_1)

    
colum = soup2_1.find("div",class_="industry-ranking-list-header").text.replace("\n",",").strip(",").split(",")    

del colum[2:4]
colum[0] = "股票代碼"
print(colum)#產業名稱跟屬性容器

   
colums   = [colum[0],colum[1],colum[2]]
for t in t_list:
    data[t] = {colums[0]: [], colums[1]: [],colums[2]:[]}

 #第4步上帝創造一切

for t, url in zip(t_list, linkData):
    resp2 = requests.get(url)
    soup2 = BeautifulSoup(resp2.text, "lxml")

    uls = soup2.find("div", class_="industry-ranking-list-body").find_all("ul")
    for ul in uls:
        li1 = ul.find_all("li")[1].text.strip().split(" ")
        li2 = ul.find_all("li")[4].text
        data[t][colums[0]].append(li1[0])
        data[t][colums[1]].append(li1[1])
        data[t][colums[2]].append(li2)    
        
import pandas as pd

df = pd.DataFrame(data)            
print(df)

