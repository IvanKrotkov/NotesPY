import datetime


class Note:
    date = 0
    text = ""
    def __init__(self, text):
        self.date = datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S")
        self.text = text
        pass
    