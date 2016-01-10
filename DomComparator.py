import hashlib
import xml.dom.minidom
from Queue import *
from logger import LoggerHandler
from lxml.html.diff import htmldiff
from BeautifulSoup import BeautifulSoup
import tidy
from lxml import etree
from lxml.html.clean import clean_html
import os, sys
from StringIO import StringIO
logger = LoggerHandler(__name__)
   
out = StringIO()

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
        tagCount1, strippedDom1 = traverseDom(dom1)
        tagCount2, strippedDom2 = traverseDom(dom2)
        diff = htmldiff(strippedDom1, strippedDom2)
        bdiff = BeautifulSoup(diff)
        ins = ''.join(str(bdiff.findAll("ins")))
        diffDom = cleanDom(ins)
        diffTagCount,diffStrippedDom = traverseDom(diffDom)                
        if (float(diffTagCount)/float(tagCount1))*100 > 10:
            return False
        return True
        
def getDomDiff(parentDom, childDom):
    html = htmldiff(parentDom, childDom)
    bshtml = BeautifulSoup(html)
    ins = ''.join(str(bshtml.findAll("ins")))  
    diffDom = cleanDom(ins)
    return diffDom      
    
    
def traverseDom(document):
    document = str(tidy.parseString(document))
    document = clean_html(document)
    #print data
    tree   = etree.HTML(document.replace('\r', ''))
    document = '\n'.join([ etree.tostring(stree, pretty_print=True, method="xml") 
                          for stree in tree ])
    tagCount = 0
    dom = xml.dom.minidom.parseString(document)
    q = Queue() 
    nodes = dom.childNodes
    
    for node in nodes:
        q.put(node)
    while(q.empty() == False):
        cur  = q.get()
        tagCount+=1
        if cur.nodeName == '#text':
            cur.nodeValue = ""
            tagCount-=1

        if cur.attributes:
            keys = cur.attributes.keys()
            for key in keys:
                cur.attributes[key].value = ""
        l = len(cur.childNodes)
        i = 0
        while i < l:
            q.put(cur.childNodes[i]) 
            i+=1 
    dom.writexml(out)
    s = out.getvalue()
    return (tagCount, s)

'''
file1 = open("page1", "r").read()
file3 = open("page1", "r").read()
benign1="<html><head><title>Title1</title></head><body><b>Hi</b><a href='a'></a><p>hello1</p></body></html>"
benign2 = None
benign2="<html><head><title>Title2</title></head><body><b>Hi</b><a href='a'></a><p>hello2</p></body></html>"
hostile1="<html><head><title>Title3</title></head><body><b>Hi</b><a href='a'></a><p>hello3</p></body></html>"
htmlCompare(file1,None,file3)
'''
