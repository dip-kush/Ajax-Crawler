from GetClickables import AnchorTags, ButtonLinks, Clickables
import networkx as nx

class StateNode:
    def __init__(self):
        self.domString = ""
        self.domAddressPath = ""
        self.clickables = Clickables()
        self.title = ""

class StateMachine:
    def __init__(self):
        self.graph = nx.MultiDiGraph()

    def addNode(self, node1):
        self.graph.add_node(node1)
    
    def addEdges(self, node1, node2):
        self.graph.add_edge(node1, node2)

        
            
         
