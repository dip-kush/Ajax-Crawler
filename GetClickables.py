from urllib import urlopen
from bs4 import BeautifulSoup
from logger import LoggerHandler

logger = LoggerHandler(__name__)


class Clickables:

    def __init__(self):
        self.links = []
        self.buttons = []


def getLinks(domString):
    '''
    Returns all the anchor tags <a></a>
    Filtering the <a> tags with href = "#something"
    for eg <a href="#div1"> </a>
    because this leads to same page with no new state discovery
    '''

    validLinks = {'href': [], 'onclick': []}
    soup = BeautifulSoup(domString, 'html.parser')
    links = soup.find_all("a")
    buttons = soup.find_all("button")
    for link in links:
        link = str(link.get('href'))
        if len(link) == 0:
            pass
        else:
            validLinks['href'].append(link)
    for link in links:
        if link.get("onclick"):
            validLinks['onclick'].append(link.get("onclick"))        
    return validLinks


def onClickLinks(domString):
    '''
    Returns the <a> with on click property
    '''
    onClickLinks = []
    soup = BeautifulSoup(domString, 'html.parser')
    links = soup.findAll("a")
    for link in links:
        if link.get("onclick"):
            onClickLinks.append(link.get("onclick"))
    return onClickLinks


def getSubmitButtons(domString):
    '''
    Return the target of the submit buttons
    present in the form
    '''
    pass

def getButton(domString):
    ''' Get all the Buttons  <button> </button> '''

    pass


def GetDomElements(url):

    #urlHandle = urlopen(url);
    #dom = urlHandle.read()
    dom = open("page1").read()
    getLinks(dom)

# GetDomElements("https://selenium-python.readthedocs.org/navigating.html")
# GetDomString("http://www.w3schools.com/tags/tag_button.asp")
