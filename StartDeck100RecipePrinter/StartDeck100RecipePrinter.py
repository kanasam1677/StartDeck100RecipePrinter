import sys
import requests
from requests.exceptions import Timeout

targetPageURL="https://www.pokemon-card.com/ex/si/index.html"

try:
    r= requests.get(targetPageURL, timeout=(3.0,7.5))
except Timeout:
    sys.stderr.write("サーバに接続できませんでした")
    exit(1)

if r.status_code != 200 :
    sys.stderr.write("ページを取得できませんでした")
    exit(1)

print(r.text)
