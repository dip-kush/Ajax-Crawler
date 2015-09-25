from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GetClickables import GetDomElements, getLinks
from selenium.webdriver.support.ui import WebDriverWait
from State import StateMachine, NodeData
import matplotlib.pyplot as plt
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
        clickables = []
        clickables = graph.node[curNode]['nodedata'].clickables
        #print clickables
        domString = graph.node[curNode]['nodedata'].domString
        for clickable in clickables:
            #print clickable
            driver.find_element_by_xpath("//a[@href='"+clickable+"']").click()
            #make a new node add in the graph and the queue            
            newNode = NodeData()
            newNode.link = driver.current_url
            newNode.domString = driver.page_source
            newNode.clickables = getLinks(newNode.domString)
            print "the current node " + str(curNode) +  " "+ str(getLinks(domString))
            newNode.visited = 0
            newNode.title = driver.title
            print newNode.title
            fsm.addNode(newNode)
            nodeNumber = fsm.numberOfNodes()
            fsm.addEdges(curNode, nodeNumber-1)
            print "the number of node "+ str(nodeNumber)
            queue.put(nodeNumber-1)
            #print queue
            WebDriverWait(driver, 2000)
            #print driver.title
            driver.back()
        #print graph.nodes()
    print graph.edges()
    pos = nx.spring_layout(graph)
    labels = {k:graph.node[k]['nodedata'].title for k in graph.nodes()}
    print labels
    nx.draw_networkx_nodes(graph,pos)
    nx.draw_networkx_edges(graph,pos)
    nx.draw_networkx_labels(graph,pos,labels)          
    #nx.draw(graph,node_size=3000,nodelist=graph.nodes(),node_color='b')
    #nx.draw_networkx_labels( graph ,pos, labels)
    plt.show()
     
    
    
    
    
    
