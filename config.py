import os

class Config(object):
    DATABASE = os.environ.get("DB_URI")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5011359168").split())
    SUPPORT = os.environ.get("SUPPORT")
