import os
from os import getenv

from dotenv import load_dotenv

from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCnMks33wfF9mRhqXLU813wagcRX0mRWvUQDRuo7EfrvyBDoFKcVxcS_-nG709V0t_rBYpUHIUb3mEUaLq6j4ie-1iBtyPAkJWeSBoizyo1C5BMQCZNccfUOCxj2bwyJjIihuIQ7RYU0L4ED6kw8kGQFGThIgdFDg4z37rGrLDTwQV8FHZfmcW-O3kz8fxlQbLOIgRlY_Y5rzeWnppi5WSxRPAIzTeob8KrOnPyeCRMH65hKNkd6tdzVX-6DUOT_k7jIDfMG-1dz4c827wnHjTuy9uABOrMutz2NK_rakjNb-e0oZ7F_YH1BVjg6-_U7Ayq84Dz0N2czLFDTYcPMDdBdquPPgA")
BOT_TOKEN = getenv("BOT_TOKEN", "2061760260:AAH5oGUxogL5ZkUTX4yctjSqEFXN4aNyi7E")
BOT_NAME = getenv("BOT_NAME", "ZYPHERx_BOT")
BG_IMAGE = getenv("BG_IMAGE", "https://raw.githubusercontent.com/theshashankk/HinataBot/main/background1.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/976bb4ee2f66857cfa317.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/5dd2446cfe99c08a7490a.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/e3c0c7e817f95448473a1.jpg")
ALIVE_IMG = getenv('ALIVE_IMG', 'https://telegra.ph/file/1c041dbf79dba92070da0.mp4')
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "ZYPHERx_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "zypher_assist")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ZYPHERXSUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZYPHERxSUPPORT")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "andreobee_xD")
# fill with DISABLE if you want to disable pm-permit
PMPERMIT = getenv("PMPERMIT", "ENABLE")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID", '2003485925'))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/Team-Zypher/ZYPHERx"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
