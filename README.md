# Telegram Бот для Суммаризации Ссылок

Этот проект представляет собой телеграм-бота, который автоматически анализирует ссылки, отправленные пользователями, извлекает из них краткое содержание с помощью Yandex API и отправляет это содержание обратно в чат.

## Функции

- Бот слушает сообщения в чате и ищет ссылки в текстах.
- При нахождении ссылки бот отправляет запрос на Яндекс для получения краткого содержания страницы.
- Полученное содержание отправляется обратно в чат.

## Установка и запуск

Для работы с ботом используется Docker, что упрощает настройку окружения и развертывание приложения.

### Шаг 1: Установите Docker и Docker Compose

Перед началом работы установите Docker и Docker Compose, следуя [официальной инструкции](https://docs.docker.com/get-docker/).

### Шаг 2: Клонируйте репозиторий

Клонируйте репозиторий с помощью Git и перейдите в папку проекта:

```bash
git clone https://github.com/r4hx/telegram-summary-links.git
cd telegram-summary-links
```

Вот ваш README.md в формате Markdown:

markdown

# Telegram Бот для Суммаризации Ссылок

Этот проект представляет собой телеграм-бота, который автоматически анализирует ссылки, отправленные пользователями, извлекает из них краткое содержание с помощью Yandex API и отправляет это содержание обратно в чат.

## Функции

* Бот слушает сообщения в чате и ищет ссылки в текстах.
* При нахождении ссылки бот отправляет запрос на Яндекс для получения краткого содержания страницы.
* Полученное содержание отправляется обратно в чат.

## Установка и запуск

Для работы с ботом используется Docker, что упрощает настройку окружения и развертывание приложения.

### Шаг 1: Установите Docker и Docker Compose

Перед началом работы установите Docker и Docker Compose, следуя [официальной инструкции](https://docs.docker.com/get-docker/).

### Шаг 2: Клонируйте репозиторий

Клонируйте репозиторий с помощью Git и перейдите в папку проекта:

```bash
git clone https://github.com/yourusername/telegram-link-summary-bot.git
cd telegram-link-summary-bot
```

### Шаг 3: Переменные окружения

В корне проекта создайте файл .env с содержимым, содержащим ваши конфигурационные переменные, например:

```env
# .env файл

# Токен Telegram бота
TELEGRAM_TOKEN=your_telegram_bot_token_here

# ID Telegram группы или чата
TELEGRAM_GROUP_ID=your_telegram_group_id_here

# Другие переменные окружения (например, для Yandex API)
YANDEX_API_KEY=your_yandex_api_key_here
YANDEX_API_URL=https://api.yandex.com/summary
```

### Шаг 4: Запустите бота

Для запуска бота используйте Docker Compose. Это автоматически создаст все необходимые контейнеры и запустит бота в фоновом режиме:

```bash
make up
```

### Шаг 5: Войдите в контейнер бота

Если нужно зайти в контейнер бота для отладки или настройки, используйте команду:

```bash
make entry
```

## Использование
### Шаг 1: Отправьте ссылку

Отправьте ссылку в чат с вашим телеграм-ботом. Бот будет автоматически отслеживать ссылки, начинающиеся с http:// или https://.

### Шаг 2: Бот обработает ссылку

После того, как бот получит ссылку, он отправит запрос на Яндекс API для получения краткого содержания страницы. Как только содержание будет извлечено, бот отправит его обратно в чат.

## Требования

Для запуска проекта на локальной машине необходимо выполнить следующие требования:

- Docker — для контейнеризации приложения и упрощения развертывания.
- Docker Compose — для упрощения работы с несколькими контейнерами.
- telebot — библиотека для взаимодействия с Telegram API.
- beautifulsoup4 — для парсинга HTML-страниц, если необходимо извлекать информацию с веб-страниц.
- httpx — для асинхронных HTTP-запросов к внешним сервисам.


