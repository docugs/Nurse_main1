import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from hellbot.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>๐ฅ๐ฅษฆษสสษฎึt ษจs ึีผสษจีผษ๐ฅ๐ฅ</b></i>
<i><b>โผ รwรฑรชr โ</i></b> : ใ <a href='tg://user?id={}'>{}</a> ใ
โญโโโโโโโโโโโโโโ
โฃโ <b>ยป Telethon ~</b> <i>{}</i>
โฃโ <b>ยป Alexa ~</b> <i>{}</i>
โฃโ <b>ยป Sudo ~</b> <i>{}</i>
โฃโ <b>ยป Uptime ~</b> <i>{}</i>
โฃโ <b>ยป Ping ~</b> <i>{}</i>
โฐโโโโโโโโโโโโโโ
<b><i>ยปยปยป <a href='https://t.me/YMMLLL'>[ Alexa Bot ]</a> ยซยซยซ</i></b>
"""

msg = """{}\n
<b><i>๐ ๐ฑ๐๐ ๐๐๐๐๐๐ ๐</b></i>
<b>Telethon โ</b>  <i>{}</i>
<b>Alexa โ</b>  <i>{}</i>
<b>Uptime โ</b>  <i>{}</i>
<b>Abuse โ</b>  <i>{}</i>
<b>Sudo โ</b>  <i>{}</i>
"""
#-------------------------------------------------------------------------------

@hell_cmd(pattern="alive$")
async def up(event):
    cid = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    start = datetime.datetime.now()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, HELL_USER, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=PIC, caption=omk, parse_mode="HTML")
    await hell.delete()



@hell_cmd(pattern="hell$")
async def hell_a(event):
    cid = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cid[0], cid[1], cid[2]
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>ยปยป ะฝัโโะฒฯั ฮนั ฯะธโฮนะธั ยซยซ</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "โ Harmless Module"
).add()
