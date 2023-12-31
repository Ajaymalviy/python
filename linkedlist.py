
class Node:
    def __init__(self ,data=None,next=None):
        self.data=data
        self.next=next
class  Linkedlist   :
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("linkedlist is empty")        
            return
        itr=self.head
        linkedliststring=''
        while itr:
            linkedliststring += str(itr.data)+ '-->'
            # pdb.set_track()
            itr=itr.next
        print(linkedliststring)


    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data ,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)     

    def getlength(self):
        count=0
        itr=self.head
        while itr:
            count +=1
            itr=itr.next
        return count    


    def insert_at(self,index,data):
        if index<0 or index > self.getlength():
            raise Exception('error  of invalid index occure')
        count=0
        itr=self.head
        while itr:
            if count== 'index-1':
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count +=1 
    def remove_at(self,index):
        if index<0 or index > self.getlength():
            raise Exception('error  of invalid index occure')
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count +=1

    # def insert_after_value(self,data,head):
    #     itr=self.head
    #     while itr.data != data:
    #         if self.data==self.head.data:
    #             return 
        

    def insert_at(self,index,data):
        if index<0 or index > self.getlength():
            raise Exception('error  of invalid index occure')
        count=0
        itr=self.head
        while itr:
            if count== 'index-1':
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count +=1     
    

    

    def insert_after_value(self,value,data):
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
        print("Value not found ")

  
    def remove_by_value(self,value):
        itr = self.head
        while itr:
            if itr.data == value:
                itr.next = itr.next.next
                ll.print()
                break
            itr = itr.next
        print("value not found")
       

if __name__  == '__main__':
    ll=Linkedlist()
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(14)
    ll.insert_at_beginning(24)
    ll.insert_at_beginning(34)
    ll.insert_at_end(12)
    ll.insert_at_end(12)
    print("length of linked_list",ll.getlength())
    ll.insert_at(2,33)
    ll.remove_at(2)
    ll.insert_after_value(24,14)
    ll.insert_after_value(34,8)
    ll.print()

# class Node(self.data=none,next=none,prev=none):
#     self.data=data 
#     self.next=next
#     self.prev=Prev
#     #operation on doubly linkedlist
#     def insert_at_beginning(data):
#     def insert_at_end(data):
#     def print_backward():
#     def print_forward():
#     def get_last_node():
#     def def_length() :       
    


    # question ----remove dupluicate from usorted Linkedlist
    #          ----by not taking ny buffer for 
    #            ------sorting a linkedlist (2,4,5,3,65,6,4 ) where <6 comes into another part and 6< is on another 



class Doublylinkedlist:
        # Adding a node at the front of the list
    def push(self, new_data):
    
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data=new_data)
    
        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None
    
        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node
    
        # 5. move the head to point to the new node
        self.head = new_node
    
 
def insertAfter(self, prev_node, new_data):
 
    # Check if the given prev_node is NULL
    if prev_node is None:
        print("This node doesn't exist in DLL")
        return
 
    # 1. allocate node  & 
    # 2. put in the data
    new_node = Node(data=new_data)
 
    # 3. Make next of new node as next of prev_node
    new_node.next = prev_node.next
 
    # 4. Make the next of prev_node as new_node
    prev_node.next = new_node
 
    # 5. Make prev_node as previous of new_node
    new_node.prev = prev_node
 
    # 6. Change previous of new_node's next node
    if new_node.next is not None:
        new_node.next.prev = new_node
  
def append(self, new_data):
 
    # 1. allocate node 
    # 2. put in the data
    new_node = Node(data=new_data)
    last = self.head
 
    # 3. This new node is going to be the
    # last node, so make next of it as NULL
    new_node.next = None
 
    # 4. If the Linked List is empty, then
    #  make the new node as head
    if self.head is None:
        new_node.prev = None
        self.head = new_node
        return
 
    # 5. Else traverse till the last node
    while (last.next is not None):
        last = last.next
 
    # 6. Change the next of last node
    last.next = new_node
    # 7. Make last node as previous of new node */
    new_node.prev = last
 


     