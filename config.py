import os
import heroku3
from telethon import TelegramClient, events
#
# Buranı qurdalama
# Yalnız deploy buttonuyla botunu yarat
# 
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME")
log_qrup = int(os.environ.get("LOG_QRUP"))
startmesaj = os.environ.get("startmesaj")
komutlar = os.environ.get("komutlar")
qrupstart = os.environ.get("qrupstart")
support = os.environ.get("support")
sahib = os.environ.get("sahib") f'https://t.me/TheMrMuazzam
#
# mutsuz_panda 
# mutsuz_panda 
# mutsuz_panda 
