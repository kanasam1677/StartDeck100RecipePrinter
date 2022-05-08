import dataclasses

#段組みの参考：https://qiita.com/kokardy/items/92e8f3b65c965e20de34
from reportlab.platypus import BaseDocTemplate, PageTemplate
from reportlab.platypus import Paragraph, Image, PageBreak, FrameBreak
from reportlab.platypus.frames import Frame
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4, portrait ,mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

@dataclasses.dataclass(frozen=True)
class DeckData:
    deckNum:str
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
        "fontSize":7,
        "leading":7,
        }
    deckNumStyle = ParagraphStyle(**style_dict)

    style_dict ={
        "name":"title",
        "fontName":"GenShinGothicPB",
        "fontSize":14,
        "leading":14,
        "alignment":1#TA_CENTER,
        }
    titleStyle = ParagraphStyle(**style_dict)

    style_dict ={
        "name":"description",
        "fontName":"GenShinGothicPN",
        "fontSize":10,
        "leading":10,
        "firstLineIndent":10,
        }
    descStyle = ParagraphStyle(**style_dict)

    para=Paragraph(data.deckNum,deckNumStyle)
    flowables.append(para)

    para=Paragraph(data.title,titleStyle)
    flowables.append(para)

    para=Paragraph(data.description,descStyle)
    flowables.append(para)

    para=Paragraph(data.cardListFilePath,deckNumStyle)
    flowables.append(para)


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
    testDeckList.append(DeckData("11", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("12", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("13", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("21", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("22", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("23", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("31", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("32", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("33", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("41", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("42", "test1", "description", "./tmpimage/test.png"))
    testDeckList.append(DeckData("43", "test1", "description", "./tmpimage/test.png"))
    MakePdf("test.pdf", testDeckList)
