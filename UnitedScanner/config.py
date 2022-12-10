
import os

que = {}
admins = {}

SESSION_STRING = os.environ.get("SESSION_STRING", "BQBYAVjYu6u8L40myEoKYuMTbBTEK75ioDmJKkLZsXyPzs2WoLG5WsGEkHgqdxZQv37Y4hXoFAC3SLaW0nUToSMZguPq4v01tPb1uYKGZ7AAhf3WitpOM62PlOkDtTfXy6pxWyic_b-ap1OOL00cdn9WOPaX5ND7NC7cwZwy3njX8anF7wQl9AvUvMlIXFIJI9na_HalUsb6nxnnThQdzXDVQ3y1MYvq8RGswy2ln7xOvH2x7Md9vgd1Tz6hQuVOGW7zdBJSPJJsxfcC0P9zx7iOs-Mmcsx6yW1BE0bWvYZsVwZujhOL_CFwZoQHstLCAJryGYe5JXDiDOh86trLOyqzc2bXxgA")
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
