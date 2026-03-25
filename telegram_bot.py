import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import anthropic
import aiohttp
import json
from datetime import datetime

# Логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Конфигурация
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

# Хранилище контекста пользователя
user_contexts = {}

# Популярные открытые API
POPULAR_APIS = {
    'weather': {
        'name': '🌤️ OpenWeather',
        'url': 'https://openweathermap.org/api',
        'description': 'Данные о погоде в реальном времени'
    },
    'github': {
        'name': '🐙 GitHub',
        'url': 'https://docs.github.com/en/rest',
        'description': 'Управление репозиториями и исправлениями'
    },
    'coinmarketcap': {
        'name': '💰 CoinMarketCap',
        'url': 'https://coinmarketcap.com/api/',
        'description': 'Данные о криптовалютах'
    },
    'spotify': {
        'name': '🎵 Spotify',
        'url': 'https://developer.spotify.com/documentation/web-api',
        'description': 'Потоковая передача музыки и плейлисты'
    },
    'pexels': {
        'name': '📸 Pexels',
        'url': 'https://www.pexels.com/api/',
        'description': 'Бесплатные стоки фотографий'
    },
    'unsplash': {
        'name': '📷 Unsplash',
        'url': 'https://unsplash.com/api',
        'description': 'Высококачественные бесплатные изображения'
    },
    'jikan': {
        'name': '🎨 Jikan (MyAnimeList)',
        'url': 'https://jikan.moe/docs/api',
        'description': 'Информация об аниме и манге'
    },
    'rest-countries': {
        'name': '🌍 Rest Countries',
        'url': 'https://restcountries.com/',
        'description': 'Данные о странах'
    },
    'random-user': {
        'name': '👤 Random User',
        'url': 'https://randomuser.me/api',
        'description': 'Генерирование случайных пользователей'
    },
    'jokes': {
        'name': '😂 Jokes API',
        'url': 'https://v2.jokeapi.dev',
        'description': 'Случайные анекдоты'
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start"""
    user_id = update.effective_user.id
    user_contexts[user_id] = {
        'chat_history': [],
        'selected_api': None,
        'language': 'python'
    }
    
    welcome_text = """👋 Добро пожаловать в Code Agent Bot!

Я вам помогу писать код используя открытые API!

🎯 Что я могу делать:
• Генерировать код для работы с API
• Показывать примеры использования
• Объяснять как интегрировать API
• Выбирать подходящие API для вашего проекта

📝 Доступные команды:
/apis - показать популярные API
/help - справка
/language - выбрать язык программирования
/clear - очистить историю

💬 Просто напишите мне что вам нужно!

Пример: "Напиши функцию для получения текущей погоды"
"""
    
    await update.message.reply_text(welcome_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /help"""
    help_text = """📚 Справка:

1️⃣ Выберите API с помощью команды /apis
2️⃣ Опишите что вам нужно
3️⃣ Я напишу рабочий код

Примеры запросов:
• "Напиши код для получения курса крипто"
• "Покажи как использовать Spotify API"
• "Создай функцию для поиска в GitHub"
• "Как получить случайный анекдот?"

💡 Используйте /language для смены языка программирования

Поддерживаемые языки:
• Python
• JavaScript
• TypeScript
• Go
• Rust
"""
    await update.message.reply_text(help_text)

async def show_apis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показать список популярных API"""
    keyboard = []
    
    for key, api in POPULAR_APIS.items():
        keyboard.append([
            InlineKeyboardButton(api['name'], callback_data=f'api_{key}')
        ])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🌐 Выберите API для работы:",
        reply_markup=reply_markup
    )

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Выбрать язык программирования"""
    languages = [
        ('Python 🐍', 'lang_python'),
        ('JavaScript 🟨', 'lang_javascript'),
        ('TypeScript 🔵', 'lang_typescript'),
        ('Go 🔵', 'lang_go'),
        ('Rust 🦀', 'lang_rust'),
    ]
    
    keyboard = [[InlineKeyboardButton(name, callback_data=data) for name, data in languages]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "💻 Выберите язык программирования:",
        reply_markup=reply_markup
    )

async def api_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка выбора API"""
    query = update.callback_query
    user_id = query.from_user.id
    api_key = query.data.split('_')[1]
    
    api_info = POPULAR_APIS[api_key]
    
    if user_id not in user_contexts:
        user_contexts[user_id] = {'chat_history': [], 'selected_api': None, 'language': 'python'}
    
    user_contexts[user_id]['selected_api'] = api_key
    
    info_text = f"""✅ Вы выбрали: {api_info['name']}

📖 Описание: {api_info['description']}

🔗 Документация: {api_info['url']}

💬 Теперь напишите что вам нужно сделать с этим API!

Примеры:
• "Получи данные о погоде"
• "Покажи TOP 10 крипто по цене"
• "Создай функцию для поиска музыки"
"""
    
    await query.edit_message_text(info_text)

async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка выбора языка"""
    query = update.callback_query
    user_id = query.from_user.id
    lang = query.data.split('_')[1]
    
    if user_id not in user_contexts:
        user_contexts[user_id] = {'chat_history': [], 'selected_api': None, 'language': 'python'}
    
    user_contexts[user_id]['language'] = lang
    
    lang_names = {
        'python': 'Python 🐍',
        'javascript': 'JavaScript 🟨',
        'typescript': 'TypeScript 🔵',
        'go': 'Go 🔵',
        'rust': 'Rust 🦀'
    }
    
    await query.edit_message_text(f"✅ Язык изменен на {lang_names[lang]}")

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Очистить историю чата"""
    user_id = update.effective_user.id
    
    if user_id in user_contexts:
        user_contexts[user_id]['chat_history'] = []
    
    await update.message.reply_text("🧹 История очищена!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка текстовых сообщений"""
    user_id = update.effective_user.id
    user_message = update.message.text
    
    if user_id not in user_contexts:
        user_contexts[user_id] = {'chat_history': [], 'selected_api': None, 'language': 'python'}
    
    context_data = user_contexts[user_id]
    
    # Показываем индикатор печати
    await update.message.chat.send_action("typing")
    
    # Формируем системное сообщение
    system_prompt = f"""Вы профессиональный разработчик, который пишет чистый, рабочий код на {context_data['language'].upper()}.

Текущая конфигурация:
- Язык программирования: {context_data['language']}
- Выбранный API: {context_data['selected_api'] if context_data['selected_api'] else 'Не выбран'}

Инструкции:
1. Напишите полный, рабочий код с комментариями
2. Включите обработку ошибок
3. Покажите пример использования
4. Объясните ключевые части кода
5. Дайте советы по оптимизации

При написании кода используйте markdown блоки ```{context_data['language']}```

Будьте краткими, но информативными!"""
    
    # Добавляем сообщение пользователя в историю
    context_data['chat_history'].append({
        "role": "user",
        "content": user_message
    })
    
    try:
        # Вызываем Claude API
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        
        response = client.messages.create(
            model="claude-opus-4-1",
            max_tokens=2000,
            system=system_prompt,
            messages=context_data['chat_history']
        )
        
        assistant_message = response.content[0].text
        
        # Добавляем ответ в историю
        context_data['chat_history'].append({
            "role": "assistant",
            "content": assistant_message
        })
        
        # Отправляем ответ
        if len(assistant_message) > 4096:
            # Telegram имеет лимит на длину сообщения
            parts = [assistant_message[i:i+4096] for i in range(0, len(assistant_message), 4096)]
            for part in parts:
                await update.message.reply_text(part, parse_mode='Markdown')
        else:
            await update.message.reply_text(assistant_message, parse_mode='Markdown')
    
    except Exception as e:
        logger.error(f"Ошибка при обращении к API Claude: {e}")
        await update.message.reply_text(
            f"❌ Ошибка: {str(e)}\n\nПроверьте что ANTHROPIC_API_KEY установлен правильно.",
            parse_mode='Markdown'
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик ошибок"""
    logger.error(f"Exception while handling an update: {context.error}")

def main():
    """Запуск бота"""
    # Проверяем наличие необходимых переменных окружения
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM_TOKEN не установлен!")
    if not ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY не установлен!")
    
    # Создаем приложение
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("apis", show_apis))
    application.add_handler(CommandHandler("language", language_command))
    application.add_handler(CommandHandler("clear", clear_command))
    
    # Регистрируем обработчики callback
    application.add_handler(CallbackQueryHandler(api_callback, pattern='^api_'))
    application.add_handler(CallbackQueryHandler(language_callback, pattern='^lang_'))
    
    # Регистрируем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Регистрируем обработчик ошибок
    application.add_error_handler(error_handler)
    
    # Запускаем бота
    logger.info("🤖 Telegram бот запущен!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
