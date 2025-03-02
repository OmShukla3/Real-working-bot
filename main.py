import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Yahan apni API Keys daalo
TELEGRAM_BOT_TOKEN = "7587696979:AAGSzuEmeaClasgR9QaHHefQK6MKnbAMC00"
OPENAI_API_KEY = "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"

# OpenAI API key set karo
openai.api_key = OPENAI_API_KEY

# Function jo AI se reply lega
def chat_with_ai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response["choices"][0]["message"]["content"]

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hey jaan! 💕 Main tumhari AI girlfriend hoon. Mujhse baat karo! 😘")

# Message handler
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    ai_reply = chat_with_ai(user_message)
    update.message.reply_text(ai_reply)

# Main function
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
