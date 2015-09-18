from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GetClickables import GetDomElements, getLinks
from selenium.webdriver.support.ui import WebDriverWait
from State import StateMachine, NodeData
import networkx as nx
import Queue


def initState(domString, link, title, driver):
    
    fsm = StateMachine()
    node = NodeData()
    node.link = link
    node.domString = domString
    node.title = title
    node.visited = 0
    node.clickables = getLinks(domString)
    print "i was here"
    print node.clickables
    fsm.addNode(node)
    Crawl(fsm, driver)
    
def Crawl(fsm, driver):
    graph = fsm.graph 
    queue = Queue.Queue()
    queue.put(0)
        
    while queue.empty() == False:
        curNode = queue.get()
        graph.node[curNode]['nodedata'].visited = 1
        clickables = graph.node[curNode]['nodedata'].clickables
        domString = graph.node[curNode]['nodedata'].domString
        for clickable in clickables:
            print clickable
            driver.find_element_by_xpath("//a[@href='"+clickable+"']").click()            
            WebDriverWait(driver, 2000)
            print driver.title
            driver.back()
            
    
    
     
    
    
    
    
    
