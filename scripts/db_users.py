import aiosqlite


async def add_user(tg_id: int,
                   username: str) -> None:

    db = await aiosqlite.connect('''data_bases/users.db''')

    # Создаем таблицу "Users", если она еще не была создана
    await db.execute("""
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        group_id INTEGER,
        eng_group TEXT,
        is_admin INTEGER,
        get_updates BOOLEAN,
        update_time INTEGER
        )
        """)

    # Проверяем, не находится ли пользователь уже в БД
    cursor = await db.execute(f"SELECT id, username FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    # Если его нет в БД, добавляем 
    if result is None:
        await db.execute("INSERT INTO Users (id, username, is_admin) "
                         "VALUES (?, ?, ?)",
                         (tg_id, username, 0))

    await db.commit()
    await db.close()

async def get_user(tg_id: int)->None:
    db = await aiosqlite.connect('''data_bases/users.db''')
    cursor = await db.execute(f"SELECT * FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()
    await db.close()
    return result
    

async def update_user_group(tg_id: int, new_group: int) -> None:
    db = await aiosqlite.connect('data_bases/users.db')
    
    cursor = await db.execute(f"SELECT id FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    if result is not None:
        await db.execute("UPDATE Users SET group_id=? WHERE id=?",
                         (new_group, tg_id))
        await db.commit()

    await db.close()
    
async def update_user_name(tg_id: int, new_first_name: str, new_last_name: str) -> None:
    db = await aiosqlite.connect('data_bases/users.db')

    cursor = await db.execute(f"SELECT id FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    if result is not None:
        await db.execute("UPDATE Users SET first_name=?, last_name=? WHERE id=?",
                         (new_first_name, new_last_name, tg_id))
        await db.commit()

    await db.close()
async def update_user_updates(tg_id: int, new_get_updates: bool) -> None:
    db = await aiosqlite.connect('data_bases/users.db')

    cursor = await db.execute(f"SELECT id FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    if result is not None:
        await db.execute("UPDATE Users SET get_updates=? WHERE id=?",
                         (new_get_updates, tg_id))
        await db.commit()

    await db.close()
async def update_user_update_time(tg_id: int, new_update_time: int) -> None:
    db = await aiosqlite.connect('data_bases/users.db')

    cursor = await db.execute(f"SELECT id FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    if result is not None:
        await db.execute("UPDATE Users SET update_time=? WHERE id=?",
                         (new_update_time, tg_id))
        await db.commit()

    await db.close()
async def update_is_admin(tg_id: int, new_is_admin: int) -> None:
    db = await aiosqlite.connect('data_bases/users.db')

    cursor = await db.execute(f"SELECT id FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    if result is not None:
        await db.execute("UPDATE Users SET is_admin=? WHERE id=?",
                         (new_is_admin, tg_id))
        await db.commit()

    await db.close()
async def is_user_admin(tg_id: int) -> bool: #админ
    db = await aiosqlite.connect('data_bases/users.db')

    cursor = await db.execute(f"SELECT is_admin FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()
    await db.close()
    if result is not None:
        if(result[0]==2):
            return True
        else: 
            return False
    else:
        return False

async def is_user_captain(tg_id: int) -> bool: #староста/админ
    db = await aiosqlite.connect('data_bases/users.db')

    cursor = await db.execute(f"SELECT is_admin FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    await db.close()
    if result is not None:
        if(result[0]>=1):
            return True
        else:
            return False
    else:
        return False
async def is_filled(tg_id: int) -> bool: 
    db = await aiosqlite.connect('data_bases/users.db')
    cursor = await db.execute(f"SELECT first_name, last_name, group_id FROM Users WHERE (id == {tg_id})")
    result = await cursor.fetchone()

    await db.close()

    if result is not None:
        first_name, last_name, group_id = result
        if first_name and last_name and group_id:
            return True
        else:
            return False
    else:
        return False
    
    


