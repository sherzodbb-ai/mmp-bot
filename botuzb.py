from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

TOKEN = "8692859921:AAE5KgLG8d0kPy9Mv6LaqBwjJhq13W-KTMw"

print("📂 Файлы:", os.listdir('.'))

CONTACTS = """📞 Контакт:

Телефон: +998998303016
Telegram: @R_Mehriddinovna
Компания: Mis Metal Plast MChJ
Адрес: Тошкент ш., Нилуфар кучаси, 1Г"""

LOCATION = """📍 Бизнинг манзил:

Тошкент ш., Нилуфар кучаси, 1Г

🗺 Открыть на карте:
https://maps.app.goo.gl/uzcdhdBqNkUu7CcS6"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open('logo.png', 'rb') as photo:
            await update.message.reply_photo(photo=photo, caption="👋 Хуш келибсиз!", parse_mode='Markdown')
    except:
        await update.message.reply_text("👋 Хуш келибсиз!")

    keyboard = [
        [KeyboardButton("📞 Контакт")],
        [KeyboardButton("💰 Прайс")],
        [KeyboardButton("📍 Локация")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Меню:", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "контакт" in text:
        await update.message.reply_text(CONTACTS)
    
    elif "тарифы" in text or "прайс" in text:
        for fname in os.listdir('.'):
            if 'pricelist' in fname.lower() and fname.lower().endswith('.pdf'):
                with open(fname, 'rb') as pdf:
                    await update.message.reply_document(document=pdf, caption="📄 Прайс-лист Mis Metal Plast")
                return
        await update.message.reply_text("❌ Не найден файл с названием pricelist.pdf")

    elif "локация" in text or "адрес" in text:
        await update.message.reply_text(LOCATION)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
