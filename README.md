# 🤖 Code Agent Telegram Bot

Ваш персональний AI-програміст у Telegram! Генерує код для роботи з будь-яким API із відкритих джерел.

## ✨ Можливості

✅ **Генерування коду** - Пише повний робочий код на Python, JavaScript, TypeScript, Go, Rust
✅ **10+ популярних API** - OpenWeather, GitHub, CoinMarketCap, Spotify, Pexels, Unsplash, Jikan і більше
✅ **Вибір мови** - Змініть мову програмування прямо в боті
✅ **Історія чату** - Бот запам'ятовує ваш контекст
✅ **24/7 Доступ** - Запустіть на безплатному або платному сервісі
✅ **Відкриті API** - Інтегрується з публічними API

## 🚀 Швидкий Старт (3 хвилини)

### 1️⃣ Створіть Telegram Бота
```
Телеграм → BotFather → /newbot → введіть ім'я
Скопіюйте TOKEN
```

### 2️⃣ Отримайте API Key
```
Перейдіть на console.anthropic.com
Створіть новий API Key (починається на sk-ant-)
```

### 3️⃣ Розгорніть на Replit (НАЙПРОСТІШЕ)
1. Перейдіть на replit.com
2. Створіть новий Python Repl
3. Копіюйте файли з цього проекту
4. Додайте Secrets (TELEGRAM_TOKEN та ANTHROPIC_API_KEY)
5. Натисніть "Run"

👉 **Детальна інструкція в файлі `QUICK_START.txt`**

## 📁 Файли Проекту

```
├── telegram_bot.py              # Головна програма бота
├── requirements.txt             # Python залежності
├── .env.example                 # Приклад конфігурації
├── Procfile                     # Для Railway/Heroku
├── QUICK_START.txt              # ⭐ Почніть ЗВІДСИ
├── DEPLOYMENT_INSTRUCTIONS.txt  # Варіанти розгортання
├── API_EXAMPLES.txt             # Приклади використання API
└── README.md                    # Цей файл
```

## 💻 Системні Вимоги

- Python 3.8+
- pip (менеджер пакетів)
- Інтернет з'єднання

## 📦 Встановлення Локально

```bash
# 1. Клонуйте або завантажте проект
git clone <url>
cd telegram_bot

# 2. Встановіть залежності
pip install -r requirements.txt

# 3. Створіть .env файл
cp .env.example .env
# Заповніть TELEGRAM_TOKEN та ANTHROPIC_API_KEY

# 4. Запустіть бота
python telegram_bot.py
```

## 🌐 Варіанти Розгортання

### ⭐ Replit (Рекомендується для початківців)
- **Ціна**: Безплатно + $7/місяць для 24/7
- **Складність**: Дуже легко
- **Час**: 5 хвилин
- 👉 [Інструкція](QUICK_START.txt)

### Railway.app (Найбільш гнучкий)
- **Ціна**: Безплатно (500 годин) + $5/місяць додатково
- **Складність**: Легко
- **Час**: 10 хвилин
- 👉 [Інструкція](DEPLOYMENT_INSTRUCTIONS.txt)

### VPS (Contabo, DigitalOcean, Hetzner)
- **Ціна**: $2.99-5/місяць
- **Складність**: Середня
- **Час**: 20 хвилин
- 👉 [Інструкція](DEPLOYMENT_INSTRUCTIONS.txt)

### Heroku (Більше не має безплатного плану)
- **Ціна**: $7+/місяць
- **Складність**: Легко
- 👉 [Інструкція](DEPLOYMENT_INSTRUCTIONS.txt)

## 🎮 Команди Бота

```
/start       - Розпочати роботу
/help        - Показати справку
/apis        - Вибрати API для роботи
/language    - Змінити мову програмування
/clear       - Очистити історію чату
```

## 🔗 Вбудовані API

| API | Опис | Безплатно | Ауте |
|-----|------|----------|------|
| 🌤️ OpenWeather | Дані про погоду | ✅ | API Key |
| 🐙 GitHub | Керування репо | ✅ | Опціонально |
| 💰 CoinMarketCap | Крипто ціни | ✅ | API Key |
| 🎵 Spotify | Потокова музика | ✅ | OAuth |
| 📸 Pexels | Безплатні фото | ✅ | API Key |
| 📷 Unsplash | Якісні фото | ✅ | API Key |
| 🎨 Jikan | Аніме БД | ✅ | Ні |
| 🌍 Rest Countries | Країни | ✅ | Ні |
| 👤 Random User | Випадкові люди | ✅ | Ні |
| 😂 Jokes API | Анекдоти | ✅ | Ні |

## 📚 Приклади Використання

### Приклад 1: Отримання Погоди
```
Користувач: "Напиши функцію для отримання погоди"
Бот: 
```python
import requests

def get_weather(city, api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(url, params=params)
    return response.json()
```
```

### Приклад 2: Пошук Крипто
```
Користувач: "Як отримати топ 10 крипто?"
Бот: [Напише повний код для CoinMarketCap API]
```

### Приклад 3: GitHub Пошук
```
Користувач: "Покажи популярні Python репозиторії"
Бот: [Напише скрипт для пошуку на GitHub]
```

👉 **Більше прикладів в файлі `API_EXAMPLES.txt`**

## 🔑 Отримання API Keys

### OpenWeather
1. Перейдіть на https://openweathermap.org/api
2. Натисніть "Sign Up"
3. Використовуйте безплатний плат (1000 запитів/день)

### CoinMarketCap
1. Перейдіть на https://pro.coinmarketcap.com/
2. Зареєструйтесь
3. Отримайте API Key в профілі

### Spotify
1. Перейдіть на https://developer.spotify.com/
2. Створіть додаток
3. Отримайте Client ID та Client Secret

### Інші API
- **Pexels**: https://www.pexels.com/api/
- **Unsplash**: https://unsplash.com/api
- **Jikan**: Безплатно, без реєстрації!

## ⚙️ Конфігурація

### Файл .env
```env
TELEGRAM_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
ANTHROPIC_API_KEY=sk-ant-v0-1234567890abcdef...
```

### Змінити Мову Програмування
```
/language → виберіть Python, JavaScript, TypeScript, Go чи Rust
```

### Змінити API
```
/apis → натисніть на потрібний API
```

## 🚨 Розв'язання Проблем

### ❌ Помилка: "No module named telegram"
**✅ Рішення**: 
```bash
pip install -r requirements.txt
```

### ❌ Помилка: "Invalid token"
**✅ Рішення**: 
- Перевірте що скопіювали ВЕСЬ TOKEN правильно
- Перегенеруйте token у BotFather

### ❌ Помилка: "API key not found"
**✅ Рішення**:
- Перевірте наявність ANTHROPIC_API_KEY в .env
- На Replit додайте як Secret, не в .env

### ❌ Бот не відповідає
**✅ Рішення**:
1. Напишіть `/start` першим
2. Дайте 30 секунд на першу відповідь
3. Перевірте логи сервісу

### ❌ Бот не працює 24/7
**✅ Рішення**:
- На Replit: купіть Plus ($7/місяць)
- На Railway: $5/місяць додатково
- На VPS: $2.99-5/місяць

## 📊 Використання Claude API

Цей бот використовує Claude API для генерування коду.

**Вартість**: Дешево! (~$0.01 за запит)

**Лімити**: Залежать від плану, рекомендується 100+ запитів/день

**Моделі**: claude-opus-4-1 (найпотужніша)

👉 **Для більш детальної інформації**: https://docs.claude.com/en/api/overview

## 🛠️ Технічний Стек

- **Python 3.8+**
- **python-telegram-bot** - Telegram API
- **anthropic** - Claude API
- **aiohttp** - Асинхронні HTTP запити
- **python-dotenv** - Управління змінними окружения

## 📝 Ліцензія

MIT - Використовуйте вільно!

## 🤝 Контриб'ютинг

Маєте ідеї? Добавте свої API або функції!

## 📞 Підтримка

### Проблеми з ботом?
- Перевірте `QUICK_START.txt`
- Перевірте `DEPLOYMENT_INSTRUCTIONS.txt`
- Прочитайте розділ "Розв'язання Проблем"

### Питання до Anthropic?
- https://support.anthropic.com

### Питання до Telegram?
- https://core.telegram.org/

## 🎉 Що далі?

1. ✅ Розгорніть бота
2. ✅ Напишіть йому своє завдання
3. ✅ Отримайте готовий код
4. ✅ Використовуйте в своїх проектах!

---

**Готові почати?** Перейдіть на `QUICK_START.txt` 🚀

**Made with ❤️ using Claude AI**
