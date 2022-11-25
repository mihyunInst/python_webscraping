import requests
url = "https://velog.io/@hold1593"
# 내 user agent string 구하는 사이트
# https://www.whatismybrowser.com/detect/what-is-my-user-agent/
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("agenttest.html", 'w', encoding='utf8') as f:
    f.write(res.text)