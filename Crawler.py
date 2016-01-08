import Queue
import time
import networkx as nx
from urlparse import urlparse
from GetClickables import getLinks
from selenium.webdriver.support.ui import WebDriverWait
from State import StateMachine, NodeData
from DomComparator import getDomDiff
from FormExtractor import getSubmitButtonNumber, fillFormValues
from logger import LoggerHandler
import matplotlib.pyplot as plt


logger = LoggerHandler(__name__)


def initState(domString, link, title, driver, formValues):
    '''
    Initialize the State Machine adding a StateNode
    '''

    fsm = StateMachine()
    node = NodeData()
    node.link = link
    # print domString
    node.domString = domString
    node.title = title
    node.visited = 0
    node.clickables = getLinks(domString)
    node.backtrackPath.append(link)
    print 0, node.clickables
    fsm.addNode(0, node)
    Crawl(0, fsm, driver, formValues)    
    #clickables = graph.node[curNode]['nodedata'].clickables
    drawGraph(fsm)
    
def drawGraph(fsm):
    graph = fsm.graph
    printEdges(graph)
    printNodes(graph)
    print fsm.doBacktrack
    logger.info("Number of Node Found %s" % (fsm.numberOfNodes()))
    pos = nx.spring_layout(graph)
    #labels = {k: str(k) for k in graph.nodes()}
    labels = {k: graph.node[k]['nodedata'].title for k in graph.nodes()}
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos, labels)
    #nx.draw(graph,node_size=3000,nodelist=graph.nodes(),node_color='b')
    #nx.draw_networkx_labels( graph ,pos, labels)
    plt.show()

    
def backtrack(driver, fsm, node, formValues, tillEnd):               
    if fsm.doBacktrack == False:
        driver.back()
    else:
        graph = fsm.graph
        path = graph.node[node]['nodedata'].backtrackPath
        driver.get(path[0])
        for i in range(1, len(path)-1+tillEnd):
            time.sleep(2.0)
            fillFormValues(formValues, driver)
            time.sleep(2.0)
            action, target= path[i].split(":")
            if action == "click":
                driver.find_element_by_xpath("//a[@href='" + target + "']").click()
            elif action == "form":
                submitNumber = target.split('-')[1]
                element = driver.find_element_by_xpath("(//input[@type='submit'])[" + str(submitNumber) + "]")
                element.click()
    time.sleep(2.0) 

def Crawl(curNode, fsm, driver, globalVariables):
    '''
    Crawls the Application by doing the Breadth First Search
    over the State Nodes.
    '''
    graph = fsm.graph
    graph.node[curNode]['nodedata'].visited = 1
    clickables = []
    clickables = graph.node[curNode]['nodedata'].clickables
    domString = graph.node[curNode]['nodedata'].domString
    logger.info("Clicking All Clickables to get a New State")
    for clickableType, clickableList in clickables.iteritems():
        for clickable in clickableList:        
            if checkForBannedUrls(
                    clickable,
                    globalVariables,
                    graph.node[curNode]['nodedata'].link):
                continue
                        
            if fsm.checkStateUrlExist(globalVariables.baseAddress+clickable):
                continue
            logger.info("Trying to click"+clickable)
            driver.find_element_by_xpath(
                "//a[@"+clickableType+"='" + clickable + "']").click()
            time.sleep(2)
            # make a new node add in the graph and the queue
            newNode = CreateNode(driver)
            # add the Node checking if the node already exists
            nodeNumber = addGraphNode(newNode,curNode,driver,fsm,"click:"+clickable)
            if nodeNumber != -1:
                Crawl(nodeNumber, fsm, driver, globalVariables) 
            else:
                backtrack(driver,fsm,curNode,globalVariables.formFieldValues, 1)
                
    submitButtonNumber = getSubmitButtonNumber(domString, driver)
    time.sleep(2.0)
    fillFormValues(globalVariables.formFieldValues, driver)
    time.sleep(2.0)
    logger.info("Initiating Crawling Submit Button")
    for i in range(1, submitButtonNumber + 1):
        element = driver.find_element_by_xpath(
            "(//input[@type='submit'])[" + str(i) + "]")
        element.click()
        time.sleep(2)
        newNode = CreateNode(driver)
        
        nodeNumber = addGraphNode(newNode,curNode,driver,fsm,"form:submit" +str(i))
        if nodeNumber != -1:
            Crawl(nodeNumber, fsm, driver, globalVariables)
        else:
            backtrack(driver,fsm,curNode,globalVariables.formFieldValues, 1)
    WebDriverWait(driver, 2000)
    backtrack(driver,fsm,curNode,globalVariables.formFieldValues,0)           
 

   
    

def checkForBannedUrls(clickable, globalVariables, currentPath):
    '''    
    if clickable.find("http") != -1:
        logger.info(clickable + "is a absolute link")
        path = clickable
    else:        
        index = currentPath.rfind("/")
        path = currentPath[0:index] + "/" + clickable
    '''     
    scopeUrls = globalVariables.scopeUrls
    baseAddress = globalVariables.baseAddress
    bannedUrls= globalVariables.bannedUrls
    flag = 0    
    parsed = urlparse(clickable)
    if not parsed.hostname:
        combinedUrl = baseAddress+parsed.path
    else:
        combinedUrl = parsed.hostname+parsed.path
    for item in scopeUrls:
        if item in combinedUrl:
            flag = 1
            break
        
    if flag == 0:
        return True
    
    if clickable in bannedUrls:
        logger.info("Exist in Banned Url " + clickable)
        return True
    else:
        logger.info("Path doesn't exist")
        return False


def printNodes(graph):
    numberofnodes = graph.number_of_nodes()
    for i in range(numberofnodes):
        print i ,graph.node[i]['nodedata'].backtrackPath


def printEdges(graph):
    edges = graph.edges()
    numEdges = len(edges)
    for i in range(numEdges):
        source = edges[i][0]
        dest = edges[i][1]
        print edges[i], graph[source][dest]
    


def CreateNode(driver):
    '''
    Creates a New State Node assigning the NodeData Properties
    '''
    newNode = NodeData()
    newNode.link = driver.current_url
    newNode.domString = driver.page_source
    newNode.visited = 0
    newNode.title = driver.title
    logger.info("Creating a new node with title %s" % (newNode.title))
    return newNode


def addGraphNode(newNode, curNode, driver, fsm, event):
    '''
    Adding a Node to the Finite State Machine
    Checking if the Dom Tree Does Not Exist Already
    '''
    graph = fsm.graph
    curNodeUrl = graph.node[curNode]['nodedata'].link
    newNodeUrl = driver.current_url
    if curNodeUrl == newNodeUrl:
        logger.debug("found the same url %s %d" % (curNodeUrl, curNode))
        fsm.doBacktrack = True
        
    for item in graph.node[curNode]['nodedata'].backtrackPath:
        newNode.backtrackPath.append(item)
        
    newNode.backtrackPath.append(event)    
    existNodeNumber = fsm.checkNodeExists(newNode.domString)
    
    if existNodeNumber == -1:
        nodeNumber = fsm.numberOfNodes()
        newNode.insertedDom = getDomDiff(graph.node[curNode]['nodedata'].domString,newNode.domString)
        newNode.clickables = getLinks(newNode.insertedDom)
        #write code here
        fsm.addNode(nodeNumber, newNode)
        logger.info("Adding a New Node %d to Graph" % (nodeNumber))
        fsm.addEdges(curNode, nodeNumber, event)
        logger.info(
            "Adding a Edge from Node %d and %d" %
            (curNode, nodeNumber))
        print nodeNumber, newNode.clickables
        return nodeNumber    
        #queue.put(nodeNumber)
    else:
        logger.info("Dom Tree Already Exist")
        fsm.addEdges(curNode, existNodeNumber, event)
        return -1
    #WebDriverWait(driver, 2000)
    #driver.back()
