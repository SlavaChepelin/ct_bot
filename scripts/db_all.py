import aiosqlite
async def add_all(group: int,
                            date: int,
                            number: int,
                            subject: str,
                            lesson_type: str,
                            auditorium: str,
                            teacher: str) -> None:
    db = await aiosqlite.connect('''data_bases/all.db''')
    
    await db.execute("""CREATE TABLE IF NOT EXISTS Schedule (
    id INTEGER PRIMARY KEY,
    group_id INTEGER NOT NULL, 
    date INTEGER NOT NULL,
    number INTEGER NOT NULL,
    subject TEXT NOT NULL,
    lesson_type TEXT NOT NULL,
    auditorium TEXT NOT NULL,
    teacher TEXT NOT NULL
    )
    """)
    await db.execute("INSERT INTO Schedule (group_id, date, number, subject,lesson_type,auditorium, teacher)"
                     "VALUES (?, ?, ?, ?, ?, ?, ?)",
                     (group, date, number, subject, lesson_type, auditorium, teacher))
    await db.commit()
    await db.close()

async def check_is_in(group: int, date: int, number: int) -> bool:
    db = await aiosqlite.connect('''data_bases/all.db''')

    cursor = await db.execute(f"SELECT * FROM Schedule WHERE (group_id == {group} AND date == {date} AND number == {number})")
    result = await cursor.fetchone()

    await db.close()

    if result is not None:
        return True  
    else:
        return False  
async def get_row(group: int, date: int, number: int) -> None:
    db = await aiosqlite.connect('''data_bases/all.db''')

    cursor = await db.execute(f"SELECT * FROM Schedule WHERE (group_id == {group} AND date == {date} AND number == {number})")
    result = await cursor.fetchone()

    await db.close()

    if result is not None:
        return result
    else:
        return None