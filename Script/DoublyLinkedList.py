from Node import Node


class DoublyLinkedList:
    def __init__(self):  
        self.head = None  
        self.tail = None  
        self.length = 0  

    
    def doublyListLength(self):
        current = self.head 
        count = 0  
        while current is not None:  
            count += 1
            current = current.getNext()  
        return count
    
    def printForwardList(self):
        if self.head is None:  
            print("Empty Doubly Linked List")
        else:
            current = self.head
            while current is not None:  
                print(current.getData(), end=" ")  
                current = current.getNext() 
    
    def printBackwardList(self):
        if self.head is None:  
            print("Empty Doubly Linked List")
        else:
            current = self.head
            while current.getNext() is not None:  
                current = current.getNext()  
            while current is not None:  
                print(current.getData(), end=" ")  
                current = current.getPrev()  

    def addNodeBeginning(self, data):
        newNode = Node(data)
        newNode.setData(data)
        if self.head is None:  
            self.head = newNode  
        else:
            newNode.setNext(self.head)  
            self.head.setPrev(newNode)  
            newNode.setPrev(None)  
            self.head = newNode  
        self.length += 1 
    
    def addNodeEnd(self, data):
        newNode = Node(data)
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() is not None:  
                current = current.getNext()  
            current.setNext(newNode)  
            newNode.setPrev(current)  
            newNode.setNext(None)  
        self.length += 1
    def addNodeInPos(self, pos, data):
       
        if pos > self.length - 1 or pos < 0:
            return None
        elif pos == self.length - 1:  
            self.addNodeEnd(data)  
        elif pos == 0:  
            self.addNodeBeginning(data)  
        else:
            newNode = Node(data)
            newNode.setData(data)
            current = self.head
            count = 0
            while count != pos - 1:  
                current = current.getNext()  
                count += 1
            newNode.setPrev(current)  
            newNode.setNext(current.getNext())  
            current.getNext().setPrev(newNode)  
            current.setNext(newNode)  
        self.length += 1

def addNodeInPos(self, pos, data):
       
        if pos > self.length - 1 or pos < 0:
            return None
        elif pos == self.length - 1:  
            self.addNodeEnd(data)  
        elif pos == 0:  
            self.addNodeBeginning(data)  
        else:
            newNode = Node(data)
            newNode.setData(data)
            current = self.head
            count = 0
            while count != pos - 1:  
                current = current.getNext()  
                count += 1
            newNode.setPrev(current)  
            newNode.setNext(current.getNext())  
            current.getNext().setPrev(newNode)  
            current.setNext(newNode)  
        self.length += 1

    
    def deleteFirstNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            self.head = self.head.getNext()  
            self.head.setPrev(None) 
        self.length -= 1

   
    def deleteLastNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            current = self.head
            previous = None  
            while current.getNext() is not None:  
                previous = current  
                current = current.getNext()  
            previous.setNext(None) 
        self.length -= 1

