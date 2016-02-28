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
        #print "ALL tag count %d %d" % (tagCount1, tagCount2)
        mintagCount = min(tagCount1,tagCount2)
        maxtagCount = max(tagCount1,tagCount2)
        if float(mintagCount)/float(maxtagCount) < 0.9:
            logger.info("Different States Huge Difference in Tag Count")
            return False
        diff1 = htmldiff(strippedDom1, strippedDom2)
        diff2 = htmldiff(strippedDom2,strippedDom1)
        if len(diff1) > len(diff2):
            diff = diff1
        else:
            diff = diff2

        bdiff = BeautifulSoup(diff)
        ins = ''.join(str(bdiff.findAll("ins")))
        delete = ''.join(str(bdiff.findAll("del")))
        print cleanDom(delete)
        diffDom = cleanDom(ins)
        print diffDom

        if diffDom!="[]":
            diffTagCount,diffStrippedDom = traverseDom(diffDom)
        else:
            if hash(strippedDom1) ==  hash(strippedDom2):
                return True
            else:
                return False
        logger.info("tag count %d %d" % (diffTagCount, tagCount1))
        if (float(diffTagCount)/float(tagCount1))*100 > 5:
            return False
        logger.info("STATE ALREADY EXIST")
        #print dom1
        #print dom2
        return True

def getDomDiff(parentDom, childDom):
    html = htmldiff(parentDom, childDom)
    bshtml = BeautifulSoup(html)
    ins = ''.join(str(bshtml.findAll("ins")))
    diffDom = cleanDom(ins)
    return diffDom

def traverseDom(domString):
    out = StringIO()
    domString = str(tidy.parseString(domString))
    domString = clean_html(domString)
    tree   = etree.HTML(domString.replace('\r', ''))
    domString = '\n'.join([ etree.tostring(stree, pretty_print=True, method="xml")
                          for stree in tree ])
    tagCount = 0
    dom = xml.dom.minidom.parseString(domString)
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
