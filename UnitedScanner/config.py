
import os

que = {}
admins = {}

SESSION_STRING = os.environ.get("SESSION_STRING", "BQBiMZkAwsBAAJmq0C_P2oQgdvrCHWpxeynIHSoDniz0AlWVrPivnlk2KrpY67Kg2SIhHiyfrxxsTEMmLDSy3U-DNsQsbokepJb56xtC6P4VAAqvM-UYUe4-rbsyRiTkUqVV5MVy9AHYxzXA23PVU3_gFUkD97rKKxeYJ7iTKoCBGY5LqN31-EXpXBH-zxcH_gc4d02nFARWW-mdCzkiMJxD3kNX2wKK2yZotHbH-RGAn1-5xQVCQ42ezK3GGqfHXu5lux6sRTM6aF-30UhD35pcGY-t0iyLtXHZu7Kc2QG15zbjQMM-FwiD56o1U5IkgYyz_QFSWF5jVXQW8NYQTOvbhr0R6gAAAAFjLzPOAA")
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
ENFS = set(int(x) for x in os.environ.get("ENFS", "").split()) 
ENFS = list(ENFS) 
GBAN_CHATS = set(int(x) for x in os.environ.get("GBAN_CHATS", "").split())
