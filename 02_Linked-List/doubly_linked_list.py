class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = 
        
    
class DLL:
    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return (self.start==None)

    def insert_at_start(self,data):
        n = Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self,data):
        temp = self.start 
        if self.start != None:
            while(temp.next is not None):
                temp = temp.next 
        n = Node(temp,data,None)
        if temp==None:
            self.next = n
        else:
            temp.next = n


    def search(self,data):
        temp = self.start
        while(temp is not None):
            if temp.item == data:
                return temp
            temp = temp.next
        return None
        


# jis node ko reffer kar raha hai temp usske baad node mai value insert karna hai.
    def insert_after(self,temp,data):
        if temp is not None 
        



