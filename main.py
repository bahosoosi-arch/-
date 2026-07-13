import os
import telebot
from flask import Flask, jsonify
import threading

# 1. دروستکردنی سێرڤەری وێب بۆ ئەوەی هەمیشە کار بکات
app = Flask('')

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "Bot is running!"})

def run_web_server():
    app.run(host='0.0.0.0', port=8080)

# 2. ڕێکخستنی بۆتی تلگرام بە تۆکنی خۆت
BOT_TOKEN = "8817650183:AAGqpdooN4QD0AiZnvw3aRb1Pz2e4YJ59Fw"  
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سڵاو کاکە بەهجەت! بۆتەکەت بە سەرکەوتوویی لەسەر Render کار دەکات. 🚀")

# 3. بەگەڕخستنی بۆتەکە بە شێوازێک کە هەرگیز نەکوژێتەوە
def run_bot():
    print("Bot started...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

if __name__ == "__main__":
    t = threading.Thread(target=run_web_server)
    t.start()
    run_bot()
