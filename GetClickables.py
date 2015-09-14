from urllib import urlopen

class Clickables:
    def __init__(self):
        self.anchorTags = AnchorTags()
        self.buttonLinks = ButtonLinks()

class AnchorTags:
    def __init__(self):
        self.Tags = []
    
    def addTag(self, link):
        self.Tags.append(link)

    def showAll(self):
        for tag in self.Tags:
            print tag
        

class ButtonLinks:
    def __init__(self):
        self.Buttons = []
    
    def addButton(self, button):
        self.Buttons.append(button)

    def showAll(self):
        for button in self.Buttons:
            print button




def getAnchorTags(domString):
    anchorTag = AnchorTags()
    domStringLength = len(domString)
    startPos = 0
    while startPos < domStringLength:
        anchorStartPos = domString.find("<a ", startPos)
        if anchorStartPos == -1:
            break
        anchorEndPos = domString.find(">", anchorStartPos+1)
        tagString = domString[anchorStartPos:anchorEndPos+1]
        startPos = anchorEndPos+1
        anchorTag.addTag(tagString)
         
    anchorTag.showAll()        

def getButtonLinks(domString):
    buttonLink = ButtonLinks()
    domStringLength = len(domString)
    startPos = 0
    while startPos < domStringLength:
        buttonStartPos = domString.find("<button ", startPos)
        if buttonStartPos == -1:
            break
        buttonEndPos = domString.find("</button>", buttonStartPos+1)
        buttonString = domString[buttonStartPos:buttonEndPos+9]
        startPos = buttonEndPos+1
        buttonLink.addButton(buttonString)
         
    buttonLink.showAll()        




def GetDomString(url):
    urlHandle = urlopen(url);
    dom = urlHandle.read()
    #print dom
    #getAnchorTags(dom)
    getButtonLinks(dom)

   
#GetDomString("https://selenium-python.readthedocs.org/navigating.html")   
GetDomString("http://www.w3schools.com/tags/tag_button.asp")    
