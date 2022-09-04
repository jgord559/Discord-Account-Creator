import requests
import base64
import time
import json
from itertools import cycle
import string
import random
from threading import active_count, Thread

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxy_list = []
proxy_cycle = cycle(proxy_list)

with open('proxy.txt') as f:
    for line in f:
        proxy_list.append(line.strip())

threadcount = int(input("Please enter number of threads to use: "))

def usr():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))

def gen():
    while True:
        global __dcfduid
        global __sdcfduid
        proxy = next(proxy_cycle)
        #print(proxy)
        proxies = {
            "http": "http://" + proxy,
            "https":"https://" + proxy}
        getcookie = requests.get("https://discord.com/register", proxies=proxies, verify=False)
        __dcfduid = getcookie.cookies['__dcfduid']
        __sdcfduid = getcookie.cookies['__sdcfduid']

        ##fingerprint
        xtrackfull = str(base64.b64encode(bytes('{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-GB","browser_user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36","browser_version":"103.0.5060.134","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":9999,"client_event_source":null}', "utf-8")))
        xtrackquotes = xtrackfull.replace("'", "")
        xtrack = xtrackquotes.replace("b", "", 1)
        #print(xtrack)

        fingerprinthed = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'connection': 'keep-alive',
            'host': 'discord.com',
            'referer': 'https://discord.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
            'x-track': xtrack}
        fingerprintreq = requests.get("https://discord.com/api/v9/experiments", headers=fingerprinthed, proxies=proxies, verify=False)
        global fingerprint
        fingerprint = fingerprintreq.json()['fingerprint']
        #print(fingerprint)

        sendcap = requests.get("http://2captcha.com/in.php?key=ENTER_KEY_HERE&method=hcaptcha&sitekey=4c672d35-0701-42b2-88c3-78380b0db560&pageurl=https://discord.com/register&json=1")
        capid = sendcap.json()['request']
        print(capid)
        time.sleep(20)
        getcap = requests.get(f"http://2captcha.com/res.php?key=ENTER_KEY_HERE&action=get&id={capid}&json=1")
        checkcap = getcap.json()['status']
        if checkcap == 0:
            time.sleep(7)
            getcap = requests.get(f"http://2captcha.com/res.php?key=ENTER_KEY_HERE&action=get&id={capid}&json=1")
            solve = getcap.json()['request']
        else:
            solve = getcap.json()['request']
            pass
        print(getcap.text)

        registerhed = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'connection': 'keep-alive',
            'content-length': '4621',
            'content-type': 'application/json',
            'cookie': f'__dcfduid={__dcfduid}; __sdcfduid={__sdcfduid}',
            'host': 'discord.com',
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/register',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
            'X-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-GB',
            'x-fingerprint': fingerprint,
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjUwNjAuMTM0IFNhZmFyaS81MzcuMzYiLCJicm93c2VyX3ZlcnNpb24iOiIxMDMuMC41MDYwLjEzNCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNDAzNTUsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'}

        username = usr()
        email = username
        email += "@gmail.com"
        password = "ENTER_PASS_HERE"
        registerdata = {"fingerprint": f"{fingerprint}", "email": f"{username}@gmail.com", "username": f"{username}", "password": "Doodle135!", "invite": "null", "consent": "true", "date_of_birth": "1998-05-04", "gift_code_sku_id": "null", "captcha_key": f"{solve}", "promotional_email_opt_in": "false"}
        registerdatajson = json.dumps(registerdata)
        registerurl = "https://discord.com/api/v9/auth/register"
        registerreq = requests.post(registerurl, headers=registerhed, data=registerdatajson, proxies=proxies, verify=False)
        tokenfile = registerreq.json()['token']
        accinfo = open("accounts.txt", "a")
        accinfo.write(email)
        accinfo.write(":")
        accinfo.write(password)
        accinfo.write(":")
        accinfo.write(tokenfile)
        accinfo.write("\n")
        accinfo.close()
        print(registerreq.text)

        ###email verify send
        emailverifyurl = "https://discord.com/api/v9/auth/verify/resend"
        emailverifyhed = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en;q=0.9',
            'authorization': tokenfile,
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-GB',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAzLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MDU3NSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
        #emailverifyreq = requests.post(emailverifyurl, headers=emailverifyhed, proxies=proxies, verify=False)



for x in range(threadcount):
    Thread(target=(gen)).start()
    time.sleep(0.5)
