from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sqlite3
import os

def start(update, context):
    update.message.reply_text("Hi! Send your phone number to get OTP codes.")

def get_otps(update, context):
    phone_number = update.message.text
    otps = fetch_otps(phone_number)
    if otps:
        message = "\n".join([f"OTP: {otp[0]}, Received at: {otp[1]}" for otp in otps])
        update.message.reply_text(message)
    else:
        update.message.reply_text("No OTPs found for this number.")

def fetch_otps(phone_number):
    conn = sqlite3.connect('otps.db')
    cursor = conn.cursor()
    cursor.execute("SELECT otp_code, received_at FROM otps WHERE phone_number = ?", (phone_number,))
    otps = cursor.fetchall()
    conn.close()
    return otps

def main():
    token = os.getenv("6675363276:AAFhn3D9zTnX7kql7tYPgKa1EPoHDuMu5DkN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_otps))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
