import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Переменная BOT_TOKEN не найдена!")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Бот запущен 🚀")


@dp.message_handler(commands=['bigtest'])
async def bigtest_handler(message: types.Message):
    # 🔥 Вставь сюда свой file_id стикера денег
    sticker_id = "CAACAgIAAxkBAAEexample_money_sticker_id"

    await message.answer_sticker(sticker_id)
    await message.answer("Салас")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)