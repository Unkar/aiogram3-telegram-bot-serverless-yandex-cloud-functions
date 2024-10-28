# create_bot.py
import os
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault

def init_bot():
    bot_token = os.getenv('BOT_TOKEN')
    bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher(storage=MemoryStorage())

    # Внутренняя функция для установки команд
    async def set_commands():
        commands = [
            BotCommand(command='start', description='Старт'),
            BotCommand(command='start_2', description='Старт 2'),
            BotCommand(command='start_3', description='Старт 3')
        ]
        await bot.set_my_commands(commands, BotCommandScopeDefault())

    # Вызов set_commands после инициализации бота
    dp.startup.register(set_commands)  # Регистрация установки команд на запуске бота
    dp.include_router(Router())  # Общий роутер, можно использовать для других обработчиков

    return bot, dp
