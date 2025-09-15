class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queueLL:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,data):
        newnode=Node(data)
        if self.rear is None:
            self.front=self.rear=newnode
            return
        self.rear.next=newnode
        self.rear=newnode
    def dequeue(self):
        if self.front is None:
            print("Empty")
            return
        item=self.front.data
        print("Deque :",item)
        self.front=self.front.next
        if self.front is None:
            self.rear=None
    def display(self):
        if self.front is None:
            print("Empty")
            return
        current=self.front
        while current:
            print(current.data,end=" ")
            current=current.next
        print()
q1=queueLL()
q1.enqueue(3)
q1.display()
q1.enqueue(8)
q1.display()
q1.enqueue(1)
q1.display()
q1.dequeue()
q1.display()