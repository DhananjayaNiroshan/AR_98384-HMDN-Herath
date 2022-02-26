from Node import Node

class DoublyLinkedList:
    def __init__(self):  # defining variable
        self.head = None  # initially first node is none
        self.tail = None  # initially last node is none
        self.length = 0  # initially doubly linked list length is zero

    
# Doubly Linked List length size
    def doublyListLength(self):
        current = self.head  # create current as head node
        count = 0  # creating count as zero
        while current is not None:  # traversing until current node is none
            count += 1
            current = current.getNext()  # change next of current as current
        return count
    
     # this function print contend of all doubly linked
    def printForwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            current = self.head
            while current is not None:  # traversing until current node is none
                print(current.getData(), end=" ")  # print data of current node
                current = current.getNext()  # change next of current as current

   # this function print to reverse contend of all doubly linked
    def printBackwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            current = self.head
            while current.getNext() is not None:  # traversing until next of current is none
                current = current.getNext()  # change next of new node as current
            while current is not None:  # traversing until current is none
                print(current.getData(), end=" ")  # print data of current
                current = current.getPrev()  # change previous of current as current

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

def deleteNodeByPos(self, Pos):
        if self.head is None:
            print("Empty Doubly Linked List")
            return None
        if self.length > Pos > -1:  
            if Pos == 0: 
                self.deleteFirstNode()  
            elif Pos == self.length - 1:  
                self.deleteLastNode()  
            else:
                count = 0
                current = self.head
                while count != Pos - 1:  
                    count += 1
                    current = current.getNext()  
                
                deleteNode = current.getNext()
                current.setNext(deleteNode.getNext())  
                current.getNext().setPrev(current) 
            self.length -= 1


