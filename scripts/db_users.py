import aiosqlite


async def add_user(tg_id: int,
                   username: str,
                   first_name: str,
                   last_name: str) -> None:

    db = await aiosqlite.connect('''data_bases/users.db''')

    # Создаем таблицу "Users", если она еще не была создана
    await db.execute("""
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        "group" INTEGER,
        eng_group TEXT,
        is_admin BOOLEAN
        )
        """)

    # Проверяем, не находится ли пользователь уже в БД
    cursor = await db.execute(f"SELECT id, username FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    # Если его нет в БД, добавляем
    if result is None:
        await db.execute("INSERT INTO Users (id, username, first_name, last_name, is_admin) "
                         "VALUES (?, ?, ?, ?, ?)",
                         (tg_id, username, first_name, last_name, False))

    await db.commit()
    await db.close()
