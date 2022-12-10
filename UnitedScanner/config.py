
import os

que = {}
admins = {}

SESSION_STRING = os.environ.get("SESSION_STRING", "BQChC24XXMTx_IQNjvyLiNEG4QYgiS53PW9hMje9hMIEGkAullljnud79tY1K7IoDPCsLoZKkW0W0QQoWVT7-B_UTdvfhIokJjzN51NrNzNV7N0JSAHffuDiHA4y8Jw6PyXBoPq5kjqThDNKK3w4hdj4oawADKLYbB3iHTMb00n6K7EleEht4jnxpXNueQrpQlXxYr3LPVg30St5_Qak-cyUOzuZg3aULGmVB65SHKXLyUDMGcS90FCc6oL2e8GMdZlQqqGVf2bmAj_ojjrtMtahJGg3t8QmUvzZPBhAQmXZONGINEHYiIgHknfPlQ11RLGW4XoqfTvIqQg7U0mBgVI4AAAAAHNm18YA")
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
