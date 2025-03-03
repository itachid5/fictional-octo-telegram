from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from flask import Flask

# --- টেলিগ্রাম বট সেকশন ---
# আপনার টেলিগ্রাম বটের API টোকেন
TOKEN = "7059109518:AAGtP3w5i6qoyThsxnPeSbDD5rIV2ybiPHw"

# স্টার্ট কমান্ড ফাংশন
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("👋 হ্যালো! আমি আপনার টেলিকম বট। কিছু জানতে চাইলে /help লিখুন।")

# হেল্প কমান্ড ফাংশন
async def help_command(update: Update, context: CallbackContext):
    help_text = "🛠 **সহায়তা মেনু**:\n\n"
    help_text += "/start - বট শুরু করুন\n"
    help_text += "/help - সহায়তা মেনু দেখুন\n"
    help_text += "/about - বট সম্পর্কে জানুন\n"
    await update.message.reply_text(help_text)

# অ্যাবাউট কমান্ড
async def about_command(update: Update, context: CallbackContext):
    await update.message.reply_text("📡 আমি একটি টেলিকম সহায়ক বট! আমাকে তৈরি করা হয়েছে ব্যবহারকারীদের সহায়তা করার জন্য।")

# টেক্সট মেসেজ হ্যান্ডলার (হ্যালো -> হাই)
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text.lower()

    if user_message == "হ্যালো":
        await update.message.reply_text("হাই!")
    else:
        await update.message.reply_text("⚡ দুঃখিত, আমি বুঝতে পারিনি। /help লিখে সহায়তা নিন।")

# অ্যাপ্লিকেশন তৈরি ও হ্যান্ডলার সংযুক্তকরণ
def telegram_bot_app():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ টেলিগ্রাম বট চালু হয়েছে...")
    return app

# --- Flask সেকশন ---
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Kazi Nazrul Islam is a fool."

# --- মেইন ফাংশন ---
def main():
    # টেলিগ্রাম বট অ্যাপ্লিকেশন শুরু করুন (ব্যাকগ্রাউন্ডে)
    telegram_app = telegram_bot_app()
    telegram_app.run_polling(drop_pending_updates=True) # drop_pending_updates=True যোগ করা হলো

    # Flask অ্যাপ্লিকেশন শুরু করুন
    flask_app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False) # use_reloader=False যোগ করা হলো

if __name__ == "__main__":
    main()
