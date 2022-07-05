from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
import humanize
from Translation import mr
from helper.database import  insert 
from helper.utils import not_subscribed 

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**sᴏʀʀʏ ᴅᴜᴅᴇ ʏᴏᴜʀ ɴᴏᴛ ᴊᴏɪɴᴅ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs  ʙᴏᴛ 🙏 **",
       reply_markup=InlineKeyboardMarkup([
           [ InlineKeyboardButton(text="📢ᴊᴏɪɴ ᴍʏ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ📢", url=client.invitelink)]
           ])
       )
    
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo="https://telegra.ph/file/955a798ca2c38c87d67e0.jpg",
       caption=f"""👋 ʜᴀɪ {message.from_user.mention} \nɪᴍ ᴀ sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇ + ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏᴠᴇʀᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ 🤩 \nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ : @CS_Teamchannel \n 🤩""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ 👨‍💻", url='https://t.me/Sanoob_Achu_18')
          ],[
          InlineKeyboardButton('📢 ᴜᴘᴅᴀᴛᴇs', url='https://t.me/CS_Teamchannel'),
          InlineKeyboardButton('👥 sᴇʀɪᴇs ɢʀᴏᴜᴘ', url='https://t.me/CS_Series')
          ],[
          InlineKeyboardButton('🔔 ᴀʙᴏᴜᴛ ', callback_data='about'),
          InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help')
          ]]
          )
       )
    return

@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size)
    fileid = file.file_id
    await message.reply_text(
        f"__What do you want me to do with this file?__\n**File Name** :- `{filename}`\n**File Size** :- `{filesize}`",
        reply_to_message_id = message.id,
        reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 ʀᴇɴᴀᴍᴇ",callback_data = "rename"),
        InlineKeyboardButton("ᴄᴀɴᴄᴇʟ ✖️",callback_data = "cancel")  ]]))


@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 ʜᴀɪ {query.from_user.mention} \nɪᴍ ᴀ sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇ + ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏᴠᴇʀᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ 🤩 \nʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ: @CS_Teamchannel \n 🤩""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("👨‍💻 ᴏᴡɴᴇʀ 👨‍💻", url='https://t.me/Sanoob_Achu_18')
                ],[
                InlineKeyboardButton('📢 ᴜᴘᴅᴀᴛᴇs', url='https://t.me/CS_Teamchannel'),
                InlineKeyboardButton('👥 sᴇʀɪᴇs ɢʀᴏᴜᴘ', url='https://t.me/CS_Series')
                ],[
                InlineKeyboardButton('🔔 ᴀʙᴏᴜᴛ', callback_data='about'),
                InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', callback_data='help')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("🔒 𝙲𝙻𝙾𝚂𝙴", callback_data = "close"),
               InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





