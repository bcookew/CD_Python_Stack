from platform import node


class SLList:
    def __init__(self):
        self.head = None
    
    def addToFront(self,val):
        newNode = SLNode(val)
        current_head = self.head
        newNode.next = current_head
        self.head = newNode
        return self
    
    def addToBack(self,val):
        if self.head == None:
            self.addToFront(val)
            return self
        newNode = SLNode(val)
        node = self.head
        while (node.next != None):
            node = node.next
        node.next = newNode
        return self

    def removeFromFront(self):
        removedValue = self.head.value
        self.head = self.head.next
        return removedValue
    
    def removeFromBack(self):
        prevNode = None
        node = self.head
        while (node.next != None):
            prevNode = node
            node = node.next
        prevNode.next = None
        return node.value
    
    def printValues(self):
        node = self.head
        while (node != None):
            print(node.value)
            node = node.next
        return self 
    


class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    

lst1 = SLList()

lst1.addToFront(5).addToFront(10).addToFront(15).printValues()
print("*"*35)
lst2 = SLList()

lst2.addToBack(1).addToBack(2).addToBack(3).addToBack(4).printValues()
lst2.removeFromBack()
lst2.printValues()

print("Removed: ", lst1.removeFromFront())
lst1.printValues()