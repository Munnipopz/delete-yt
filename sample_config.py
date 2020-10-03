import os

class Config(object):
    # get a token from @BotFather  
    TG_BOT_TOKEN = os.environ.geta ("1233265878:AAHJDgJgdskG-tbctKlElKZfXmEWdsOiuOg", "1233265878:AAHJDgJgdskG-tbctKlElKZfXmEWdsOiuOg")
    # Your Telegram Id
    OWNER_ID = int(os.environ.get ('984441749') or 984441749)

