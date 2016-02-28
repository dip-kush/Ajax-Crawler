from urllib import urlopen
from bs4 import BeautifulSoup
from logger import LoggerHandler
import re

logger = LoggerHandler(__name__)


class ClickableEntity:

    '''
    Initializing each Clickable Entity with TagName , Attribute ,
    AttributeValue

    def __init__(self, tag, attr, attrVal, tagNumber=0, xpath):
        self.tag = tag
        self.attr = attr
        self.attrVal = attrVal
        self.tagNumber = tagNumber
        self.xpath = ""
    '''
    def __init__(self, tag, attrs, xpath):
        self.tag = tag
        self.attrs = attrs
        self.xpath = xpath
        self.action = "click"

    #def __str__(self):
        #return self.tag+" "+self.attrs+" "+self.xpath


def getLinks(domString):
    '''
    Returns all the anchor tags <a></a>
    Filtering the <a> tags with href = "#something"
    for eg <a href="#div1"> </a>
    because this leads to same page with no new state discovery
    '''
    clickables = []
    tagName = "a"
    validLinks = {'href': [], 'onclick': []}
    soup = BeautifulSoup(domString, 'html.parser')
    links = soup.find_all("a")
    buttons = soup.find_all("button")
    for link in links:
        link = str(link.get('href'))
        if len(link) == 0:
            pass
        else:
            clickableEntity = ClickableEntity(tagName, "href", link)
            clickables.append(clickableEntity)
            #validLinks['href'].append(link)
    for link in links:
        if link.get("onclick"):
            clickableEntity = ClickableEntity(tagName, "onclick", link)
            clickables.append(clickableEntity)
            #validLinks['onclick'].append(link.get("onclick"))
    return clickables
    #return validLinks


def GetClickables(domString):
    clickables = []
    soup = BeautifulSoup(domString)
    tagname = ""
    anchor = soup.findAll("a")
    submit = soup.findAll("input",attrs={'type':'submit'})
    button = soup.findAll("input",attrs={'type':'button'})
    otherclickables = otherClickables(domString)
    totalclickables = anchor + submit + button + otherclickables


    for clickable in totalclickables:
        attrs = clickable.attrs
        #print attrs
        path = "//"
        path+=str(clickable.name)
        for key in attrs:
            #print attr
            path += "[@"+str(key)+"="+'"'+str(attrs[key])+'"'+"]"
        #print path
        #print attrs
        clickableEntity = ClickableEntity(clickable.name, clickable.attrs, path)
        clickables.append(clickableEntity)
    return clickables


def otherClickables(domString):
    '''
    Returns other clickables with attribute 'onclick' and 'onmouseover'
    '''
    otherClickables = []
    soup = BeautifulSoup(domString)
    onclickElements = soup.findAll(attrs={'onclick': re.compile(r".")})
    #onmouseoverElements = soup.findAll(attrs={'onmouseover': re.compile(r".")})
    elements = onclickElements
    for element in elements:
        if element.name != "a" or element.name != "input" or element.name != "input":
            otherClickables.append(element)
    del elements
    return otherClickables

    '''
    for element in onclickElements:
        clickableEntity = ClickableEntity(element.name, "onclick", element['onclick'])
        otherClickables.append(clickableEntity)
    for element in onmouseoverElements:
        clickableEntity = ClickableEntity(element.name, "onmouseover", element['onmouseover'])
        otherClickables.append(clickableEntity)
    '''


def frameExists(domString):
    '''
    Checks whether 'frame' element exist in source code
    '''
    soup = BeautifulSoup(domString)
    frame = soup.findAll("frame")
    if len(frame) == 0:
        return 0
    else:
        return 1


def getSubmitButtons(domString):
    '''
    Returns the submit buttons of forms with structure
    <input type="submit">
    <input type="button">
    '''
    buttons = []
    tagName = "input"
    soup = BeautifulSoup(domString, 'html.parser')
    typeSubmit = soup.findAll("input",attrs={'type':'submit'})
    typeButton = soup.findAll("input",attrs={'type':'button'})
    for count, element in enumerate(typeSubmit):
        clickableEntity = ClickableEntity(tagName, "type", "submit", count)
        buttons.append(clickableEntity)
    for count, element in enumerate(typeButton):
        clickableEntity = ClickableEntity(tagName, "type", "button", count)
        buttons.append(clickableEntity)
    return buttons



def GetDomElements(url):
    #urlHandle = urlopen(url);
    #dom = urlHandle.read()
    dom = open("page1").read()
    getLinks(dom)

# GetDomElements("https://selenium-python.readthedocs.org/navigating.html")
# GetDomString("http://www.w3schools.com/tags/tag_button.asp")
