import urllib.parse
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.enums.parse_mode import ParseMode
from configs import Config 


db = Database(Var.DATABASE_URL, Var.SESSION_NAME)




@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=Config.START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=Config.START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=Config.HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=Config.HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=Config.ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=Config.ABOUT_BUTTONS
        )
    elif update.data == "dev":
        await update.message.edit_text(
            text=Config.DEV_TXT,
            reply_markup=Config.DEV_BUTTONS
        )
    elif update.data == "don":
        await update.message.edit_text(
            text=Config.DON_TXT,
            reply_markup=Config.DONATE_BUTTONS
        )
    else:
        await update.message.delete()

def get_media_file_size(m):
    media = m.video or m.audio or m.document
    if media and media.file_size:
        return media.file_size
    else:
        return None


def get_media_file_name(m):
    media = m.video or m.document or m.audio
    if media and media.file_name:
        return urllib.parse.quote_plus(media.file_name)
    else:
        return None


@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    # lang = getattr(Language, m.from_user.language_code)
    lang = getattr(Language, "en")
    # Check The User is Banned or Not
    if await db.is_user_banned(m.from_user.id):
        await b.send_message(
                chat_id=m.chat.id,
                text=Config.BAN_TXT,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
        return
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text=" **Sᴏʀʀʏ Sɪʀ, Yᴏᴜ Aʀᴇ Bᴀɴɴᴇᴅ Tᴏ Usᴇ Mᴇ. Cᴏɴᴛᴀᴄᴛ Mʏ [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗥𝗢𝗨𝗣](https://t.me/kr_join).**",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Jᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode=ParseMode.HTML
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<i>Sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i> <b><a href='http://t.me/Kr_Join'>[ ᴄʟɪᴄᴋ ʜᴇʀᴇ ]</a></b>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True)
                return
        await m.reply_photo(
            photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
            caption=Config.START_TEXT.format(m.from_user.first_name, m.from_user.id), 
            parse_mode=ParseMode.HTML,
            reply_markup=Config.START_BUTTONS, 
        )                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**𝘚𝘰𝘳𝘳𝘺 𝘚𝘪𝘳, 𝘠𝘰𝘶 𝘈𝘳𝘦 𝘉𝘢𝘯𝘯𝘦𝘥 𝘛𝘰 𝘜𝘴𝘦 𝘔𝘦. 𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘔𝘺 [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽](https://t.me/kr_join).**",
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ**!\n\n**Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")],
                         [InlineKeyboardButton("🔄 Refresh / Try Again", url=f"https://t.me/{(await b.get_me()).username}?start=KRBOTS_{usr_cmd}")
                        
                        ]]
                    ),
                    parse_mode=ParseMode.MARKDOWN
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍʏ [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽](https://t.me/kr_join).**",
                    parse_mode=ParseMode.MARKDOWN,
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))
        file_name = get_media_file_name(get_msg)
        file_size = humanbytes(get_media_file_size(get_msg))

        stream_link = "{}/{}/{}".format(Var.DOMAIN, get_msg.id, file_name) if Var.ON_HEROKU or Var.NO_PORT else \
            "{}/{}/{}".format(Var.DOMAIN,
                                     get_msg.id,
                                     file_name)

        msg_text ="""
<i><u>𝗬𝗼𝘂𝗿 𝗟𝗶𝗻𝗸 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲𝗱 !</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <code>{}</code>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🚸 Nᴏᴛᴇ : Tʜɪs ᴘᴇʀᴍᴀɴᴇɴᴛ Lɪɴᴋ, Nᴏᴛ Exᴘɪʀᴇᴅ</b>\n
<b>🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : ©️ @KR_BOTZ</b>
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Dᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ 📥", url=stream_link)]])
        )



@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_photo(
        photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
        caption=Config.ABOUT_TEXT.format(update.from_user.mention),
        reply_markup=Config.ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    # lang = getattr(Language, m.from_user.language_code)
    lang = getattr(Language, "en")
    # Check The User is Banned or Not
    if await db.is_user_banned(m.from_user.id):
        await b.send_message(
                chat_id=m.chat.id,
                text=Config.BAN_TXT,
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True
            )
        return
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. Cᴏɴᴛᴀᴄᴛ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode=ParseMode.MARKDOWN
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ Mʏ [𝗦𝘂𝗽𝗽𝗼𝗿𝘁 𝗚𝗿𝗼𝘂𝗽](https://t.me/kr_join).**",
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True)
            return
    await message.reply_photo(
        photo="https://graph.org/file/c72af6f77c6d164b81dd2.jpg",
        caption=Config.HELP_TEXT,
        parse_mode=ParseMode.HTML,
        reply_markup=Config.HELP_BUTTONS
        )

