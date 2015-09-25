from urllib import urlopen
from bs4 import BeautifulSoup



class Clickables:
    def __init__(self):
        self.links = []
        self.buttons = []

'''
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
'''



def getLinks(domString):
    validLinks = []
    soup = BeautifulSoup(domString, 'html.parser')
    links = soup.find_all("a")
    buttons = soup.find_all("button")
    for link in links:
        link = str(link.get('href')) 
        if len(link)==0 or link[0] == '#':
            pass
        else:
             validLinks.append(link)
    return validLinks
  

 

def getButton(domString):
    pass
    


def GetDomElements(url):
    #urlHandle = urlopen(url);
    #dom = urlHandle.read()
    dom = open("page1").read()
    getLinks(dom)

#GetDomElements("https://selenium-python.readthedocs.org/navigating.html")   
#GetDomString("http://www.w3schools.com/tags/tag_button.asp")    
