
class Node:
    def __init__(self, elements=[]):
        self.left = None
        self.right = None
        self.elements = set(elements)

    def addBetween(self, node1, node2):
        self.left = node1
        self.right = node2

        node1.right = self
        node2.left = self
    
    def deleteNode(self):
        left, right = self.left, self.right
        left.right = right
        right.left = left
            
			
class AllOne:
    def __init__(self):
        self.keyToNum = {}
        self.numToNode = {}
        
        self.head, self.tail = Node(), Node()
        self.head.right = self.tail
        self.tail.left = self.head
        
    def inc(self, key: str) -> None:
        keyToNum = self.keyToNum
        numToNode = self.numToNode

        if key not in keyToNum:
            keyToNum[key] = 1
            if 1 in numToNode:
                numToNode[1].elements.add(key)
            else:
                newNode = Node([key])
                numToNode[1] = newNode
                newNode.addBetween(self.head, self.head.right)                
        else:
            oldNum = keyToNum[key]
            oldNode = numToNode[oldNum]
            
            newNum = oldNum + 1
            keyToNum[key] = newNum

            if newNum in numToNode:
                numToNode[newNum].elements.add(key)
            else:
                newNode = Node([key])
                numToNode[newNum] = newNode
                newNode.addBetween(oldNode, oldNode.right)
            
            oldNode.elements.discard(key)
            if not oldNode.elements:
                oldNode.deleteNode()
                del numToNode[oldNum]

    def dec(self, key: str) -> None:
        keyToNum = self.keyToNum
        numToNode = self.numToNode
        
        if key not in keyToNum:
            return
        
        oldNum = keyToNum[key]
        oldNode = numToNode[oldNum]
        
        if oldNum == 1:
            del keyToNum[key]
        else:
            newNum = oldNum - 1
            keyToNum[key] = newNum
			
            if newNum in numToNode:
                newNode = numToNode[newNum]
                newNode.elements.add(key)
            else:
                newNode = Node([key])
                numToNode[newNum] = newNode
                oldLeft = oldNode.left
                newNode.addBetween(oldLeft, oldNode)
                
        oldNode.elements.discard(key)
        if not oldNode.elements:
            oldNode.deleteNode()
            del numToNode[oldNum]

    def getMaxKey(self) -> str:
        if self.tail.left == self.head:
            return ''
        else:
            for e in self.tail.left.elements:
                return e

    def getMinKey(self) -> str:
        if self.head.right == self.tail:
            return ''
        else:
            for e in self.head.right.elements:
                return e