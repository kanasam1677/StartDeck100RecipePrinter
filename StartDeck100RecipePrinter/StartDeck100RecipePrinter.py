import sys
import requests
from requests.exceptions import Timeout

args=sys.argv
if len(args) < 2:
    sys.stderr.write("出力するデッキ番号を改行区切りで並べたテキストファイルをドラッグアンドドロップしてください\n")
    exit(1)


print(args)


targetPageURL="https://www.pokemon-card.com/ex/si/index.html"

try:
    r= requests.get(targetPageURL, timeout=(3.0,7.5))
except Timeout:
    sys.stderr.write("サーバに接続できませんでした\n")
    exit(1)

if r.status_code != 200 :
    sys.stderr.write("ページを取得できませんでした\n")
    exit(1)

print(r.text)
