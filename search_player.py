from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import ssl


ssl._create_default_https_context = ssl._create_unverified_context
#URL
url = "https://www.shogi.or.jp/game/"
html = urlopen(url)
soup = BeautifulSoup(html,"html.parser")

#table
table = soup.findAll(name = 'div' , attrs={'class' : 'tabContentsA02' , 'id' : "jsTabE01_02"})[0]
rows = table.findAll("tr")

#player
player = input("棋士を入力 : ")
check = 0
battle_day = []
with open("shogi_schedule.csv" , "w" , encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows :
        csvRow = []
        for cell in row.findAll(['td' , 'th']):
            csvRow.append(cell.get_text())

        writer.writerow(csvRow)
        #print(csvRow)
        for i in range(len(csvRow)):
            if csvRow[i] == player:
                check = check+1
                battle_day.append(day)



            if len(csvRow)==1:
                 day = csvRow[i]
                 #print(day)
        #print(type(len(csvRow)))
if check >= 1:
    for i in range(check):
        print(battle_day[i])
    print("に",player,"の対局があります")
