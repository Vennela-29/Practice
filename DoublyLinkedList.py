class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        new_node.prev=current
    def insert_at_index(self,data,index):
        new_node=Node(data)
        if index==0:
            self.insert_at_begin(data)
            return
        i=0
        current=self.head
        while current and i<index:
            current=current.next
            i+=1
        if current is None:
            if i==index:
                self.insert_at_end(data)
                return
            print("Index out of bounds")
            return
        previous=current.prev
        previous.next=new_node
        new_node.prev=previous
        new_node.next=current
        current.prev=new_node
    def delete_begin(self):
        if not self.head:
            print("Empty")
            return
        if self.head.next is None:
            self.head=None
        self.head=self.head.next
        self.head.prev=None
    def delete_end(self):
        if not self.head:
            print("Empty")
            return
        current=self.head
        while current.next:
            prev=current
            current=current.next
        prev.next=None
        current.prev=None
    def delete_data(self,data):
        if self.head is None:
            print("Empty")
            return
        current=self.head
        prev=current
        while current:
            if current.data==data:
                previous.next=nextnode
                nextnode.prev=previous
                return
            previous=current
            current=current.next
            nextnode=current.next
    def traversal(self):
        current=self.head
        while current:
            print(current.data,"-> ",end="")
            current=current.next
        print("end")
    def reverse(self):
        current=self.head
        previous=None
        while current:
            nextnode=current.next
            current.next=previous
            current.prev=nextnode
            previous=current
            current=nextnode
        self.head=previous
dll=DoublyLinkedList()
dll.insert_at_begin(5)
dll.traversal()
dll.insert_at_begin(1)
dll.traversal()
dll.insert_at_end(0)
dll.traversal()
dll.insert_at_index(2,5)
dll.insert_at_index(2,1)
dll.traversal()
dll.reverse()
dll.traversal()