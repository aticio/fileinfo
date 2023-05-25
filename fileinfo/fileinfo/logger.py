import datetime


class Logger:
    def __init__(self) -> None:
        self.messages = []

    def log(self, message):
        self.messages.append((datetime.datetime.now(), message))