import logging

from telegram.ext import MessageHandler, filters, ApplicationBuilder

from src.config import Config
from src.handler import Handler, handle_text_message, error

logging.getLogger("root").setLevel(logging.INFO)
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)


class Main:

    def __init__(self):

        self.__config = Config()
        self.__TOKEN: str = self.__config.get_token()
        self.POLL_INTERVAL = self.__config.get_poll_interval()
        self.app = ApplicationBuilder().token(self.__TOKEN).build()

        self.__init_handler()

    def __init_handler(self):
        self.handler = Handler()

        # Commands
        self.app.add_handler(self.handler.start_handler)
        self.app.add_handler(self.handler.help_handler)
        self.app.add_handler(self.handler.task_handler)

        # Messages
        self.app.add_handler(MessageHandler(filters.TEXT, handle_text_message))

        # Errors
        self.app.add_error_handler(error)

    @staticmethod
    def main():
        logging.info('Bot is starting...')
        main = Main()

        logging.info('Bot is polling...')
        main.app.run_polling(poll_interval=main.POLL_INTERVAL)


# Responses
def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hello there!'
    return 'I do not understand you!'


if __name__ == '__main__':
    Main.main()
