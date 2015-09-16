from GetClickables import AnchorTags, ButtonLinks, Clickables
import networkx as nx

class StateNode:
    def __init__(self):
        self.domString = ""
        self.domAddressPath = ""
        self.clickables = Clickables()
        self.title = ""
        print self.domString

class StateMachine:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        
    def addNode(self, node):
        self.graph.add_node(self, self.graph.size, domString=node.domString)
      
    def addEdges(self, n1, n2):
        self.graph.add_edge(n1, n2)  
    
   
class MyGraph(nx.MultiGraph):
    def __init__(self):
        pass
         
