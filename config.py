import yaml


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        with open('config.yml', 'r') as file:
            config = yaml.safe_load(file)
            self.token = config['token']
            self.name = config['bot_name']
            self.poll_interval = config['poll_interval']

    def get_token(self):
        return self.token

    def get_name(self):
        return self.name

    def get_poll_interval(self):
        return self.poll_interval
