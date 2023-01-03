import os
import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class Config(object):

    START_TEXT = """
**⍟ Hᴇʟʟᴏ Mʏ Fʀɪᴇɴᴅ {} ⍟ \n \n ⍟ Mʏ Nᴀᴍᴇ Iꜱ [『Fɪʟᴇs 2 Lɪɴᴋ Bᴏᴛ』](https://t.me/KR_File2link_Bot)
✌︎ I Aᴍ PᴏᴡᴇʀFᴜʟ 🧛‍♂️ Fɪʟᴇs 2 Lɪɴᴋ Bᴏᴛ  
 🚀 Sᴇᴇ Mʏ Pᴏᴡᴇʀ ⚡.....!!
⚜️ Sʜᴀʀᴇ Aɴᴅ Sᴜᴘᴘᴏʀᴛ Us 💖......!!!

🔹𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸
🔞 Pᴏʀɴ Cᴏɴᴛᴇɴᴛs Lᴇᴀᴅs Yᴏᴜ Tᴏ Pᴇʀᴍᴀɴᴇɴᴛ Bᴀɴ Fʀᴏᴍ Aʟʟ BOTS**

"""

    BAN_TXT = """
_Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ._

**Cᴏɴᴛᴀᴄᴛ <a href=https://t.me/kr_join>Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ</a> Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**
"""


    HELP_TEXT = """
🎆 𝐇𝐎𝐖 𝐓𝐎 𝐔𝐒𝐄 𝐅𝐈𝐋𝐄𝐒 𝟐 𝐋𝐈𝐍𝐊 𝐁𝐎𝐓
<b>🔘sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ (ᴏʀ) ᴍᴇᴅɪᴀ ғʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ....
🔘 ᴛʜɪs ʙᴏᴛ ᴡɪʟʟ sᴇɴᴅ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ
🔘 ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ sᴛʀᴇᴀᴍ ғɪʟᴇs[ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ] ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀ
🔘 ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ᴍᴏɴᴏ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ
🔘 ᴛʜɪs ʙᴏᴛ sʜᴀʀᴇs ᴛʜᴇ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ʏᴏᴜ.
🔘 ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛᴇᴅ ɪɴ ᴄʜᴀɴɴᴇʟs. ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ᴡᴏʀᴋᴀʙʟᴇ...!
🔘 ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ : @KR_Join

🔹𝗪𝗔𝗥𝗡𝗜𝗡𝗚 🚸
🔞 𝐏𝐨𝐫𝐧 𝐂𝐨𝐧𝐭𝐞𝐧𝐭𝐬 𝐋𝐞𝐚𝐝𝐬 𝐘𝐨𝐮 𝐓𝐨 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐁𝐚𝐧 𝐅𝐫𝐨𝐦 𝐀𝐥𝐥 𝐁𝐨𝐭𝐬
️ 
⚜️ Bᴏᴛ Aɴʏ Issᴜᴇs Cᴏɴᴛᴀᴄᴛ Mᴇ
@MrTamil_KiD </b>
"""

    ABOUT_TEXT = """
<b>╔══❰ 𝗙𝗜𝗟𝗘𝗦 𝟮 𝗟𝗜𝗡𝗞 𝗕𝗢𝗧 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖 Mʏ Nᴀᴍᴇ : <a href='https://t.me/KR_File2link_Bot'>『Fɪʟᴇs 2 Lɪɴᴋ Bᴏᴛ』</a>
║┣⪼👦 Oᴡɴᴇʀ : <a href=https://t.me/MR_tamil_kid>Ꮋ ค ℘ ℘ ꪗ 👻 Ҝiᗪ</a>
║┣⪼👨‍💻 Dᴇᴠ : <a href=https://t.me/LastDrogz>Lᴀsᴛ 🐲 Dʀᴏɢᴢ</a>
║┣⪼📢 Uᴘᴅᴀᴛᴇ : <a href=https://t.me/kr_botz>𝗞𝗥 ⚠︎ 𝗕ᴏᴛᴢ</a>
║┣⪼❣️ Sᴜᴘᴘᴏʀᴛ : <a href=https://t.me/kr_join>𝗞𝗥 👽 𝗝ᴏɪɴ</a>
║┣⪼📡 Sᴇʀᴠᴇʀ : <a href=https://t.me/MRtamil_kid>𝗩𝗣𝗦</a>
║┣⪼🗣️ Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Pʏᴛʜᴏɴ3</a>
║┣⪼📚 Lɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>  
║┣⪼🗒️ Vᴇʀsɪᴏɴ : V 1.0.0 [ Bᴇᴛᴀ ]
║╰━━━━━━━━━━━━━━━➣
╚═════❰ @KR_Botz ❱═════❍ </b>
"""
    DON_TXT = """
<b>💗 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐝𝐨𝐧𝐚𝐭𝐢𝐨𝐧
Dᴏɴᴀᴛᴇ Us Tᴏ Kᴇᴇᴘ Oᴜʀ Sᴇʀᴠɪᴄᴇs Cᴏɴᴛɪɴᴏᴜsʟʏ Aʟɪᴠᴇ 😢
Yᴏᴜ Cᴀɴ Sᴇɴᴅ Aɴʏ Aᴍᴏᴜɴᴛ 
Dᴏɴᴀᴛᴇ Oɴʟʏ Oɴᴇ Rᴜᴘᴇᴇ 🥲
Of 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ 😊
📨 Pᴀʏᴍᴇɴᴛ Mᴇᴛʜᴏᴅs:
 
GᴏᴏɢʟᴇPᴀʏ / Pᴀʏᴛᴏɴ / PʜᴏɴPᴀʏ / PᴀʏPᴀʟ
 
 Oʀ Dᴏɴᴀᴛᴇ: Mᴇssᴀɢᴇ Mᴇ @MR_Tamil_KiD </b>
"""

    DEV_TXT = "<a href=https://t.me/MrTamil_KiD/5>Cʟɪᴄᴋ Hᴇʀᴇ</a>"

########################## BUTTONS TXT ########################## 

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('♡︎ Cᴏɴᴛᴀᴄᴛ 🧛‍♂️ Aᴅᴍɪɴ ♡︎', url=f'http://t.me/mr_tamil_kid')
        ],[
        InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇ', url='https://t.me/kr_botz'),
        InlineKeyboardButton('⚡ Sᴜᴘᴘᴏʀᴛ', url='https://t.me/kr_join')
        ],[
        InlineKeyboardButton("👨‍💻 Mʏ Fᴀᴛʜᴇʀ", url="https://t.me/mrtamil_kid")
        ],[
        InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
        ]]
    )

    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("💸 Dᴏɴᴀᴛᴇ", callback_data="don")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
        ]]
    )

    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' Dᴏɴᴀᴛᴇ 💸 Mᴇ ', callback_data='don')
        ],[
        InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇ", url= "https://t.me/KR_Botz"),
        InlineKeyboardButton("👨‍💻 Dᴇᴠs 🥷", callback_data = "dev")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data = "home"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
        ]]
    )

    DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ",
                                             url="https://t.me/mr_tamil_kid")
        ],[
        InlineKeyboardButton("⛺ Hᴏᴍᴇ", callback_data="home"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data="close")
        ]]
    ) 

    DEV_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton('๑۩ tค๓เl ۞ التاميل ۩๑', url='https://t.me/mr_tamil_kid'),
        ],[
        InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data = "about"),
        InlineKeyboardButton("🗑 Cʟᴏsᴇ", callback_data = "close")
        ]]
    ) 
