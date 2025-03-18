class Node:
    def __init__(self,item=None, next=None):
        self.item = item
        self.next = next
    
class CLL:
    def __init__(self,last=None):
        self.last = None
    
    def is_empty(self):
        return self.last==None

    def insert_at_start(self,data=None):
        n=Node(data)
        if self.is_empty():  #Linked list is empty
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        
    
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while(temp != self.last):

            if temp.item == data:
                return temp

            temp = temp.next

        if temp.item == data:  # check last data of  node 
            return temp
        
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next = n
            if temp == self.last:  # if temp equal hai last node ke then new node will be last node
                self.last = n

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while(temp != self.last):
                print(temp.item,end=' ')
                temp = temp.next
            print(temp.item)   # print last node value


    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:  # that means we have single node
                self.last = None
            
            else:
                temp = self.last.next
                while(temp.next != self.last):
                    temp = temp.next
                
                temp.next = self.last.next
                self.last = temp


    
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last:     # that means we have single node
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()  # delete 1st node 
                else:
                    temp = self.last.next  # reffer first node
                    while( temp != self.last ):   # means first node equal nahi honga last node se
                        if temp.next == self.last:  # if 2nd node and last node eual hai
                            if self.last.item == data: # if 2nd node data and last node data eual hai  to delete last node
                                self.delete_last()
                                break
                        if temp.next.item == data:  # 
                            temp.next  = temp.next.next
                            break
                        temp = temp.next

        
    # def __init__(self):
    #     if self.current == None:
    #         return CLLIterator(None)
    #     else:
    #         return CLLIterator(self.last.next)

# class CLLIterator:
#     def __init__(self,start):
#         self.current = start   # it takes the 1st node refference
#         self.start = start
    
#     def __init__(self):
#         return self

#     def __next__(self):
#         if self.current == None:  # if list is empty then it run
#             raise StopIteraion
#         data = self.current.item
#         self.current = self.current.next
#         if self.current == self.start:
#             raise StopIteraion
#         return data






cll = CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
cll.print_list()

# 20 10 50 30 40