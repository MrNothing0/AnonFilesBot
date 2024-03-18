import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6750722613:AAHrfaoZekdYuB_uoaO7qjbq4n2kmj5ZUJE")

    APP_ID = int(os.environ.get("APP_ID", "28874176" ))

    API_HASH = os.environ.get("API_HASH", "b175f88c3cc0f322c6db04d2eda7aa2d")

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002018226982")
