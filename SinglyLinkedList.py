class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            head=new_node
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def insert_at_index(self,data,index):
        new_node=Node(data)
        i=0
        current=self.head
        while current and i<index:
            i+=1
            current=current.next
        if current is None:
            print("Index out of bounds")
            return
        new_node.next=current.next
        current.next=new_node
    def delete_at_begin(self):
        if not self.head:
            print("Empty")
            return
        self.head=self.head.next
    def delete_at_end(self):
        current=self.head
        if not current:
            print("Empty")
            return
        if current.next==None:
            self.head=None
            return
        while current.next!=None:
            prev=current
            current=current.next
        prev.next=None
    def delete_data(self,data):
        if not self.head:
            print("Empty")
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
        print("Not found")
    def traversal(self):
        current=self.head
        if not current:
            print("Empty")
            return
        while current:
            print(current.data,"--> ",end="")
            current=current.next
        print("end")
    def length(self):
        current=self.head
        i=0
        while current:
            i+=1
            current=current.next
        print("Length of linked list is",i)
    def search(self,data):
        ind=0
        current=self.head
        while current:
            if current.data==data:
                print(data,"Found at Index :",ind)
                return
            ind+=1
            current=current.next
        print("Not found")
    def reverse(self):
        current=self.head
        prev=None
        while current:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        self.head=prev

sll=SLL()
sll.insert_at_begin(2)
sll.traversal()
sll.insert_at_begin(5)
sll.traversal()
sll.insert_at_end(7)
sll.traversal()
sll.insert_at_index(3,5)
sll.traversal()
sll.length()
sll.delete_data(2)
sll.traversal()
sll.insert_at_end(9)
sll.insert_at_end(13)
sll.traversal()
sll.reverse()
sll.traversal()
sll.search(9)
sll.delete_at_begin()
sll.traversal()
sll.delete_at_end()
sll.traversal()

