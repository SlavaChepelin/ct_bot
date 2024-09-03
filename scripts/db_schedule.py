import aiosqlite



async def add_schedule_plus(group: int,
                            date: str,
                            number: int,
                            subject: str,
                            lesson_type: str,
                            auditorium: str,
                            teacher: str) -> None:
    db = await aiosqlite.connect('''data_bases/schedule.db''')
    
    await db.execute("""CREATE TABLE IF NOT EXISTS Plus (
    id INTEGER PRIMARY KEY,
    group_id INTEGER NOT NULL, 
    date TEXT NOT NULL,
    number INTEGER NOT NULL,
    subject TEXT NOT NULL,
    lesson_type TEXT NOT NULL,
    auditorium TEXT NOT NULL,
    teacher TEXT NOT NULL
    )
    """)
    await db.execute("INSERT INTO Plus (group_id, date, number, subject,lesson_type,auditorium, teacher)"
                     "VALUES (?, ?, ?, ?, ?, ?, ?)",
                     (group, date, number, subject, lesson_type, auditorium, teacher))
    await db.commit()
    await db.close()
    
async def add_schedule_minus(group: int,
                            date: str,
                            number: int,
                            )-> None:
    db = await aiosqlite.connect('''data_bases/schedule.db''') 
    await db.execute("""CREATE TABLE IF NOT EXISTS Minus (
    id INTEGER PRIMARY KEY,
    group_id INTEGER NOT NULL, 
    date TEXT NOT NULL,
    number INTEGER NOT NULL
    )
    """)
    await db.execute("INSERT INTO Minus (group_id, date, number)"
                     "VALUES (?, ?, ?)",
                     (group, date, number))
    await db.commit()
    await db.close()
    
async def get_plus_changes(group: int, date: str):
    db = await aiosqlite.connect('''data_bases/schedule.db''')

   
    cursor = await db.execute(f"SELECT * FROM Plus WHERE (group_id == {group} AND date == '{date}')")
    result = await cursor.fetchall()

    await db.commit()
    await db.close()

    return result
async def get_minus_changes(group: int, date: str):
    db = await aiosqlite.connect('''data_bases/schedule.db''')

   
    cursor = await db.execute(f"SELECT * FROM Minus WHERE (group_id == {group} AND date == '{date}')")
    result = await cursor.fetchall()

    await db.commit()
    await db.close()

    return result
'''

async def get_schedule_changes(date: str):
    db = await aiosqlite.connect(

    # Ищем в БД все совпадения по дате и выгружаем в "result"
    cursor = await db.execute(f"SELECT group_id, date, number, subject, lesson_type, auditorium FROM Users "
                              f"WHERE (date == {date})")
    result = await cursor.fetchall()

    await db.commit()
    await db.close()

    return result
'''
    
