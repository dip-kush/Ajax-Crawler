import GetClickables
import networkx as nx
from DomComparator import htmlCompare

class NodeData:
    def __init__(self):
        self.link = ""
        self.domString = ""
        self.title = ""
        self.index = -1
        self.visited = 0
        self.clickables = []
        #print self.domString

class StateMachine:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        
    def addNode(self, data):
        #print self.graph.number_of_nodes()
        self.graph.add_node(self.graph.number_of_nodes(), nodedata = data)
      
    def addEdges(self, n1, n2):
        self.graph.add_edge(n1, n2)  
    
    def checkNodeExists(self, dom):
        for n in self.graph.nodes():
            #print self.graph.node[n]['nodedata']
            if htmlCompare(dom,None,self.graph.node[n]['nodedata'].domString):
                return n
        return -1        

    def numberOfNodes(self):
        return self.graph.number_of_nodes()

    
class MyGraph(nx.MultiGraph):
    def __init__(self):
        pass         


'''
n1=NodeData()
n2=NodeData()
n1.domString="abc"
n1.domAddressPath="xyz"
n2.domString="abc"
n2.domAddressPath="abc";
s=StateMachine()
s.addNode(n1)
s.addNode(n2)
print s.graph.node[0]

s.addEdges(0,1)
'''
