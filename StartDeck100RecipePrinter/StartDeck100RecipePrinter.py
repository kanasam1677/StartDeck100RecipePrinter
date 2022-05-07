import sys
import requests
from requests.exceptions import Timeout
from bs4 import BeautifulSoup


def GetPageContents():
    targetPageURL="https://www.pokemon-card.com/ex/si/index.html"
    try:
        r= requests.get(targetPageURL, timeout=(3.0,7.5))
    except Timeout:
        sys.stderr.write("サーバに接続できませんでした\n")
        exit(1)

    if r.status_code != 200 :
        sys.stderr.write("ページを取得できませんでした\n")
        exit(1)
    
    souped=BeautifulSoup(r.text)

    return souped

def File2DeckNum(filepath:str):
    f=open(filepath, "r")
    text = f.read()
    f.close()
    splited=text.split()
    if len([i for i in splited if not i.isdigit()]) != 0:
        sys.stderr.write("デッキ番号ファイルに不正な文字が含まれています\n")
        exit(1)
    return splited

def GetDeckContents(deckNum, souped:BeautifulSoup):
    targetDeckContentsClass="modal-deck-%s" % deckNum
    deckContents=souped.find("div",class_=targetDeckContentsClass)
    print(deckContents)

def MakeSheet(filepath:str, souped:BeautifulSoup):
    print("%sのシート作成を開始します" % filepath)
    deckNums=File2DeckNum(filepath)
    for num in deckNums:
        GetDeckContents(num,souped)
    print("%sのシート作成が完了しました" % filepath)

args=sys.argv
if len(args) < 2:
    sys.stderr.write("出力するデッキ番号を改行区切りで並べたテキストファイルをドラッグアンドドロップしてください\n")
    exit(1)

print("公式サイトより情報を取得しています...")
pageContents=GetPageContents()
print("取得完了しました")


for filepath in args[1:]:
    MakeSheet(filepath, pageContents)






