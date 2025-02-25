import asyncio
import logging
import wikipedia
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

wikipedia.set_lang('uz')


API_TOKEN = "7846226435:AAHJPnGV4Vx4IxG4w9VhanlSDROFGF2LeBE"  # Tokeningizni shu yerga yozing

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Dispatcher yaratishda hech qanday argument kerak emas


@dp.message(Command("start", "help"))
async def send_welcome(message: types.Message):
    """
    Foydalanuvchi /start yoki /help komandasini yuborganida ishga tushadi.
    """
    await message.answer("Assalomu aleykum!\nWikipedia botiga xush kelibsiz.")

@dp.message()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")

async def main():
    """
    Botni ishga tushirish funksiyasi
    """
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)  # FAQAT shuni chaqiramiz, `include_router` KERAK EMAS!

if __name__ == "__main__":
    asyncio.run(main())
