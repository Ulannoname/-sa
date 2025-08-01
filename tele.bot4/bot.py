import asyncio #для асинхронности
import logging #для логирования
from aiogram import Bot, Dispatcher, types #для бота
from aiogram.filters.command import Command 

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="8360441269:AAHDqoZtE4n-hyeLG7Hsv8bQFz6jtN3zCYQ")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())