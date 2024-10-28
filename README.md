# Telegram-бот на Python с использованием aiogram 3.13.1 и Yandex Cloud Functions

Этот проект представляет собой пример создания простого Telegram-бота с использованием Python и библиотеки `aiogram`. Бот обрабатывает команды `/start`, `/start_2` и `/start_3` и отвечает соответствующими сообщениями. Проект настроен для развертывания на платформе Yandex Cloud Functions.

## Структура проекта

- **index.py**: Основная точка входа приложения. Обрабатывает входящие события от Yandex Cloud Function и передает их в диспетчер `aiogram`.
- **create_bot.py**: Содержит логику инициализации бота и диспетчера, а также установку команд бота.
- **start.py**: Файл с обработчиками команд `/start`, `/start_2`, `/start_3`.

## Установка и настройка

### Требования

Для работы проекта необходимо установить следующие зависимости:

```bash
pip install aiogram==3.13.1
```

Также вам потребуется создать аккаунт на Yandex Cloud и настроить доступ к Yandex Cloud Functions.

### Настройка переменных окружения

В файле `create_bot.py` используется переменная окружения `BOT_TOKEN` для хранения токена вашего Telegram-бота. Убедитесь, что вы установили эту переменную перед запуском проекта.

### Развертывание на Yandex Cloud Functions

Следуйте инструкциям по созданию и настройке функции на Yandex Cloud Functions. Укажите файл `index.handler` в качестве точки входа вашей функции.

### Лицензия

Этот проект распространяется под лицензией MIT. См. файл LICENSE для получения дополнительной информации.

**Примечание:** Не забудьте заменить токены и другие конфиденциальные данные на свои собственные при использовании этого примера.

Telegram Bot on Python with aiogram 3.13.1 and Yandex Cloud Functions
This project is an example of creating a simple Telegram bot using Python and the aiogram library. The bot handles commands such as /start, /start_2, and /start_3 and responds with corresponding messages. The project is configured for deployment on the Yandex Cloud Functions platform.

Project Structure
index.py: Main entry point of the application. Handles incoming events from Yandex Cloud Function and passes them to the aiogram dispatcher.
create_bot.py: Contains logic for initializing the bot and its dispatcher, as well as setting up the bot's commands.
start.py: File containing handlers for the /start, /start_2, and /start_3 commands.
Installation and Configuration
Requirements
To run this project, you need to install the following dependencies:


pip install aiogram==3.13.1
You will also need to create an account on Yandex Cloud and set up access to Yandex Cloud Functions.

Environment Variables Setup
In the file create_bot.py, the environment variable BOT_TOKEN is used to store your Telegram bot token. Make sure you have set this variable before running the project.

Deployment on Yandex Cloud Functions
Follow the instructions for creating and configuring a function on Yandex Cloud Functions. Specify index.handler as the entry point for your function.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Note: Remember to replace tokens and other sensitive data with your own when using this example.

