import sys
from SDLang import *

class ForLoop:
    def __init__(self):
        self.startVal = None
        self.endVal = None
        self.loopVar = None
        self.for_type = None
        self.startLineNo = None
        self.endLineNo = None
        self.funcName = None
        self.binaryNodeList = []
        self.varInfoNodeList = []
        self.forLoopInner = None
        self.ifElseInner = None
        self.assignNode = None
        self.topLevelNode = True

    def getStartVal(self):
        return self.startVal

    def getEndVal(self):
        return self.endVal

    def getLoopVar(self):
        return self.loopVar

    def getStartLineNo(self):
        return self.startLineNo

    def getEndLineNo(self):
        return self.endLineNo

    def getFuncName(self):
        return self.funcName

    def getBinaryNodeList(self):
        return self.binaryNodeList

    def getVarInfoNodeList(self):
        return self.varInfoNodeList

    def getInnerLoop(self):
        return self.forLoopInner

    def getAssignNode(self):
        return self.assignNode

    def isTopLevelNode(self):
        return self.topLevelNode

    def updateForLoopStruct(self, node, startLineNo, funcName):
        if (node.type != ops.FOR) and (node.type != ops.FORALL):
            print("updateForLoopStruct in ForLoop was passed a node that is not of type FOR or FORALL")
            return
        self.for_type = node.type
        if ( (type(startLineNo) is not int) or (startLineNo < 1) ):
            sys.exit("Problem with start line number passed to updateForLoopStruct in ForLoop.")
        self.startLineNo = startLineNo

        if ( (type(funcName) is not str) or (len(funcName) == 0) ):
            sys.exit("Problem with function name passed to updateForLoopStruct in ForLoop.")
        self.funcName = funcName

        if node.type == ops.FOR:
            loopVar = node.left.left.attr
            if ( (type(loopVar) is not str) or (len(loopVar) == 0) ):
                sys.exit("Problem with loop variable extracted in updateForLoopStruct method in ForLoop.")
            self.loopVar = loopVar
    
            self.startVal = node.left.right.attr
            self.endVal = node.right.attr
        self.assignNode = BinaryNode.copy(node)

    def setInnerLoop(self, forLoopInnerStruct):
        self.forLoopInner = forLoopInnerStruct
        
    def setEndLineNo(self, endLineNo):
        if ( (type(endLineNo) is not int) or (endLineNo < 1) ):
            sys.exit("Problem with ending line number passed to setEndLineNo in ForLoop.")

        if (self.startLineNo >= endLineNo):
            sys.exit("setEndLineNo in ForLoop.py:  end line number passed in is less than or equal to start line number.")

        self.endLineNo = endLineNo

    def appendToBinaryNodeList(self, binaryNode):
        self.binaryNodeList.append(binaryNode)

    def appendToVarInfoNodeList(self, varInfoNode):
        self.varInfoNodeList.append(varInfoNode)
