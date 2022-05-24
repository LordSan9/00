pip install requests
pip install telebot

import requests
import telebot


token = "5362583249:AAFGgCSW5b9Aqo9ciTkbbf1qU6jdyIQLvsU"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi,\nSend Your Channel Username to increase Views! \nBy: @trprogram - @ttrakos </strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def send(message):
    msg = message.text 
    
    bot.send_message(message.chat.id,f"<strong>Done Save Username, Wait Increase.. </strong>",parse_mode="html")
    if msg[0] == "@":
        msg = msg.replace("@","")
    count = 0
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0"
    }
    r2 = requests.get("https://telegram.software",headers=headers)
    XSRF_TOKEN = r2.cookies["XSRF-TOKEN"]
    telegramsoftware_session = r2.cookies["telegramsoftware_session"]
    r = requests.get("https://telegram.software/", headers=headers)
    print("done")
    i = str(r.text)
    token = i.split('<input type="hidden" name="_token" value="')[1]
    token2 = token.split('">')[0]
    token = token2
    def send_request(message):
            bot.send_message(message.chat.id,f"<strong>Done, Now Send Request</strong>",parse_mode="html")
            url = "https://telegram.software/make_views_order"
            headers = {
            "Host": "telegram.software",
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "155",
            "Origin": "https://telegram.software",
            "Connection": "close",
            "Referer": "https://telegram.software/",
            "Cookie": f"XSRF-TOKEN={XSRF_TOKEN}; telegramsoftware_session={telegramsoftware_session}; _ga_LDCYE0PVMB=GS1.1.1640463457.3.0.1640463459.58; _ga=GA1.2.1949754996.1640447487; _gid=GA1.2.760731106.1640447487; _ym_uid=1640440888262602307; _ym_d=1640447487; _ym_isad=2",
            "Upgrade-Insecure-Requests": "1"
            }
            data = {
            f"_token={token}&test_mode=on&number-days=1&slct-day=-&slct-moth=-&slct-year=-&link-channel={username}&speed-hour=1800&views=10000"
            }
            r = r.post(url,headers=headers,data=data)
            print("done") 
            bot.send_message(message.chat.id,"<strong>Done send 1000</strong>",parse_mode="html") 
            if r.text.find('You already used demo')>=0:
                bot.send_message(message.chat.id,"Error, Try Later")
  
pass
bot.polling() 
