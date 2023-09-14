import random,requests,re 
from flask import Flask, jsonify,request
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
    gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
    gttt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
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
app = Flask('__name__')
@app.route('/')
def hello():
  return 'Bùi Tuấn Đạt'
@app.route('/', methods=['POST'])
def calculate():
  data = request.form
  tk = str(data['tk'])
  mk = str(data['mk'])
  fa=str(data['fa'])
  kkk=geta(tk,mk,fa)
  return jsonify(kkk)
if __name__=='__main__':
  app.run()


  
