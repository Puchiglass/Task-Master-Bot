import yaml


class Config:
    def __init__(self):
        with open('../config.yml', 'r') as file:
            config = yaml.safe_load(file)
            self.token = config['token']
            self.name = config['bot_name']

    def get_token(self):
        return self.token

    def get_name(self):
        return self.name
