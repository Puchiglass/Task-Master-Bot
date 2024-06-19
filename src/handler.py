import logging

from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from command import Command


logging.basicConfig(level=logging.INFO)


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    logging.info(f'User ({update.message.chat.full_name}) sent a message: {text}')

    response: str = handle_response(text)
    logging.info(f'Bot: {response}')
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logging.info(f'Update {update} caused error {context.error}')


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello there!'
    return 'I do not understand you!'


class Handler:

    def __init__(self):
        self.command = Command()
        self.start_handler = CommandHandler('start', self.command.start_command)
        self.help_handler = CommandHandler('help', self.command.help_command)
        self.task_handler = CommandHandler('task', self.command.task_command)
