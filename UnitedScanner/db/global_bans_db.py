from Scanner.db import db

GloballyBannedUsers = db.guser

GBANNED_LIST = set()


def gban_user(user_id, scanner, reason=None):
    GloballyBannedUsers.update_one(
        {"user_id": user_id}, {"$set": {"reason": reason, "scanner": scanner}}, upsert=True
    )
    __load_gbanned_userid_list()

def ungban_user(user_id):
    user = GloballyBannedUsers.find_one({"user_id": user_id})
    if user:
        GloballyBannedUsers.delete_one({"user_id": user_id})
        __load_gbanned_userid_list()


def is_user_gbanned(user_id):
    return user_id in GBANNED_LIST


def get_gbanned_user(user_id):
    return GloballyBannedUsers.find_one({"user_id": user_id})


def get_gban_list():
    return [x for x in GloballyBannedUsers.find()]


def num_gbanned_users():
    return len(GBANNED_LIST)


def __load_gbanned_userid_list():
    global GBANNED_LIST
    GBANNED_LIST = {x["user_id"] for x in GloballyBannedUsers.find()}

# create in memory userid to avoid disk access
__load_gbanned_userid_list()
