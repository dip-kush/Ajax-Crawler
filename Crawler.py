import Clickables
from States import State, StateNode, getAnchorTags, getButtonLinks

def StartState(domString):
    
    startNode = States()
    stateNode = StateNode()
    stateNode.domString = domString
    stateNode.clickables.anchorTags = getAnchorTags(domString)
    stateNode.clickables.buttonLinks = getButtonLinks(domString)
    startNode.addNode(stateNode)
    
    
    
    
    
