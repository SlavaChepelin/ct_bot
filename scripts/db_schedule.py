import aiosqlite



async def add_schedule_plus(group: int,
                            date: str,
                            number: int,
                            subject: str,
                            lesson_type: str,
                            auditorium: str) -> None:
    db = await aiosqlite.connect('''data_bases/schedule.db''')
    
    await db.execute("""CREATE TABLE IF NOT EXISTS Plus (
    id INTEGER PRIMARY KEY,
    group_id INTEGER NOT NULL, 
    date TEXT NOT NULL,
    number TEXT NOT NULL,
    subject TEXT NOT NULL,
    lesson_type TEXT NOT NULL,
    auditorium TEXT NOT NULL,
    )
    """)
    await db.execute("INSERT INTO Plus (group_id, date, number, subject,lesson_type,auditorium)"
                     "VALUES (?, ?, ?, ?, ?, ?)",
                     (group, date, number, subject, lesson_type, auditorium))
    await db.commit()
    await db.close()
'''
async def add_schedule_change(group: int,
                              date: str,
                              number: int,
                              subject: str,
                              lesson_type: str,
                              auditorium: str) -> None:

    db = await aiosqlite.connect

    # Создаем таблицу "Changes", если она еще не была создана
    await db.execute("""
    CREATE TABLE IF NOT EXISTS Changes (
    id INTEGER PRIMARY KEY,
    group_id INTEGER NOT NULL, 
    date TEXT NOT NULL,
    number TEXT NOT NULL,
    subject TEXT NOT NULL,
    lesson_type TEXT NOT NULL,
    auditorium TEXT NOT NULL,
    
    )
    """)

    # Добавляем в БД новую запись об изменениях
    await db.execute("INSERT INTO Changes (group_id, date, number, subject, lesson_type, auditorium) "
                     "VALUES (?, ?, ?, ?, ?, ?)",
                     (group, date, number, subject, lesson_type, auditorium))

    await db.commit()
    await db.close()

    return None


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
    
