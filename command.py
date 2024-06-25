from telegram import Update
from telegram.ext import ContextTypes

from task_manager import TaskManager


class Command:

    def __init__(self):
        self.task_manager = TaskManager()

    async def task_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        task = self.task_manager.get_task()
        await update.message.reply_text(task)

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Hello!')

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Help!')

