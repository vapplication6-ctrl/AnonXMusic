from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("30804214", 0))
        self.API_HASH = getenv("868c14bb613d143a45d1eaa5a17d8e1b")

        self.BOT_TOKEN = getenv("8960458103:AAHhFY4J52hJq4z7Xk_kKiTL-g-2LEA1J-8")
        self.MONGO_URL = getenv("mongodb+srv://arise:xenonop106@arise.a8gu8rp.mongodb.net/?appName=arise")

        self.LOGGER_ID = int(getenv("-1004331727741", 0))
        self.OWNER_ID = int(getenv("7983098956", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("1BVtsOMYBuwFwVPXeMdZyjb5W0EW6lKjgxoXbhSTg2xQUhoyE18orBWxPNit8_UOEqfDhZ7u-EY5UXMZfVNz05mljiP6qxzov7T6fteAcIkIsDPXWcbM4FTXR72UiUmA72ImCoFn1vU_ts8Z6EsCryvNwaBILGYFXRlQ9E_Wll2V00IeOPneM4EeOjwmKuXEox5_SBgJ364TnbggeP-IsLb87WBKmXBkPR9lOA7QrJl6C2FEPjVToE2OaRtQZUFkZC_UTBaRLEyGimsLC4xCqk_cAmwHxfkIdVyOwFBlz7pRG27J3azr_KAMO8KRDbON9nqFODuwo_uthf8K26nhDMLlTTAg1rqc=1BVtsOMYBuwFwVPXeMdZyjb5W0EW6lKjgxoXbhSTg2xQUhoyE18orBWxPNit8_UOEqfDhZ7u-EY5UXMZfVNz05mljiP6qxzov7T6fteAcIkIsDPXWcbM4FTXR72UiUmA72ImCoFn1vU_ts8Z6EsCryvNwaBILGYFXRlQ9E_Wll2V00IeOPneM4EeOjwmKuXEox5_SBgJ364TnbggeP-IsLb87WBKmXBkPR9lOA7QrJl6C2FEPjVToE2OaRtQZUFkZC_UTBaRLEyGimsLC4xCqk_cAmwHxfkIdVyOwFBlz7pRG27J3azr_KAMO8KRDbON9nqFODuwo_uthf8K26nhDMLlTTAg1rqc=", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/fallenx")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
