from bs4 import BeautifulSoup
import csv
import requests
answ = []
def download():
    global answ
    html = requests.get('https://docs.google.com/spreadsheets/d/1dy_i_s5Cn4DEZnl87_j5YdkAL4Yf1Gq9RTe_wVwoHzk/pubhtml').text
    soup = BeautifulSoup(html, "lxml")
    tables = soup.find_all("table")

    index=0
    answ=[]
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
dates=[[0,16],[17,33],[34,50],[51,67],[68,84],[85,102]]
def get_date(day,group): #day 1-6, group 32-39
    idgroup=(group-30)*4+1
    day_cnt=dates[day-1]
    for x in answ[day_cnt[0]+3:day_cnt[1]+3:2]:
        print(x[idgroup:idgroup+4])
download()
get_date(1,39)
print("")
get_date(2,39)