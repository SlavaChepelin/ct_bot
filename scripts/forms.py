import datetime
from scripts import db_schedule
from scripts import db_all
from parsing import updating
'''
3) Отменить пару (группа день номер пары)
'''
async def cancel_lessons(groupid: int, date: str, lesson: int) -> None: #группа, дата, номер пары
    await db_schedule.add_schedule_minus(groupid, date, lesson)
'''
4) Добавить пару (группа, день, номер пары, subject, lesson_type, auditorium, teacher)
'''
async def add_lessons(groupid: int, date: str, lesson: int, 
                      subject: str, lesson_type:str, auditorium: str, teacher: str) -> None: 
    await db_schedule.add_schedule_plus(groupid, date, lesson, subject, lesson_type, auditorium, teacher)
'''
5) Перенести пару (день номер пары откуда, день номер пары куда)
'''
async def transfer_lessons(groupid: int, date: str, lesson:str, newdate: str, newlesson:str) -> None:
    cnt= await db_all.get_row(groupid,date,lesson)
    if(cnt != None):
        await cancel_lessons(groupid, date, lesson)
        await add_lessons(groupid, newdate, newlesson, cnt[4], cnt[5], cnt[6], cnt[7])

'''
6) Заменить пару (день номер пары, на что заменить(вид и т.п)
'''

async def replace_lessons(groupid: int, date: str, lesson: int, new_subject: str, new_lesson_type: str, new_auditorium: str, new_teacher: str) -> None:
    await cancel_lessons(groupid,date,lesson)
    await add_lessons(groupid,date,lesson,new_subject, new_lesson_type, new_auditorium, new_teacher )
''') Убрать изменения на день x'''
async def delete_changes(groupid: int, date: str) -> None:
    await db_schedule.delete_plus_changes(groupid, date)
    await db_schedule.delete_minus_changes(groupid, date)
    
''' вернуть расписание на день x, группы y'''
    
async def get_schedule(groupid: int, date: str) -> list:
    return await updating.beatiful_schedule(groupid, date)
