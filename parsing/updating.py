import aiosqlite
from parsing import parsing
from scripts import db_all 
async def updating_database(group):
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