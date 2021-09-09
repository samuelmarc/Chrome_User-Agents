import requests
from requests.structures import CaseInsensitiveDict
import re

def list():
    users_agents = """
If you've gotten this far, it's because you don't know the user-agents available, so here's a list of all of them:

Windows: windows = ua.user_agents('windows')
print(windows[0])
print(windows[1])
print(windows[2])

Mac Os: ua.user_agents('mac_os')

Linux: ua.user_agents('linux')

Iphone: ua.user_agents('iphone')

Ipad: ua.user_agents('ipad')

Ipod: ua.user_agents('ipod')
Android: android = ua.user_agents('android')
print(android[0])
print(android[1])
print(android[2])
print(android[3])
print(android[4])
print(android[5])
print(android[6])
print(android[7])

All are updated according to this page:
https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
"""
    return users_agents

def user_agents(plataform):
    url = "https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome"
    headers = CaseInsensitiveDict()
    headers["Host"] = "www.whatismybrowser.com"
    headers["Connection"] = "keep-alive"
    headers["Cache-Control"] = "max-age=0"
    headers["device-memory"] = "4"
    headers["dpr"] = "1"
    headers["viewport-width"] = "1366"
    headers["rtt"] = "100"
    headers["downlink"] = "10"
    headers["ect"] = "4g"
    headers["sec-ch-ua"] = '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"'
    headers["sec-ch-ua-mobile"] = "?0"
    headers["sec-ch-ua-full-version"] = '"93.0.4577.63"'
    headers["sec-ch-ua-arch"] = '"x86"'
    headers["sec-ch-ua-platform"] = '"Windows"'
    headers["sec-ch-ua-platform-version"] = '"10.0.0"'
    headers["sec-ch-ua-model"] = '""'
    headers["sec-ch-prefers-color-scheme"] = 'dark'
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    headers["Sec-Fetch-Site"] = "same-site"
    headers["Sec-Fetch-Mode"] = "navigate"
    headers["Sec-Fetch-User"] = "?1"
    headers["Sec-Fetch-Dest"] = "document"
    headers["Accept-Language"] = "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        RegExp = re.findall(r'<span class="code">(.*?)</span>', resp.text)
        if 'windows' in plataform:
                return [RegExp[0], RegExp[1], RegExp[2]]
        else:
            if 'mac_os' in plataform:
                    return RegExp[3]
            else:
                if 'linux' in plataform:
                        return RegExp[4]
                else:
                    if 'iphone' in plataform:
                            return RegExp[5]
                    else:
                        if 'Ipad' in plataform:
                                return RegExp[6]
                        else:
                            if 'Ipod' in plataform:
                                    return RegExp[7]
                            else:
                                if 'android' in plataform:
                                        return [RegExp[8], RegExp[9], RegExp[10], RegExp[11], RegExp[12], RegExp[13], RegExp[14], RegExp[15]]
                                else:
                                    return 'Invalid user agent platform, please read the list using print(web_browser.list())'
    else:
        return 'An error occurred in the process of getting data from the page, please try again later'
