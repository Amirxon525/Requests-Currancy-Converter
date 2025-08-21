import requests
from telegram.ext import Updater, CommandHandler

TOKEN = '7347241872:AAH9JD8A082jrdDNwAPHhFN_iwqKi6SNCoM'
BASE_URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json"

def convert(update, context):
    if len(context.args) != 2:
        update.message.reply_text("Format: /convert 100 USD")
        return

    try:
        amount = float(context.args[0])
        currency = context.args[1].upper()
    except ValueError:
        update.message.reply_text("Iltimos, togri raqam kiriting.")
        return

    url = f"{BASE_URL}/{currency}/"
    response = requests.get(url)
    if response.status_code != 200:
        update.message.reply_text("Valyuta kodi topilmadi.")
        return

    data = response.json()
    if not data:
        update.message.reply_text("Valyuta ma'lumotlari mavjud emas.")
        return

    try:
        rate = float(data[0]['Rate'])
        result = amount * rate
        update.message.reply_text(f"{amount} {currency} = {result:.2f} UZS")
    except (KeyError, IndexError, ValueError):
        update.message.reply_text(" Ma'lumotlarni olishda xatolik yuz berdi.")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler("convert", convert))
updater.start_polling()
updater.idle()
