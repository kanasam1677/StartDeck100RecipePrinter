import sys
import os
import requests
from urllib import parse
from requests.exceptions import Timeout
from bs4 import BeautifulSoup

import ReportlabPrint

tmpImageFolder="./tmpimage/"

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

pictureCacheList = []
def GetPicture(relativePath:str):
    targetPageBaseURL="https://www.pokemon-card.com/ex/si/"
    fullURL=parse.urljoin(targetPageBaseURL, relativePath)
    filename = os.path.split(fullURL)[1]
    filePath = tmpImageFolder + filename
    if fullURL not in pictureCacheList:
        
        try:
            r= requests.get(fullURL, timeout=(3.0,7.5))
        except Timeout:
            sys.stderr.write("サーバに接続できませんでした\n")
            exit(1)

        if r.status_code != 200 :
            sys.stderr.write("画像を取得できませんでした\n")
            exit(1)
        with open(filePath,"wb") as f:
            f.write(r.content)
        print("サーバより%sを取得しました"%filename)
        pictureCacheList.append(fullURL)
    else:
        print("%sの取得をスキップします"%filename)
    return filePath


def File2DeckNum(filepath:str):
    with open(filepath, "r") as f:
        text = f.read()
    splited=text.split()
    if len([i for i in splited if not i.isdigit()]) != 0:
        sys.stderr.write("デッキ番号ファイルに不正な文字が含まれています\n")
        exit(1)
    return splited




def GetDeckContents(deckNum, souped:BeautifulSoup):
    print("デッキ番号%sのデータを取得"%deckNum)
    targetDeckContentsClass="modal-deck-%s" % deckNum
    deckContents=souped.find("div",class_=targetDeckContentsClass)
    title = deckContents.find("h3").text
    desc = deckContents.find("div",class_="lyt-group-content").text.replace(title,"")
    desc = desc.replace(title,"").replace("\n","")
    cardList = deckContents.find("div",class_="lyt-group-image").find("img")
    cardListFilePath=GetPicture(cardList["src"])
    return ReportlabPrint.DeckData(deckNum ,title ,desc ,cardListFilePath)
    

def MakeSheet(filepath:str, souped:BeautifulSoup):
    print("%sのシート作成を開始します" % filepath)
    deckNums=File2DeckNum(filepath)
    deckList=[]
    for num in deckNums:
        deckList.append(GetDeckContents(num,souped))
    print("%sのシート作成が完了しました" % filepath)

args=sys.argv
if len(args) < 2:
    sys.stderr.write("出力するデッキ番号を改行区切りで並べたテキストファイルをドラッグアンドドロップしてください\n")
    exit(1)

if not os.path.exists(tmpImageFolder):
    os.mkdir(tmpImageFolder)

print("公式サイトより情報を取得しています...")
pageContents=GetPageContents()
print("取得完了しました")


for filepath in args[1:]:
    MakeSheet(filepath, pageContents)






