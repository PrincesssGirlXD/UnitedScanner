
import os

que = {}
admins = {}

SESSION_STRING = os.environ.get("SESSION_STRING", "BQBiMZkAwteEVUvkjjCfMVQezEPtjcKuzAraomRjutEbJeQ29N-LY4DlCrdwqXsRHG36bwk0fsSTzst0JIF8F0HFSMbkrR_qJdjRPP5QzDb5bQefhyZjjm4wgoFsOhxPLKM46VdhGSk89E2S2moCrPUaMUV_yzBZQKh9ic8B69jqD_9YAFwk45AZXEpwh8JYgcGlKJ6qZAR0cJBEwkYdVzt4N8CVu2325fTFs4yQ_I05dEbQvz0KWEKdeqGHaGQaFVOWbk1A_5T0N0RaA0TsMtD1JPAmEGav1WOxO79Ldo7YQHnRnHDn2FaC_o64mTg_KyuNh9QKp_Qz3NHjNrZ7I6EJbi4VtAAAAAFjLzPOAA")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5988064205:AAHfPoie-X4QdIR3b4LtRztNIst4E_22axM")
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/e3c8a57b3ebcd0b1c8529.mp4")
API_ID = int(os.environ.get("API_ID", "28624076"))
API_HASH = os.environ.get("API_HASH", "439d58a783f6e70086ea81ba5baa5207")
OWNER_ID = int(os.environ.get("OWNER_ID", "1936119750"))
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "UnitedXSupport")
UPDATE = os.environ.get("UPDATE", None)
CMD_OP = list(os.environ.get("CMD_OP", "/ ?").split())
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb://mongo:QTEfQZzEmJU8fAnKj3or@containers-us-west-147.railway.app:5948")
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", -1001583123595)

INSPECTORS = set(int(x) for x in os.environ.get("INSPECTORS", "1936119750").split())
INSPECTORS.add(OWNER_ID)
INSPECTORS = list(INSPECTORS) 
ENFS = set(int(x) for x in os.environ.get("ENFS", "").split()) 
ENFS = list(ENFS) 
GBAN_CHATS = set(int(x) for x in os.environ.get("GBAN_CHATS", "").split())
