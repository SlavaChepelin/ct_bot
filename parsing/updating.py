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
   