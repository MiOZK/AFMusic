import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["المطور","مطور السورس","مبرمج السورس","الزعيم"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[سورس الزعيم](https://t.me/T_5_G)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @VVV5P ❫
◉ 𝙸𝙳      : ❪ `7118337980` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@T_5_G)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " قناة السورس", url=f"https://t.me/VVV5P"), 
                 ],[
                   InlineKeyboardButton(
                        "「مطور السورس 」", url=f"https://t.me/T_5_G"),
                ],

            ]

        ),

    )
@app.on_message(
    command(["مطور", "المطور"])
    & filters.group
  
)
async def kimmyy(client: Client, message: Message):
    usr = await client.get_users(OWNER)
    name = usr.first_name
    async for photo in client.iter_profile_photos(OWNER, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**⩹━★⊷⌯سورس الزعيم⌯⊶★━⩺**
                    
🔥 ¦𝚆𝙾𝙽𝙴𝚁 :[{usr.first_name}](https://t.me/{OWNER})
📀 ¦𝚄𝚂𝙴𝚁 :@{OWNER} 
🆔 ¦𝙸𝙳 :`{usr.id}`
 
**⩹━★⊷⌯سورس الزعيم⌯⊶★━⩺** """, 
reply_markup=InlineKeyboardMarkup(
          [               
            [            
              InlineKeyboardButton (name, url=f"https://t.me/{OWNER}")
            ],                   
          ]              
       )                 
    )                    
                    sender_id = message.from_user.id
                    sender_name = message.from_user.first_name
                    await app.send_message(OWNER, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
                    return await app.send_message(config.LOG_GROUP_ID, f"الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}")
      
