# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 
INST_COOKIES = """
# wtite up here insta cookies
"""
YTUB_COOKIES = """
# write here yt cookies
"""

#Required Variables 
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))

#Fancy edits for personalise - Required
COMPLETED_BLOCKS = getenv("COMPLETED_BLOCKS", "✅") #Replace ✅ with any other single alphabet or emoji
FRACTIONAL_BLOCKS = getenv("FRACTIONAL_BLOCKS", "🟨") #Replace 🟨 with any other single alphabet or emoji
REMAINING_BLOCKS = getenv("REMAINING_BLOCKS", "🟥") #Replace 🟥 with any other single alphabet or emoji
PRGRES_FTNOTE = getenv("PRGRES_FTNOTE", "All Set ✅") #Replace All set ✅ with your own tag line

#Button edits for personalise - Required
OWNER_USERNAME = getenv("OWNER_USERNAME", "Doldotby") #Replace with your own tg username without @
CHANNEL_USERNAME = getenv("CHANNEL_USERNAME","+rsngXN2zMJA5NTBl") #Replace value after "https://t.me/" of your channel/group link if private channel/group or value after "@" if public channel
DCUSTOM_RENAME_TAG = getenv("DCUSTOM_RENAME_TAG", "") #Add your default custom rename tag default is none, can be added from settings of bot after deployment also

#Additional Configuration Options: 
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTBU_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
