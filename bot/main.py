from pyrogram import Client
from bot.app import app

from bot.handlers import start

if __name__ == "__main__":
    print("Bot Started...")
    app.run()