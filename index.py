import json
from aiogram.types import Update
from create_bot import init_bot
from handlers.start import start_router  # Импортируем start_router

# Инициализация бота и диспетчера
bot, dp = init_bot()

# Подключаем start_router к диспетчеру
dp.include_router(start_router)

# Функция обработки события
async def process_event(event, dp):
    for message in event.get('messages', []):
        body = message.get('details', {}).get('message', {}).get('body')
        if body:
            update = Update(**json.loads(body))
            await dp.feed_update(bot, update)

# Основной обработчик
async def handler(event, context):
    print(event)
    await process_event(event, dp)
    return {'statusCode': 200, 'body': 'ok'}