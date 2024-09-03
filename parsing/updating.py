import aiosqlite
import datetime

from parsing import parsing
from scripts import db_all
from scripts import db_schedule
 
async def updating_database(group: int):
    parsing.download()
    timetable = parsing.get_schedule(group)
    date_update = []
    for day in range(6):
        for lessons in range(0,8):
            subject = timetable[day][lessons][0]
            lesson_type = timetable[day][lessons][1]
            auditorium= timetable[day][lessons][2]
            teacher = timetable[day][lessons][3]
            result = await db_all.get_row(group, day+1, lessons+1)
            if(result==None):
                if(subject==""):
                    continue
                else:
                    date_update.append([group, day+1, lessons+1])
                    await db_all.add_all(group, day+1, lessons+1, subject, lesson_type, auditorium, teacher)
            else:
                if(subject==""):
                    date_update.append([group, day+1, lessons+1])
                    await db_all.delete_row(group, day+1, lessons+1)
                else:
                    if(result[4]!=subject or result[5]!=lesson_type or result[6]!=auditorium or result[7]!=teacher):
                        date_update.append([group, day+1, lessons+1])
                        await db_all.update_row(group, day+1, lessons+1, subject, lesson_type, auditorium, teacher)
    print(date_update)


async def get_schedule(group: int, day: str):
    date = datetime.datetime(int(day.split('.')[0]),int(day.split('.')[1]),int(day.split('.')[2])).weekday()+1
    result1 = await db_schedule.get_plus_changes(group, day)
    result2 = await db_schedule.get_minus_changes(group,day) 
    result3 = await db_all.get_schedule(group,date)
    anstable = [0]*8
    for i in range(8):
        anstable[i]=["","","",""]
    for row in result3:
        anstable[int(row[3])-1]=[row[4],row[5],row[6],row[7]]
    if(result1==None and result2==None):
        return anstable
    for row in result2:
        anstable[int(row[3])-1]=["","","",""]
    for row in result1:
        anstable[int(row[3])-1]=[row[4],row[5],row[6],row[7]]
    return anstable
data = ["8:20-9:50","10:00-11:30","11:40-13:10","13:30-15:00","15:20-16:50","17:00-18:30","18:40-20:10","20:20-21.50 "]
async def beatiful_schedule(group: int, day: str):
    schedule = await get_schedule(group, day)
    ans=[]
    ans.append(f"Расписание для группы {group} на {day}:")
    for i in range(8):
        if(schedule[i][0]== ""):
            continue
        ans.append(f"{data[i]} = {schedule[i][0]}, {schedule[i][1]}, {schedule[i][2]}, {schedule[i][3]}")
    return ans