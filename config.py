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
USERNAME = os.environ.get("USERNAME")DiamonTaggerBot
log_qrup = int(os.environ.get("LOG_QRUP"))
startmesaj = os.environ.get("startmesaj")Salam** __Çox funksiyalı tağ botu
❗Qrupda Admin Etmək Vacibdir ★__
komutlar = os.environ.get("komutlar")Kömək Menyusuna Xoş gəldin 🗽
/all <səbəb> - Hər kəsi mesajda 5 tağ olmaqla tağ edər
/admin <səbəb> - Adminləri mesajda 1 tağ olmaqla tağ edər
/tektag <səbəb> - Hər kəsi mesajda 1 tağ olmaqla tağ edər
/etag  <səbəb> - Hər kəsi mesajda 5 emoji olmaqla emojilərlə tağ edər
/rtag  <səbəb> - İstifadəçiləri rənglərlə etiketləyirəm
/cancel - Tağ Prosesini Sonlandırar
❕ Bu əmrlərdən yalnız idarəçilər istifadə edə bilər. ✨
qrupstart = os.environ.get("qrupstart")✅ **Mən Aktivəm !** 🕊️ **Əmrləri görmək üçün pm-ə baxa bilərsiniz.*
support = os.environ.get("support") https://t.me/DiamondTaggerSupport
sahib = os.environ.get("sahib") https://t.me//TheMrMuazzam
#
# mutsuz_panda 
# mutsuz_panda 
# mutsuz_panda 
