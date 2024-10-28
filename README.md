# Telegram-бот на Python с использованием aiogram и Yandex Cloud Functions

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