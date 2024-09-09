import asyncio
from aiogram import Bot, Dispatcher
from aiogram_dialog import setup_dialogs

from dialogs import windows
from handlers import bot_messages, user_commands
from config_reader import config


async def main():
    bot = Bot(config.bot_token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(
         bot_messages.router)
    dp.include_routers(windows.start_dialog, windows.get_prices_dialog)
    setup_dialogs(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())