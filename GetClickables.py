from urllib import urlopen

class AnchorTags:
    def __init__(self):
        self.Tags = []
    def addTag(self, link):
        self.Tags.append(link)

    def showAll(self):
        for tag in self.Tags:
            print tag
        


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


def GetDomString(url):
    urlHandle = urlopen(url);
    dom = urlHandle.read()
    print dom
    getAnchorTags(dom)
   

GetDomString("https://selenium-python.readthedocs.org/navigating.html")   
    
