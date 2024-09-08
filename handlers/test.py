from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from scripts import db_schedule
from scripts import db_all
from scripts import formatting
from parsing import updating

test_router = Router()
test_router.message.filter()


@test_router.message(Command("dbplus"))
async def dbplus(message: Message):
    await db_schedule.add_schedule_plus(139, "2024.09.03", 2, "Матан", "пр", "2444", "Кохась" )
    
@test_router.message(Command("dbminus"))
async def dbminus(message: Message):
    await db_schedule.add_schedule_minus(139, "2024.09.03", 3)

@test_router.message(Command("dballadd"))
async def dballadd(message: Message):
    await db_all.add_all(139,1,1,"матан","пр","2333","Кохась")
@test_router.message(Command("dballget"))
async def dballget(message: Message):
    s = await db_all.get_row(39,1,1)
    print(str(s[0])+' '+str(s[1])+' '+str(s[2])+' '+str(s[3])+' '+str(s[4]))

@test_router.message(Command("dbupdater"))
async def dbupdater(message: Message):
   await formatting.update_all()

@test_router.message(Command("gettable"))
async def gettable(message: Message):
   print(await updating.get_schedule(139,"2024.09.03"))

@test_router.message(Command("getanswer"))
async def getanswer(message: Message):
   print(await updating.beatiful_schedule(139,"2024.09.03"))

@test_router.message(Command("addminus"))
async def addminus(message: Message):
   await formatting.cancel_lessons(139, "2024.09.03",5)

@test_router.message(Command("addplus"))
async def addplus(message: Message):
   await formatting.add_lessons(139, "2024.09.03",5,"1","1","1","1")

@test_router.message(Command("transfer_lessons"))
async def transfer_lessons(message: Message):
   await formatting.transfer_lessons(139, "2024.09.04",4, "2024.09.04",5)
   
@test_router.message(Command("delete_changes"))
async def delete_changes(message: Message):
   await formatting.delete_changes(139, "2024.09.04")

@test_router.message(Command("get_schedule"))
async def get_schedule(message: Message):
   print(await formatting.get_schedule(139, "2024.09.04"))

