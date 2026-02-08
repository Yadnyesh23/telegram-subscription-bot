from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.app import app
from bot.config import FORCE_SUB_CHANNEL

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    if FORCE_SUB_CHANNEL:
        try:
            member = await client.get_chat_member(
                FORCE_SUB_CHANNEL,
                message.from_user.id
            )
        except:
            buttons = [
                [InlineKeyboardButton(
                    "🔔 Join Channel",
                    url=f"https://t.me/{FORCE_SUB_CHANNEL.lstrip('@')}"
                )]
            ]
            await message.reply(
                "🚫 You must join our channel to use this bot.",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return

    await message.reply(
        "👋 Welcome!\n\nThis bot provides access via paid subscription.\n\nClick below to continue.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("💳 Subscribe", callback_data="subscribe")]
        ])
    )
