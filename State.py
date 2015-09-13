from GetClickables import AnchorTags, ButtonLinks, Clickables
import networkx as nx

class StateNode:
    def __init__(self):
        self.domString = ""
        self.domAddressPath = ""
        self.clickables = Clickables()
        self.title = ""

class States:
    def __init__(self):
        self.graph = nx.MultiDiGraph()

    def addNode(node1):
        self.graph.add_node(node1)
    
    def addEdges(node1, node2):
        self.graph.add_edge(node1, node2)

        
            
         
