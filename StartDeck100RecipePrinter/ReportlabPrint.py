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
    for y in range(cutNum[1]):
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
        "name":"title",
        "fontName":"GenShinGothicPB",
        "fontSize":20,
        "leading":20,
        "firstLineIndent":20,
        }
    style = ParagraphStyle(**style_dict)
    para=Paragraph(data.deckNum,style)
    flowables.append(para)
    para=Paragraph(data.title,style)
    flowables.append(para)
    para=Paragraph(data.description,style)
    flowables.append(para)
    para=Paragraph(data.cardListFilePath,style)
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
