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
