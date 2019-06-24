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
player = input("棋士を入力")
check = 0
with open("shogi_schedule.csv" , "w" , encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in rows :
        csvRow = []
        for cell in row.findAll(['td' , 'th']):
            csvRow.append(cell.get_text())

        writer.writerow(csvRow)
        print(csvRow)
        for i in range(len(csvRow)):
            if csvRow[i] == player:
                check = 1
                break
        print(type(len(csvRow)))
if check == 1:
    print("今週は",player,"の対局があります")