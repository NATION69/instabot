import requests

import telebot

import uuid

from time import sleep

from telebot import types

uuid = uuid.uuid4()

Run = True

Sleep = 4

bot = telebot.TeleBot("1992936661:AAGKWEXdnHcNg53IXEvmujuWEfJzb6KS4OA")

Start = types.InlineKeyboardButton(text='Start ▶️', callback_data='Start ▶️')

Spam = types.InlineKeyboardButton(text='Spam', callback_data='Sp')

Hate = types.InlineKeyboardButton(text='Hate', callback_data='HATe')

Self = types.InlineKeyboardButton(text='Self', callback_data='SEl')

Nudity = types.InlineKeyboardButton(text='Nudity', callback_data='NU')

Sale = types.InlineKeyboardButton(text='Sale', callback_data='SA')

Violence = types.InlineKeyboardButton(text='Violence', callback_data='V')

Me = types.InlineKeyboardButton(text='Me', callback_data='ME')

Harassment = types.InlineKeyboardButton(text='Harassment', callback_data='H')

re = types.InlineKeyboardButton(text='Reboot Bot ✳️', callback_data='Reboot Bot ✳️')

stop = types.InlineKeyboardButton(text='Stop 🛑', callback_data='s')

getid = types.InlineKeyboardButton(text='Get Id 📮', callback_data='gi')

log = types.InlineKeyboardButton(text='Login ✅', callback_data='login1')

Done = 0

Error = 0

markup_inline12 = types.InlineKeyboardMarkup()

markup_inline12.add(stop)

@bot.message_handler(commands=['start'])

def start(message):

    if message.chat.type == 'private':

        markup_inline = types.InlineKeyboardMarkup()

        markup_inline.row_width = 2

        markup_inline.add(Start,log,re)

        bot.send_message(message.chat.id, f'*INSTAGRAM REPORT🤍*\n\n*Ξ DEVELOPER : @zzaaz*', parse_mode='markdown',reply_markup=markup_inline)

def Reboot(message):

    global Run,checked,Error,Done,mastercard,visa1

    Error = 0

    Done = 0

    open('Account.txt', 'w')

    Run = True

    bot.send_message(message.chat.id, text='''*𝗕𝗼𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 ▶️ 

 𝗖𝗹𝗶𝗰𝗸 /start  𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗯𝗼𝘁 (:*''', parse_mode='markdown')

@bot.callback_query_handler(func=lambda call: True)

def answer(call):

    try:

        global Run

        if call.data == 'Start ▶️':

            markup_inline = types.InlineKeyboardMarkup()

            markup_inline.row_width = 2

            markup_inline.add(Spam,Hate,Self,Nudity,Sale,Violence,Me,Harassment)

            bot.send_message(call.message.chat.id, text='*Choice*',parse_mode='markdown',reply_markup=markup_inline)

        if call.data == 'Sp':

            Spam_Rep(call.message)

        if call.data == 'HATe':

            Hate_Rep(call.message)

        if call.data == 'SEl':

            Self_Rep(call.message)

        if call.data == 'NU':

            Nudity_Rep(call.message)

        if call.data == 'SA':

            Sale_Rep(call.message)

        if call.data == 'V':

            Violence_Rep(call.message)

        if call.data == 'ME':

            Me_Rep(call.message)

        if call.data == 'H':

            Harassment_Rep(call.message)            

        if call.data == 'Reboot Bot ✳️':

            Reboot(call.message)

            bot.send_message(call.message.chat.id, text='⏳ 𝗣𝗹𝗲𝗮𝘀𝗲 𝗪𝗮𝗶𝘁 >>>> ')

        if call.data == 'V':

            check_Visa(call.message)

        if call.data == 'login1':

            sent = bot.send_message(call.message.chat.id, text='*UserName :*', parse_mode='markdown')

            bot.register_next_step_handler(sent, username)

        if call.data == 's':

            Run = False

            bot.send_message(message.chat.id, text='𝗜 𝗔𝗠 𝗦𝗧𝗢𝗣 ⏸')

        if call.data == 'gi':

            user1 = bot.send_message(call.message.chat.id, text='*UserName :*', parse_mode='markdown')

            bot.register_next_step_handler(user1, get_id)

    except:

        pass

def username(message):

    try:

        usernamee = message.text

        sent = bot.send_message(message.chat.id, text='*Password :*', parse_mode='markdown')

        bot.register_next_step_handler(sent, login, usernamee)

    except:

        pass

def login(message, usernamee):

    try:

        global sess

        paswwordd = message.text

        usernamee = usernamee

        url_log = 'https://i.instagram.com/api/v1/accounts/login/'

        headers_log = {

            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',

            "Accept": "/",

            "Accept-Encoding": "gzip, deflate",

            "Accept-Language": "en-US",

            "X-IG-Capabilities": "3brTvw==",

            "X-IG-Connection-Type": "WIFI",

            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",

            'Host': 'i.instagram.com',

            'Connection': 'keep-alive'}

        data_log = {

            '_uuid': uuid,

            'username': usernamee,

            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{paswwordd}',

            'queryParams': '{}',

            'optIntoOneTap': 'false',

            'device_id': uuid,

            'from_reg': 'false',

            '_csrftoken': 'missing',

            'login_attempt_count': '0'}

        reqqq = requests.post(url_log, headers=headers_log, data=data_log)

        if '"status":"ok"' in reqqq.text:

            sess = reqqq.cookies['sessionid']

            acccc = open("Account.txt", "w")

            acccc.write(usernamee + ':' + paswwordd)

            markup_inline = types.InlineKeyboardMarkup()

            markup_inline.add(getid)

            bot.send_message(message.chat.id, text='*Done Login Sir ✅!*', parse_mode='markdown',reply_markup=markup_inline)

        else:

            markup_inline2 = types.InlineKeyboardMarkup()

            markup_inline2.add(Add)

            bot.send_message(message.chat.id, text='*Error in account ❌!*', parse_mode='markdown',reply_markup=markup_inline2)

    except:

          pass

def get_id(message):

    global Id

    Target = message.text

    urlget = f"https://www.instagram.com/{Target}/?__a=1"

    hedlog = {

        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

        'accept-encoding': 'gzip, deflate, br',

        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

        'cache-control': 'max-age=0',

        'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; ds_user_id=45758615954; sessionid={sess}; csrftoken=VOEzWVpwFtEDr68pSSMZiHiRtyilHd89; rur=VLL',

        'sec-fetch-dest': 'document',

        'sec-fetch-mode': 'navigate',

        'sec-fetch-site': 'none',

        'sec-fetch-user': '?1',

        'upgrade-insecure-requests': '1',

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

    }

    re1 = requests.get(urlget, headers=hedlog).json()

    Id = str(re1['graphql']['user'].get('id'))

    if 'graphql' in re1:

        markup_inline = types.InlineKeyboardMarkup()

        markup_inline.add(Start)

        bot.send_message(message.chat.id, text='*Done Get Id ✅!*', parse_mode='markdown',reply_markup=markup_inline)

    else:

        markup_inline121 = types.InlineKeyboardMarkup()

        markup_inline121.add(log)

        bot.send_message(message.chat.id, text='*Error Get Id ❌!*\nUse Another Account', parse_mode='markdown',reply_markup=markup_inline121)

def Spam_Rep(message):

    global Run,Done,Error

    try:

        bot.send_message(message.chat.id,text='Started (:')

        while True:

            if Run == True:

                sleep(4)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '1',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

def Hate_Rep(message):

    global Run,Done,Error

    try:

        bot.send_message(message.chat.id,text='Started (:')

        while True:

            if Run == True:

                sleep(Sleep)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '6',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

def Self_Rep(message):

    global Run,Done,Error

    try:

        bot.send_message(message.chat.id,text='Started (:')

        while True:

            if Run == True:

                sleep(Sleep)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '2',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

def Nudity_Rep(message):

    global Run,Done,Error

    try:

        bot.send_message(message.chat.id,text='Started (:')

        while True:

            if Run == True:

                sleep(Sleep)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '4',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

def Sale_Rep(message):

    global Run,Done,Error

    try:

        bot.send_message(message.chat.id,text='Started (:')

        while True:

            if Run == True:

                sleep(Sleep)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '3',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

def Violence_Rep(message):

    global Run,Done,Error

    try:

        bot.send_message(message.chat.id,text='Started (:')

        while True:

            if Run == True:

                sleep(Sleep)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '5',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

def Me_Rep(message):

    global Run,Done,Error

    try:

        bot.send_message(message.chat.id,text='Started (:')

        while True:

            if Run == True:

                sleep(Sleep)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '8',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

def Harassment_Rep(message):

    global Run,Done,Error

    bot.send_message(message.chat.id,text='Started (:')

    try:

        while True:

            if Run == True:

                sleep(Sleep)

                urlreport = f"https://www.instagram.com/users/{Id}/report/"

                hedlog1 = {

                    'accept': '*/*',

                    'accept-encoding': 'gzip, deflate, br',

                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',

                    'content-length': '37',

                    'content-type': 'application/x-www-form-urlencoded',

                    'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sess}; rur=RVA',

                    'origin': 'https://www.instagram.com',

                    'referer': 'https://www.instagram.com/users/234234234/report/',

                    'sec-fetch-dest': 'empty',

                    'sec-fetch-mode': 'cors',

                    'sec-fetch-site': 'same-origin',

                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',

                    'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',

                    'x-ig-app-id': '936619743392459',

                    'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',

                    'x-instagram-ajax': '0edc1000e5e7',

                    'x-requested-with': 'XMLHttpRequest',

                }

                datareport = {

                    'source_name': '',

                    'reason_id': '7',

                    'frx_context': '',

                }

                re2 = requests.post(urlreport, data=datareport, headers=hedlog1)

                if re2.status_code == 200:

                    Done +=1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                else:

                    Error += 1

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*I AM STARTED BOSS ▶!\n\nΞ Done Report : {Done}\n\nΞ Error Report : {Error}\n\nΞ DEVELOPER : @zzaaz*',parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except:

        pass

bot.polling(True)
