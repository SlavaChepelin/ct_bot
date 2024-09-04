'''
3) Отменить пару (группа день номер пары)
'''
from scripts import db_schedule
from scripts import db_all
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
    cnt= db_all.get_row(groupid,date,lesson)