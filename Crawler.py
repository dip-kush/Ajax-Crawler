from State import States, StateMachine
from GetClickables import getAnchorTags, getButtonLinks

def StartState(domString):
    
    startNode = States()
    stateNode = StateNode()
    stateNode.domString = domString
    stateNode.clickables.anchorTags = getAnchorTags(domString)
    stateNode.clickables.buttonLinks = getButtonLinks(domString)
    startNode.addNode(stateNode)
    
    
    
    
    
