
import os

que = {}
admins = {}

SESSION_STRING = os.environ.get("SESSION_STRING", "BQBiMZkAcwF0lppCfhZkkY8ya4Gfplq9ANahM7S_OiuoLsL9-rQh_4UT3RA4xh40qBXzWmhLpWTjX02SSq__McOIuWZ6yFsGtPyS2uoBh5ZWEOGWhyLe5IohSSdyNBHdMCbyXUEfKYHyufR-MCVelOZbGjlPjT8SPCFKOjjfydYjsRU3EO9a3yYJ3Q2E-2vdgP-0KVypGFkL6fACdWL3ovVx8ODXfCMHSJPFXpE3VCARUz5wOE8lLozSMQuQnTDX4oMu5DHOXt2kt16nvNWsp0HNhY4Uc1knhx_hpGjQ2QqILh1A64g79RzImEVAgGjdxQKJC6iTq0pl0XkmAi1KOUS7ddBgZgAAAABzZtfGAA")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5988064205:AAHfPoie-X4QdIR3b4LtRztNIst4E_22axM")
API_ID = int(os.environ.get("API_ID", "28624076"))
API_HASH = os.environ.get("API_HASH", "439d58a783f6e70086ea81ba5baa5207")
OWNER_ID = int(os.environ.get("OWNER_ID", "1936119750"))
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "UnitedXSupport")
UPDATE = os.environ.get("UPDATE", None)
CMD_OP = list(os.environ.get("CMD_OP", "/ ?").split())
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb://mongo:QTEfQZzEmJU8fAnKj3or@containers-us-west-147.railway.app:5948")
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1001583123595)

INSPECTORS = set(int(x) for x in os.environ.get("INSPECTORS", "").split())
INSPECTORS.add(OWNER_ID)
INSPECTORS = list(INSPECTORS)
GBAN_CHATS = set(int(x) for x in os.environ.get("GBAN_CHATS", "").split())
