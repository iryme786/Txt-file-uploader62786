import os

API_ID = API_ID = 29320367

API_HASH = os.environ.get("API_HASH", "f8083ef747c160b7eb41095454f59f92")

BOT_TOKEN = os.environ.get("BOT_TOKEN", ":")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6559064772))

LOG = -1002757108362,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6705657501").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


