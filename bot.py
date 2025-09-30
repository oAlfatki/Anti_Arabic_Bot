from telegram.ext import Updater, MessageHandler, Filters
import re

# التوكن الخاص بالبوت
TOKEN = "8194171295:AAE0uSVn-dw5j1NXbLtt6ABy55fX9IdpJks"

# تعبير منتظم لاكتشاف الحروف العربية
arabic_pattern = re.compile(r'[\u0600-\u06FF]')

def delete_arabic(update, context):
    message = update.message
    if arabic_pattern.search(message.text or ""):
        try:
            context.bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
            print(f"Deleted Arabic message: {message.text}")
        except Exception as e:
            print(f"Error deleting message: {e}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # فلتر أي نص مكتوب
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, delete_arabic))

    # تشغيل البوت
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if name == 'main':
    main()
