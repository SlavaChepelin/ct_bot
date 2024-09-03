from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from scripts import db_schedule
from scripts import db_all
from parsing import updating

admin_router = Router()
admin_router.message.filter()


@admin_router.message(Command("dbplus"))
async def dbplus(message: Message):
    await db_schedule.add_schedule_plus(39, "2024.09.03", 2, "Матан", "пр", "2444", "Кохась" )
    
@admin_router.message(Command("dbminus"))
async def dbminus(message: Message):
    await db_schedule.add_schedule_minus(39, "2024.09.03", 3)

@admin_router.message(Command("dballadd"))
async def dballadd(message: Message):
    await db_all.add_all(39,1,1,"матан","пр","2333","Кохась")
@admin_router.message(Command("dballget"))
async def dballget(message: Message):
    s = await db_all.get_row(39,1,1)
    print(str(s[0])+' '+str(s[1])+' '+str(s[2])+' '+str(s[3])+' '+str(s[4]))

@admin_router.message(Command("dbupdater"))
async def dbupdater(message: Message):
   await updating.updating_database(39)

@admin_router.message(Command("gettable"))
async def gettable(message: Message):
   print(await updating.get_schedule(39,"2024.09.03"))

@admin_router.message(Command("getanswer"))
async def getanswer(message: Message):
   print(await updating.beatiful_schedule(39,"2024.09.03"))