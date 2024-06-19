from config import Config
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Application, MessageHandler, filters


def main():
    print('Bot is running...')
    config = Config()
    TOKEN = config.get_token()
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('task', task_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the Telegram server for updates
    print('Bot is polling...')
    app.run_polling(poll_interval=1)


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Help!')


async def task_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Go kiss your wife!')


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello there!'
    return 'I do not understand you!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    print(f'User ({update.message.chat.id}) sent a message: {text}')

    response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    main()
