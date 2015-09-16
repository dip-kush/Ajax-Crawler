from GetClickables import AnchorTags, ButtonLinks, Clickables
import networkx as nx

class NodeData:
    def __init__(self):
        self.domString = ""
        self.domAddressPath = ""
        self.clickables = Clickables()
        self.title = ""
        self.index = -1
        print self.domString

class StateMachine:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        
    def addNode(self, data):
        self.graph.add_node(self.graph.number_of_nodes, nodedata = data)
      
    def addEdges(self, n1, n2):
        self.graph.add_edge(n1, n2)  
    
    def checkNodeExists(self, dom):
        for n in self.graph.nodes():
            if compare(dom, self.graph[n]['nodedata'].domString):
                return 1
        return 0        


    
class MyGraph(nx.MultiGraph):
    def __init__(self):
        pass         



n1=NodeData()
n2=NodeData()
n1.domString="abc"
n1.domAddressPath="xyz"
n2.domString="abc"
n2.domAddressPath="abc";
s=StateMachine()
s.addNode(n1)
s.addNode(n2)
s.addEdges(0,1)

