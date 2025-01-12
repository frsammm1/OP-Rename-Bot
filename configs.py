# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "20984532"))
    API_HASH = os.environ.get("API_HASH", "ab43b53b8201801da5efb910fd7c62c9")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 5641314567)
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://thefatherofficial:5N9j3Ef7dBedRwgb@cluster0.7gp4c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002389529583"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
