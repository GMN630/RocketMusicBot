import config


ADMIN = """
<u>**ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs :**</u>


/pause
» ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.

/resume
» ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.

/skip ᴏʀ /next
» sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.

/end ᴏʀ /stop
» ᴇɴᴅ ᴛʜᴇ ᴄᴜʀᴇᴇɴᴛ ᴏɴɢᴏɪɴ sᴛʀᴇᴀᴍ."""


AUTH = """
<u>**ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴀᴜᴛʜ/ᴜɴᴀᴜᴛʜ ᴀɴʏ ᴜsᴇʀ :**</u>

• ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴄᴀɴ sᴋɪᴩ, ᴩᴀᴜsᴇ, ʀᴇsᴜᴍᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.


/auth [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.

/unauth [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ.

/authusers 
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ."""


PLAY = """
<u>**ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴩʟᴀʏ sᴏɴɢs :**</u>


/play <sᴏɴɢ ɴᴀᴍᴇ/ʏᴛ ᴜʀʟ>
» sᴛᴀʀᴛs ᴩʟᴀʏɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴏɴ ᴠᴄ.

/queue
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ɪɴ ᴛʜᴇ ǫᴜᴇᴜᴇ.

/lyrics [sᴏɴɢ]
» sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʟʏʀɪᴄs ᴏғ ᴛʜᴇ sᴇᴀʀᴄʜᴇᴅ sᴏɴɢ."""


TOOLS = """
<u>**sᴏᴍᴇ ᴜsᴇғᴜʟ ᴛᴏᴏʟs :**</u>


/ping
» ᴄʜᴇᴄᴋ ɪғ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ. [ɪғ ᴀʟɪᴠᴇ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.]

/start 
» sᴛᴀʀᴛs ᴛʜᴇ ʙᴏᴛ.

/help 
» sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʜᴇʟᴩ ᴍᴇɴᴜ ᴏғ ᴛʜᴇ ʙᴏᴛ.

/stats
» sʜᴏᴡs ᴛʜᴇ sʏsᴛᴇᴍ, ᴀssɪsᴛᴀɴᴛ, ᴍᴏɴɢᴏ ᴀɴᴅ sᴛᴏʀᴀɢᴇ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

/sudolist 
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ sᴜᴅᴏᴇʀs.


**ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs :**

/speedtest 
» ᴄʜᴇᴄᴋᴇʀ sᴇʀᴠᴇʀ sᴩᴇᴇᴅ ᴀɴᴅ ʟᴀᴛᴇɴᴄʏ ᴀɴᴅ ᴩɪɴɢ."""


OWNER = """
<u>**ᴄᴏᴍᴍᴀɴᴅs ᴛʜᴀᴛ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ʙʏ ᴏᴡɴᴇʀ ᴏғ ᴛʜᴇ ʙᴏᴛ :**</u>


/chatlist
» ʟɪsᴛ ᴀʟʟ ᴛʜᴇ ᴄʜᴀᴛs ᴡʜᴇʀᴇ ʙᴏᴛ ɪs ᴩʀᴇsᴇɴᴛ.

/maintenance on
» ᴇɴᴀʙʟᴇ ᴛʜᴇ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ.

/maintenance off
» ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ.

/restart 
» ʀᴇsᴛᴀʀᴛs ᴛʜᴇ ʙᴏᴛ ᴏɴ ʏᴏᴜʀ sᴇʀᴠᴇʀ.
"""


SUDO = f"""
<u>**ᴄᴏᴍᴍᴀɴᴅs ᴛʜᴀᴛ ᴄᴀɴ ᴏɴʟʏ ʙᴇ ᴜsᴇᴅ ʙʏ sᴜᴅᴏ ᴜsᴇʀs :**</u>


/clean
» ᴄʟᴇᴀɴ ᴀʟʟ ᴛʜᴇ ᴛᴇᴍᴩ ᴅɪʀᴇᴄᴛᴏʀɪᴇs.

/update 
» ғᴇᴛᴄʜ ᴜᴩᴅᴀᴛᴇs ғʀᴏᴍ ᴛʜᴇ ʀᴇᴩᴏ.

/activevc
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs ᴏɴ ʙᴏᴛ's sᴇʀᴠᴇʀ.

/gban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]
» ɢʟᴏʙᴀʟʟʏ ʙᴀɴs ᴀ ᴜsᴇʀ ɪɴ ᴀʟʟ ᴛʜᴇ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.

/ungban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]
» ɢʟᴏʙᴀʟʟʏ ᴜɴʙᴀɴs ᴛʜᴇ ɢ-ʙᴀɴɴᴇᴅ ᴜsᴇʀ.

/broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]
» ʙʀᴏᴀᴅᴄᴀsᴛ's ᴛʜᴇ ɢɪᴠᴇɴ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴛʜᴇ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.

/broadcast_pin [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]
» ʙʀᴏᴀᴅᴄᴀsᴛ's ᴛʜᴇ ɢɪᴠᴇɴ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ᴛʜᴇ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ ᴀɴᴅ ᴩɪɴ's ᴛʜᴇ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ.

/joinassistant [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ]
» ᴏʀᴅᴇʀ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴊᴏɪɴ ᴛʜᴀᴛ ᴄʜᴀᴛ.

/leaveassistant [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ]
» ᴏʀᴅᴇʀ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴄʜᴀᴛ.

/leavebot [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ/ɪᴅ]
» ᴏʀᴅᴇʀ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴛʜᴀᴛ ᴄʜᴀᴛ.

{config.ASS_HANDLER[0]}approve [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ᴀᴩᴩʀᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ᴛᴏ ᴩᴍ ᴏɴ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.

{config.ASS_HANDLER[0]}disapprove [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ᴅɪsᴀᴩᴩʀᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ᴛᴏ ᴩᴍ ᴏɴ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.

{config.ASS_HANDLER[0]}pfp [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴩʜᴏᴛᴏ] 
» ᴄʜᴀɴɢᴇs ᴛʜᴇ ᴩғᴩ ᴏғ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜᴜɴᴛ.

{config.ASS_HANDLER[0]}bio [ᴛᴇxᴛ] 
» ᴄʜᴀɴɢᴇs ᴛʜᴇ ʙɪᴏ ᴏғ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
"""
