import logging
import os


class LoggingMixin:

    def __init__(self, log_level, name, time, to_file):
        self.file_name = name + time
        self.log_name = name
        self.to_file = to_file
        self.logger = logging.getLogger(self.file_name)
        self.log_level = log_level
        self.logger.setLevel(self.log_level)

    def loggin(self):
        log_formatter = logging.Formatter(f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        if self.to_file:
            if not os.path.exists('log'):
                os.mkdir('log')
            log_file = f"log\\{self.file_name}.log"
            handler = logging.FileHandler(log_file, encoding='utf-8')
        else:
            handler = logging.StreamHandler()
        handler.setFormatter(log_formatter)
        self.logger.addHandler(handler)