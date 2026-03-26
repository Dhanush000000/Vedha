# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "25038048"))
    API_HASH = getenv("API_HASH", "09e892474901472e030fcdd53fb7384a")
    BOT_TOKEN = getenv("BOT_TOKEN", "8795241058:AAE_P6Y-ADpFY8PYC8bHPJ32NdL5rOR_NZI")
    SESSION_STRING = getenv("SESSION_STRING", "")
    SUDO = list(map(int, getenv("SUDO", "5798247275 5612704084").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://kumar167:kumar167@cluster0.mi8qi5l.mongodb.net/?appName=Cluster0")

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
