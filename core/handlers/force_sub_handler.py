# (c) @cute_girl_rani

import asyncio
from configs import Config
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_subscribe(bot, cmd):
    invite_link = None
    try:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/movie4ubotschannel).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="𝗖𝘂𝘁𝗲 𝗴𝗶𝗿𝗹 𝗥𝗮𝗻𝗶 𓃦)
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/movie4ubotschannel).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return
