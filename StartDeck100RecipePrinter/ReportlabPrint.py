import dataclasses
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

@dataclasses.dataclass(frozen=True)
class DeckData:
    deckNum:str
    title:str
    description:str
    cardListFilePath:str

def MakePdf(filename:str, data:list):
    newPdfName = filename + ".pdf"
    page = canvas.Canvas(newPdfName, pagesize=portrait(A4))
    pdfmetrics.registerFont(TTFont("GenShinGothicPB", "./fonts/GenShinGothic-P-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("GenShinGothicPN", "./fonts/GenShinGothic-P-Normal.ttf"))
    page.setFont("GenShinGothicPB",20)
    page.drawCentredString(100,100,data[0].title)
    page.showPage()
    page.save()

    return newPdfName


if __name__ == "__main__":
    testDeckList=[]
    testDeckList.append(DeckData("11", "test1", "description", "./tmpimage/test.png"))
    MakePdf("test.pdf", testDeckList)
