from bs4 import BeautifulSoup
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
def get_date(day,group): #day 1-7, group 32-42
    idgroup=(group-30)*4+1
    if(group==41 or group==42):
       idgroup=(group-31)*4+1 
    day_cnt=dates[day-1]
    timetable=[]
    for x in answ[day_cnt[0]+3:day_cnt[1]+3:2]:
        timetable.append((x[idgroup:idgroup+4]))
    return timetable

def get_schedule(group):
    #тут обруби курс, позже добавим разделение на курсы
    group = group %100
    schedule=[]
    for day in range(1,7):
        schedule.append(get_date(day,group))
    return schedule
