from bs4 import BeautifulSoup
import csv
import requests

html = requests.get('https://docs.google.com/spreadsheets/d/1dy_i_s5Cn4DEZnl87_j5YdkAL4Yf1Gq9RTe_wVwoHzk/pubhtml').text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")

index=0
answ = []
for row in tables[0].find_all("tr"):
    temp=0
    cur=[]
    for cell in row.find_all(["td"]):
        if(temp==1):
           cur.append(cell.text)    
        elif(cell.text=='ч' or cell.text=='н'):
            temp=1
    answ.append(cur)
    index+=1    

idgroup=0+9*4+1

for x in answ[0:16:2]:
    print(x[37:41])
'''
for i in range(len(answ)):
    print(answ[idgroup][i],answ[idgroup][i],answ[idgroup][i],answ[idgroup][i])
    if(i>50):
        break
'''