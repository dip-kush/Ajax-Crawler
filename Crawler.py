from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GetClickables import GetDomElements, getLinks
from selenium.webdriver.support.ui import WebDriverWait
from State import StateMachine, NodeData
import matplotlib.pyplot as plt
import networkx as nx
import Queue
import time

def initState(domString, link, title, driver, formValues):
    '''
    Initialize the State Machine adding a StateNode 
    '''
    
    fsm = StateMachine()
    node = NodeData()
    node.link = link
    #print domString
    node.domString = domString
    node.title = title
    node.visited = 0
    node.clickables = getLinks(domString)
    print "i was here"
    print node.clickables
    fsm.addNode(0, node)
    #print fsm.graph.number_of_nodes()
    Crawl(fsm, driver, formValues)
    
def Crawl(fsm, driver,formValues):
    '''
    Crawls the Application by doing the Breadth First Search over the State Nodes. 
    '''
    
    graph = fsm.graph 
    queue = Queue.Queue()
    queue.put(0)
        
    while queue.empty() == False:
        curNode = queue.get()
        driver.get(graph.node[curNode]['nodedata'].link)
        graph.node[curNode]['nodedata'].visited = 1
        clickables = []
        clickables = graph.node[curNode]['nodedata'].clickables
        domString = graph.node[curNode]['nodedata'].domString
        for clickable in clickables:
            driver.find_element_by_xpath("//a[@href='"+clickable+"']").click()
            #time.sleep(10)
            #make a new node add in the graph and the queue            
            newNode = NodeData()
            newNode.link = driver.current_url
            newNode.domString = driver.page_source
            newNode.clickables = getLinks(newNode.domString)
            newNode.visited = 0
            newNode.title = driver.title
            existNodeNumber = fsm.checkNodeExists(newNode.domString)
            if existNodeNumber == -1:
                print "i am here"
                nodeNumber = fsm.numberOfNodes()
                fsm.addNode(nodeNumber, newNode)
                fsm.addEdges(curNode, nodeNumber)
                print "the number of node "+ str(nodeNumber)
                queue.put(nodeNumber)
            else:
                fsm.addEdges(curNode, existNodeNumber)
            WebDriverWait(driver, 2000)
            driver.back()
            
            #try to fill the field values 
            #press clicks of all the submit buttons
            
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
     
    
    
    
    
    
