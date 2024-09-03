import aiosqlite


async def add_schedule_change(group: str,
                              date: str,
                              time: str,
                              subject: str,
                              lesson_type: str,
                              auditorium: str):

    db = await aiosqlite.connect('''data_bases/schedule_changes.db''')

    # Создаем таблицу "Changes", если она еще не была создана
    await db.execute("""
    CREATE TABLE IF NOT EXISTS Changes (
    id INTEGER PRIMARY KEY,
    "group" TEXT NOT NULL, 
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    subject TEXT NOT NULL,
    lesson_type TEXT NOT NULL,
    auditorium TEXT NOT NULL
    )
    """)

    # Добавляем в БД новую запись об изменениях
    await db.execute("INSERT INTO Changes ('group', date, time, subject, lesson_type, auditorium) "
                     "VALUES (?, ?, ?, ?, ?, ?)",
                     (group, date, time, subject, lesson_type, auditorium))

    await db.commit()
    await db.close()


async def get_schedule_changes(date: str):
    db = await aiosqlite.connect('''data_bases/schedule_changes.db''')

    # Ищем в БД все совпадения по дате и выгружаем в "result"
    cursor = await db.execute(f"SELECT 'group', date, time, subject, lesson_type, auditorium FROM Users "
                              f"WHERE (date == {date})")
    result = await cursor.fetchall()

    await db.commit()
    await db.close()

    return result
