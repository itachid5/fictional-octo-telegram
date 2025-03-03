from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import threading

# আপনার টেলিগ্রাম বটের API টোকেন
TOKEN = "7059109518:AAGtP3w5i6qoyThsxnPeSbDD5rIV2ybiPHw"

# Flask অ্যাপ তৈরি
app = Flask(__name__)

# হোম পেজে একটি মেসেজ দেখাবে
@app.route("/")
def home():
    return "<h1>Welcome to My Telegram Bot!</h1>"

# টেলিগ্রাম বট ফাংশন
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 হ্যালো! আমি আপনার টেলিকম বট। কিছু জানতে চাইলে /help লিখুন।")

async def help_command(update: Update, context: CallbackContext):
    help_text = "🛠 **সহায়তা মেনু**:\n\n"
    help_text += "/start - বট শুরু করুন\n"
    help_text += "/help - সহায়তা মেনু দেখুন\n"
    help_text += "/about - বট সম্পর্কে জানুন\n"
    await update.message.reply_text(help_text)

async def about_command(update: Update, context: CallbackContext):
    await update.message.reply_text("📡 আমি একটি টেলিকম সহায়ক বট! আমাকে তৈরি করা হয়েছে ব্যবহারকারীদের সহায়তা করার জন্য।")

async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()
    
    if user_message == "হ্যালো":
        await update.message.reply_text("হাই!")
    else:
        await update.message.reply_text("⚡ দুঃখিত, আমি বুঝতে পারিনি। /help লিখে সহায়তা নিন।")

# টেলিগ্রাম বট চালানোর ফাংশন
def run_telegram_bot():
    app_bot = Application.builder().token(TOKEN).build()

    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("help", help_command))
    app_bot.add_handler(CommandHandler("about", about_command))
    app_bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ টেলিগ্রাম বট চালু হয়েছে...")
    app_bot.run_polling()

# ব্যাকগ্রাউন্ডে টেলিগ্রাম বট চালানো
threading.Thread(target=run_telegram_bot, daemon=True).start()

# Flask অ্যাপ চালানো
if __name__ == "__main__":
    print("🚀 Flask সার্ভার চালু হয়েছে...")
    app.run(host="0.0.0.0", port=8080, debug=True)
