import dataclasses

#段組みの参考：https://qiita.com/kokardy/items/92e8f3b65c965e20de34
from reportlab.platypus import BaseDocTemplate, PageTemplate
from reportlab.platypus import Paragraph, FrameBreak
from reportlab.platypus.flowables import Image, Spacer
from reportlab.platypus.frames import Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4, portrait ,mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

@dataclasses.dataclass(frozen=True)
class DeckData:
    deckNum:int
    title:str
    description:str
    cardListFilePath:str

def MakeFrames():
    cutNum = (3,3)
    cardSize=(62 * mm, 86 * mm) #実際のカードサイズは63x88なので1周り小さく
    paperSize=portrait(A4)
    margin = ((paperSize[0] - cardSize[0]*cutNum[0])/2,(paperSize[1] - cardSize[1]*cutNum[1])/2)
    frames=[]
    for y in reversed(range(cutNum[1])): #左下原点のようだが左上から並べたいので逆順
        for x in range(cutNum[0]):
            frames.append(
                Frame(margin[0] + cardSize[0]*x,
                      margin[1] + cardSize[1]*y,
                      cardSize[0],
                      cardSize[1],
                      showBoundary=1
                      )
            )

    return frames


def DrawDeckData(flowables:list, data:DeckData):


    style_dict ={
        "name":"deckNum",
        "fontName":"GenShinGothicPN",
        "fontSize":4,
        "leading":4,
        }
    deckNumStyle = ParagraphStyle(**style_dict)

    style_dict ={
        "name":"title",
        "fontName":"GenShinGothicPB",
        "fontSize":12,
        "leading":12,
        "alignment":1#TA_CENTER,
        }
    titleStyle = ParagraphStyle(**style_dict)

    style_dict ={
        "name":"description",
        "fontName":"GenShinGothicPN",
        "fontSize":9,
        "leading":9,
        "firstLineIndent":9,
        }
    descStyle = ParagraphStyle(**style_dict)

    para=Paragraph(str(data.deckNum),deckNumStyle)
    flowables.append(para)

    para=Paragraph(data.title,titleStyle)
    flowables.append(para)

    para=Paragraph(data.description,descStyle)
    flowables.append(para)

    space = Spacer(1*mm,1*mm)
    flowables.append(space)

    fixSize=( 40 * mm, 46 * mm)
    image = Image(data.cardListFilePath, fixSize[0], fixSize[1])
    flowables.append(image)


def MakePdf(filename:str, dataList:list):
    newPdfName = filename + ".pdf"
    doc = BaseDocTemplate(newPdfName, pagesize=portrait(A4)) #portrait(A4)はA4縦の意。landscape(A4)でA4横
    pdfmetrics.registerFont(TTFont("GenShinGothicPB", "./fonts/GenShinGothic-P-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("GenShinGothicPN", "./fonts/GenShinGothic-P-Normal.ttf"))
    frames = MakeFrames()
    page_temprate = PageTemplate("frames", frames = frames)
    doc.addPageTemplates(page_temprate)
    
    flowables = []
    for ind, data in enumerate(dataList):
        DrawDeckData(flowables, data)
        flowables.append(FrameBreak())

    flowables.pop() #最後につく不要なFrameBreakを削除

    doc.multiBuild(flowables)

    return newPdfName


if __name__ == "__main__":
    testDeckList=[]
    testDeckList.append(DeckData(11, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    testDeckList.append(DeckData(12, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    testDeckList.append(DeckData(13, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    testDeckList.append(DeckData(21, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    testDeckList.append(DeckData(22, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    #testDeckList.append(DeckData(23, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    #testDeckList.append(DeckData(31, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    #testDeckList.append(DeckData(32, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    #testDeckList.append(DeckData(33, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    #testDeckList.append(DeckData(41, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    #testDeckList.append(DeckData(42, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    #testDeckList.append(DeckData(43, "ここにデッキの説明文が入ります", "ここにデッキの解説文が入ります(使い方など)", "./tmpimage/test.png"))
    MakePdf("sample", testDeckList)
