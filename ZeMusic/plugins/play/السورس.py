import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","الزعيم","السورس", "سورس الزعيم"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/04b2f1f1c808dc49db35b.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ  قناة السورس (t.me/VVV5P)
么 [َ جروب الزعيم](t.me/EEEW2)
么 [َ مطور السورس ](t.me/T_5_G)
╰──── • ◈ • ────╯
⍟ 𝙎𝙐𝙍𝙎 𝙈𝙄𝙐𝙕𝙄𝙆 𝘼𝙇𝙕𝘼𝙀𝙄𝙈  """,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  مطور السورس  . 🕷 › ", url=f"https://t.me/T_5_G"),
                ],[
                    InlineKeyboardButton(
                        "‹ سورس›", url=f"https://t.me/VVV5P"), 
                    InlineKeyboardButton(
                        "‹ جروب السورس›", url=f"https://t.me/EEEW2"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
