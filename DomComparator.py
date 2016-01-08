import hashlib
import xml.dom.minidom
from Queue import *
from logger import LoggerHandler
from lxml.html.diff import htmldiff
from BeautifulSoup import BeautifulSoup
logger = LoggerHandler(__name__)
   

def cleanDom(dom):
    repl = ["</ins>,", "<ins>,","<ins>", "</ins>"]
    for key in repl:
        dom = dom.replace(key, "")
    return dom
     
def hash(dom):
    return(hashlib.sha256(dom.encode('utf-8')).hexdigest())

def checkExistState(dom1,dom2):
    if hash(dom1) == hash(dom2):
        return True
    else:
        return False
        
def getDomDiff(parentDom, childDom):
    html = htmldiff(parentDom, childDom)
    bshtml = BeautifulSoup(html)
    ins = ''.join(str(bshtml.findAll("ins")))  
    diffDom = cleanDom(ins)
    return diffDom      

'''
file1 = open("page1", "r").read()
file3 = open("page1", "r").read()
benign1="<html><head><title>Title1</title></head><body><b>Hi</b><a href='a'></a><p>hello1</p></body></html>"
benign2 = None
benign2="<html><head><title>Title2</title></head><body><b>Hi</b><a href='a'></a><p>hello2</p></body></html>"
hostile1="<html><head><title>Title3</title></head><body><b>Hi</b><a href='a'></a><p>hello3</p></body></html>"
htmlCompare(file1,None,file3)
'''
