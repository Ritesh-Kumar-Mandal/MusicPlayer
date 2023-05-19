class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head

            while current.next is not None:
                current = current.next
            
            current.next = Node(data)
        
    def length(self)->int:
        
        length = 0
        current = self.head

        while current is not None:
            length += 1
            current = current.next

        return length 
    
    def get(self, index:int):

        if index >= self.length():
            print("ERROR! - given 'index' is out of range")
        else:

            i = 0
            current = self.head

            while current is not None:
                if i == index:
                    return current.data
                current = current.next
                i+=1
    
    def index(self, data):
        index = 0
        current = self.head
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index+=1