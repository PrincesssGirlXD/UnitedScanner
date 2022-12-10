import asyncio
import sys

from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from UnitedScanner import LOGGER
from UnitedScanner.config import MONGO_DB_URI 


client = MongoClient()
client = MongoClient(MONGO_DB_URI, 27017)["UnitedScanner"]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, 27017)
db = motor["UnitedScanner"]
db = client["UnitedScanner"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(LOGGER.critical("Can't connect to mongodb! Exiting..."))
