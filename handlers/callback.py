# (C) 2021 VeezMusic-Project

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from handlers.play import cb_admin_check
from helpers.decorators import authorized_users_only


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**๐ก here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("โธ pause", callback_data="cbpause"),
                    InlineKeyboardButton("โถ๏ธ resume", callback_data="cbresume"),
                ],
                [
                    InlineKeyboardButton("โฉ skip", callback_data="cbskip"),
                    InlineKeyboardButton("โน end", callback_data="cbend"),
                ],
                [InlineKeyboardButton("โ anti cmd", callback_data="cbdelcmds")],
                [InlineKeyboardButton("๐ group tools", callback_data="cbgtools")],
                [InlineKeyboardButton("๐ Close", callback_data="close")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

๐ก **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

โ **usage:**

1๏ธโฃ ban & temporarily ban user from your group:
   ยป type `/b username/reply to message` ban permanently
   ยป type `/tb username/reply to message/duration` temporarily ban user
   ยป type `/ub username/reply to message` to unban user

2๏ธโฃ mute & temporarily mute user in your group:
   ยป type `/m username/reply to message` mute permanently
   ยป type `/tm username/reply to message/duration` temporarily mute user
   ยป type `/um username/reply to message` to unmute user

๐ note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ก Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**๐ก Feature:** delete every commands sent by users to avoid spam in groups !

โ usage:**

 1๏ธโฃ to turn on feature:
     ยป type `/delcmd on`
    
 2๏ธโฃ to turn off feature:
     ยป type `/delcmd off`
      
โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ก Go Back", callback_data="cbback")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

โก __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("๐ Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("๐ Advanced Cmd", callback_data="cbadvanced"),
                ],
                [
                    InlineKeyboardButton("๐ Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("๐ Sudo Cmd", callback_data="cbsudo"),
                ],
                [InlineKeyboardButton("๐ Owner Cmd", callback_data="cbowner")],
                [InlineKeyboardButton("๐ Fun Cmd", callback_data="cbfun")],
                [InlineKeyboardButton("๐ก Go Back", callback_data="cbstart")],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

โก __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("๐ก Go Back", callback_data="cbstart")]]
        ),
    )
