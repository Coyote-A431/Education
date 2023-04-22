import configparser

class SettingsClass:

    def __init__(self, config_file='settings.ini'):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def database(self):
        return [
            self.config['DATABASE']['host'],
            self.config['DATABASE']['port'],
            self.config['DATABASE']['database'],
            self.config['DATABASE']['user'],
            self.config['DATABASE']['password']
        ]

    def api_key(self):
        return self.config['API']['token']

    def log(self):
        return self.config['LOGGING']['log_level']

