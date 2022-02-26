#AR_98384
#AF/19/15732
#H.M.D.N.Herath 
class Node:                                     

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, addressA):
        self.next = addressA

    def getPrev(self):
        return self.prev

    def setPrev(self, addressB):
        self.prev = addressB

    def hasNext(self):
        return self.next is not None

    def hasPrev(self):
        return self.prev is not None
