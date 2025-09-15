class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CircularDoubleLL:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        new_node=Node(data)
        if not self.head:
            new_node.next=new_node
            new_node.prev=new_node
            self.head=new_node
            return
        last=self.head.prev
        new_node.prev=last
        last.next=new_node
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            new_node.next=new_node.prev=new_node
            self.head=new_node
            return
        last=self.head.prev
        last.next=new_node
        new_node.prev=last
        new_node.next=self.head
        self.head.prev=new_node
    def delete_at_begin(self):
        if not self.head:
            print("Empty")
            return
        last=self.head.prev
        nextnode=self.head.next
        last.next=nextnode
        nextnode.prev=last
        self.head=nextnode
    def delete_at_end(self):
        if not self.head:
            print("Empty")
            return
        last=self.head.prev
        before_last=last.prev
        before_last.next=self.head
        self.head.prev=before_last
    def delete_data(self,data):
        current=self.head
        while current.next!=self.head:
            if current.data==data:
                previous.next=nextnode
                nextnode.prev=previous
                return
            previous=current
            current=current.next
            nextnode=current.next
    def traversal(self):
        current=self.head
        while current.next!=self.head:
            print(current.data,"->",end="")
            current=current.next
        print(current.data,"-> end")
    def insert_at_index(self,data,index):
        new_node=Node(data)
        if index==0:
            self.insert_at_begin(data)
            return
        if not self.head:
            print("Can't insert at index",index,"when list is empty")
        current=self.head
        i=0
        while current.next!=self.head and i<index-1:
            curent=current.next
            i+=1
        if current is self.head:
            print("Out of bounds")
            return
        new_node.next=current.next
        current.next.prev=new_node
        current.next=new_node
        new_node.prev=current
    def length(self):
        current=self.head
        i=1
        while current.next!=self.head:
            i+=1
            current=current.next
        print("Length of CDLL is",i)
cdll=CircularDoubleLL()
cdll.insert_at_begin(4)
cdll.traversal()
cdll.insert_at_end(1)
cdll.traversal()
cdll.insert_at_begin(0)
cdll.traversal()
cdll.insert_at_index(7,0)
cdll.insert_at_index(8,13)
cdll.traversal()
cdll.delete_at_begin()
cdll.traversal()
cdll.length()
cdll.delete_at_end()
cdll.traversal()
cdll.insert_at_end(12)
cdll.traversal()
cdll.delete_data(4)
cdll.traversal()