class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
    
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
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
                temp.next = n

    def print_list(self):
        temp = self.start
        while( temp is not None):
            print(temp.item,end=' ')
            temp = temp.next

    def delete_at_first(self):
        if(self.start is not None):
            self.start = self.start.next
            self.start.prev = None
    
    def delete_at_last(self):
        if self.start == None:
            pass
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while( temp.next is not None ):
                temp = temp.next
            temp.next.prev = None 
    
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while( temp is not None):
                if temp.item == data:
                    if temp.next is not None:       # last node na ho isliye.
                        temp.next.prev = temp.prev
                    if temp.prev is not None:   # 1st node nahi hona chahiye.  
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next  # 1st node hai
                        break
                temp = temp.next
    def __iter__(self):
        return DLLIterator(self.start)


class DLLIterator:
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

####################################################################

# mylist = DLL()
# mylist.insert_at_start(10)
# mylist.insert_at_last(30)
# mylist.insert_after(mylist.search(10),20)
# for x in mylist:
#     print(x,end=' ')
# print()

### output is  10 20 30 



####################################################################
                


mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(10),20)
mylist.print_list()
print()


#### output is 10 20 30


