import requests,re,random,json,os ,base64
from time import sleep
from telebot import types
import telebot
import datetime,time
def GetToken2FA(code):
  try:
    code =code.replace(' ','')
    get=requests.get(f'https://2fa.live/tok/{code}').json()
    token=get['token']
    return token 
  except:
    return False
def geta(tk,mk,fa):
  try:
    proxy="kjxguvty-rotate:yo0oe8zjholc@p.webshare.io:80"
    ss=requests.Session()
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
    list=['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H']
    gtt=random.choice(list) 
    gttt=random.choice(list)
    android_version=str(random.randrange(6,13))
    ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
    ss.headers={'User-Agent':ua_string}
    ss.proxies= {'http': f'http://{proxy}','https': f'http://{proxy}',}
    data={
    "locale":"vi_VN",
    "format":"json",
    "email":tk,
    "password":mk,
    "access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "generate_session_cookies":True,}
    dulieu=data.copy()
    kq=ss.post('https://graph.facebook.com/auth/login',json=data)
    print(kq.text)
    if 'session_cookies' in kq.text:
      tokenu=kq.json()['access_token']
      coki = ";".join(i["name"]+"="+i["value"] for i in kq.json()["session_cookies"])
    elif 'two_factor' in kq.text:
      tokenfa=GetToken2FA(fa)
      if tokenfa == False:
        return {'status':False,'msg':0}
      data.update({"password":tokenfa,"twofactor_code":tokenfa,"userid" : kq.json()['error']['error_data']['uid'],"first_factor" : kq.json()['error']['error_data']['login_first_factor'],"credentials_type" : 'two_factor',})
      kq=ss.post('https://graph.facebook.com/auth/login',json=data)
      if 'session_cookies' in kq.text:
        tokenu=kq.json()['access_token']
        coki = ";".join(i["name"]+"="+i["value"] for i in kq.json()["session_cookies"])
      else:
        return {'status':False,'msg':1}
    else:
      return {'status':False,'msg':2}
    tokend=ss.post('https://graph.facebook.com/auth/create_session_for_app',data={"locale": "vi_VN","format": "json","new_app_id": "275254692598279","access_token": tokenu,}).json()['access_token'] 
    datr=coki.split('datr=')[1]
    dulieu.update({'access_token':'6628568379|c1e620fa708a1d5696fb991c1bde5662','machine_id':datr})
    tokeny=requests.post('https://graph.facebook.com/auth/login',json=dulieu,headers={'User-Agent':ua_string},proxies= {'http': f'http://{proxy}','https': f'http://{proxy}',}).json()['access_token']
    ttacc=requests.get(f'https://graph.facebook.com/me/?access_token={tokend}').json()
    uidacc=ttacc['id']
    nameacc=ttacc['name']
    return {'status':True,'u':tokenu,'d':tokend,'y':tokeny,'i':uidacc,'n':nameacc,'c':coki}
  except:
    return {'status':False,'msg':3}
bot = telebot.TeleBot('6400253338:AAE58YX4ro-kJXU14roxUX0bfS8XwQlzL-4')
@bot.message_handler(commands=['get'])
def getv1(message):
  bot.send_chat_action(message.chat.id, 'typing')
  uidnguoidung=str(message.from_user.id)+'v1'
  try:
    #0 Get Thất Bại 2 Fa
    #1 Sai 2 FA
    #2 Sai Pass
    #3 Sự cố không zác định
    
    if len(message.text.split('/get ')[1].split(' ')) == 2:
      tk=message.text.split('/get ')[1].split(' ')[0]
      mk=message.text.split('/get ')[1].split(' ')[1]
      fa=""
    elif len(message.text.split('/get ')[1].split(' ')) ==3:
      tk=message.text.split('/get ')[1].split(' ')[0]
      mk=message.text.split('/get ')[1].split(' ')[1]
      fa=message.text.split('/get ')[1].split(' ')[2]
    else:
      tk=message.text.split('/get ')[1].split(' ')[100]
    start_time = time.time()
    print(start_time)
    kq=geta(tk,mk,fa)
    end_time= round(time.time()-start_time,2)
    if kq['status']==True:
      text=f"""
𝐆𝐄𝐓 𝐓𝐇À𝐍𝐇 𝐂Ô𝐍𝐆 👇 

𝐈𝐃: `{kq['i']}`
𝐍𝐀𝐌𝐄: `{kq['n']}`

𝐀𝐍𝐃𝐑𝐎𝐈𝐃: `{kq['u']}`

𝐈𝐎𝐒: `{kq['y']}`

𝐅𝐁 𝐋𝐈𝐓𝐄: `{kq['d']}`

𝐂𝐎𝐎𝐊𝐈𝐄: `{kq['c']}`

admin: @buituandat|{end_time}s
"""
    else:
      dang=kq['msg']
      if dang==0:
        text="👉 `Vui lòng nhập mã 2FA (Mã gồm 32 chữ cái và số in hoa không cách)`"
      if dang==1:
        text=f"👉 `Vui lòng nhập chính xác mã 2FA của tài khoản: {tk} (Mã gồm 32 chữ cái và số in hoa không cách)`"
      if dang==2:
        text=f"Có thể gặp các lỗi sau\n👉 `Sai tài khoản hoặc mật khẩu(Thử đổi lại mật khẩu khi đúng thông tin mà vẫn thất bại)`\n👉 `Bị block đăng nhập`"
      if dang==3:
        text=f"👉 `Xảy ra sự cố không xác định vui lòng báo admin: @buituandat`"
      text=f"𝐆𝐄𝐓 𝐓𝐇Ấ𝐓 𝐁Ạ𝐈\n\n{text}\n\n admin: @buituandat|{end_time}s"
    bot.reply_to(message, re.escape(text),parse_mode='MarkdownV2')
  except:
    text="𝐇ƯỚ𝐍𝐆 𝐃Ẫ𝐍 𝐒Ử 𝐃Ụ𝐍𝐆\nSử dụng lệnh [`/get`] để get token&cookie\n\nVí dụ:\n 👉 [`/get 100071234567 pass`] là đối với những tài khoản không có xác thực 2 yếu tố\n👉 [`/get 100071234567 pass QWEIF71JF0JS82JCN1MF91HC82KA02IF`] là đối với các tài khoản có mã xác thực 2 yếu tố \n\n👉Lưu ý: mã xác bao gồm 32 chữ cái in hoa và số chỉ ghi liền với nhau như trên và không có khoảng cách,có thể sử dụng bot để xoá khoảng cách trước khi nhập ví dụ gửi cho bot 1 đoạn tin nhắn sau là `6RP2 DQFO TAH2 QS2R 7RGQ HACY 24JD EPPQ` bot sẻ trả về 1 đoạn tin nhắn không cách"
@bot.message_handler(func=lambda message: True)
def echo_all(message):
  list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
  kq=True
  mes=message.text.replace(' ','')
  sl=len(mes)
  if sl == 32:
    for i in mes:
      if i not in list:
        kq=False
    if kq == True:
      bot.reply_to(message, f'𝘾𝙤𝙙𝙚:\n\n`{mes}`',parse_mode='MarkdownV2')
    
bot.polling()
#parse_mode='MarkdownV2'
