# (c) @EliteCraft_Studios

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸🤖 **My Name:** [𝐅𝐢𝐥𝐞 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭](https://t.me/{BOT_USERNAME})
│
├🔸📝 **Language:** [𝐏𝐲𝐭𝐡𝐨𝐧𝟑](https://www.python.org)
│
├🔹📚 **Library:** [𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦](https://docs.pyrogram.org)
│
├🔹📡 **Hosted On:** [𝐇𝐞𝐫𝐨𝐤𝐮](https://heroku.com)
│
├🔸👨‍💻 **Developer:** [★彡 𝐃𝐢𝐠𝐢𝐭𝐚𝐥 彡★](https://t.me/Elite_Craft_Official) 
│
├🔹👥 **Bot Support:** [𝐒𝐮𝐩𝐩𝐨𝐫𝐭](https://t.me/EliteCraft_Support)
│
├🔸🔔 **Bot Updates:** [𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/EliteCraft_Studios)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [💞 𝐃𝐢𝐠𝐢𝐭𝐚𝐥 💞](https://t.me/Elite_Craft_Official) 

𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 𝘪𝘴 𝘚𝘶𝘱𝘦𝘳 𝘕𝘰𝘰𝘣. 𝘑𝘶𝘴𝘵 𝘓𝘦𝘢𝘳𝘯𝘪𝘨 𝘧𝘳𝘰𝘮 𝘖𝘧𝘧𝘪𝘤𝘪𝘢𝘭 𝘋𝘰𝘤𝘴. 𝘈𝘯𝘥 𝘚𝘦𝘦𝘬𝘪𝘯𝘨 𝘏𝘦𝘭𝘱 𝘍𝘳𝘰𝘮 𝘗𝘳𝘰 𝘊𝘰𝘥𝘦𝘳\𝘯 **@God_Luffy_ati**

𝘪𝘧 𝘠𝘰𝘶 𝘞𝘢𝘯𝘵 𝘵𝘰 𝘋𝘰𝘯𝘢𝘵𝘦 𝘖𝘶𝘳 𝘩𝘢𝘳𝘥 𝘞𝘰𝘳𝘬. 𝘠𝘰𝘶 𝘊𝘢𝘯 𝘊𝘰𝘯𝘵𝘢𝘤𝘵 𝘛𝘩𝘦 𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳. 

𝘈𝘭𝘴𝘰 𝘙𝘦𝘮𝘦𝘮𝘣𝘦𝘳𝘴 𝘛𝘩𝘢𝘵 𝘋𝘦𝘷𝘦𝘭𝘰𝘱𝘦𝘳 𝘞𝘪𝘭𝘭 𝘋𝘦𝘭𝘦𝘵𝘦 𝘈𝘥𝘶𝘭𝘵𝘴 𝘊𝘰𝘯𝘵𝘦𝘯𝘵𝘴 𝘍𝘳𝘰𝘮 𝘋𝘢𝘵𝘢𝘣𝘢𝘴𝘦. 𝘚𝘰 𝘉𝘦𝘵𝘵𝘦𝘳 𝘥𝘰𝘯'𝘵 𝘚𝘵𝘰𝘳𝘦 𝘛𝘩𝘰𝘴𝘦 𝘒𝘪𝘯𝘥 𝘖𝘧 𝘛𝘩𝘪𝘯𝘨𝘴.
[**𝘋𝘰𝘯𝘢𝘵𝘦 𝘔𝘦**](https://www.paypal.me/ChandanS854) (𝐏𝐚𝐲𝐏𝐚𝐥)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
