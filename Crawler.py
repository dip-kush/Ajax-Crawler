from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from GetClickables import GetDomElements, getLinks
from selenium.webdriver.support.ui import WebDriverWait
from State import StateMachine, NodeData
from FormExtractor import getSubmitButtonNumber, fillFormValues
from logger import LoggerHandler
import matplotlib.pyplot as plt
import networkx as nx
import Queue
import time


logger = LoggerHandler(__name__)


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
    print node.clickables
    fsm.addNode(0, node)
    Crawl(fsm, driver, formValues)
    
def Crawl(fsm, driver,globalVariables):
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
        logger.info("Clicking All Clickables to get a New State")
        for clickable in clickables:
            driver.find_element_by_xpath("//a[@href='"+clickable+"']").click()
            #make a new node add in the graph and the queue            
            newNode = createNode(driver)
            #add the Node checking if the node already exists
            addGraphNode(newNode,curNode, driver, fsm, queue, "click:"+clickable)
            
        submitButtonNumber = getSubmitButtonNumber(domString, driver)
        time.sleep(0.5)
        fillFormValues(globalVariables.formFieldValues, driver)
        time.sleep(0.5)
        logger.info("Initiating Crawling Submit Button")
        for i in range(1, submitButtonNumber+1):
            
            
            element = driver.find_element_by_xpath("(//input[@type='submit'])["+str(i)+"]")
            element.click()
            newNode = createNode(driver)
            addGraphNode(newNode, curNode, driver, fsm, queue, "form:submit"+str(i))
        
            
    printEdges(graph)
    logger.info("Number of Node Found %s"%(fsm.numberOfNodes()))
    pos = nx.spring_layout(graph)
    labels = {k:graph.node[k]['nodedata'].title for k in graph.nodes()}
    nx.draw_networkx_nodes(graph,pos)
    nx.draw_networkx_edges(graph,pos)
    nx.draw_networkx_labels(graph,pos,labels)          
    #nx.draw(graph,node_size=3000,nodelist=graph.nodes(),node_color='b')
    #nx.draw_networkx_labels( graph ,pos, labels)
    plt.show()
     
    
def printEdges(graph):
    edges = graph.edges()
    numEdges = len(edges)
    for i in range(numEdges):
        source = edges[i][0]
        dest = edges[i][1]
        print edges[i], graph[source][dest]
    
    
def createNode(driver):
    '''
    Creates a New State Node assigning the NodeData Properties
    '''

    newNode = NodeData()
    newNode.link = driver.current_url
    newNode.domString = driver.page_source
    newNode.clickables = getLinks(newNode.domString)
    newNode.visited = 0
    newNode.title = driver.title    
    logger.info("Creating a new node with title %s"%(newNode.title))
    return newNode
    
    
def addGraphNode(newNode,curNode, driver, fsm, queue,event):
    '''
    Adding a Node to the Finite State Machine
    Checking if the Dom Tree Does Not Exist Already 
    '''
    
    existNodeNumber = fsm.checkNodeExists(newNode.domString)
    if existNodeNumber == -1:
            
        nodeNumber = fsm.numberOfNodes()
        fsm.addNode(nodeNumber, newNode)
        logger.info("Adding a New Node %d to Graph"%(nodeNumber))
        fsm.addEdges(curNode, nodeNumber,event)
        logger.info("Adding a Edge from Node %d and %d"%(curNode, nodeNumber))
        queue.put(nodeNumber)
    else:
        fsm.addEdges(curNode, existNodeNumber,event)
    WebDriverWait(driver, 2000)
    driver.back()
            