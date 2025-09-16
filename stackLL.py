class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackll:
    def __init__(self):
        self.top=None
    def push(self,data):
        newnode=Node(data)
        if not self.top:
            self.top=newnode
            return
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.isempty():
            print("Empty stack")
            return
        item=self.top.data
        self.top=self.top.next
        print("Popped :",item)
    def peek(self):
        if self.isempty():
            print("Empty")
            return
        print(self.top.data)
    def isempty(self):
        return self.top is None
    def display(self):
        current=self.top
        if self.isempty():
            print("empty")
            return
        while current:
            print(current.data)
            current=current.next
s1=stackll()
print(s1.isempty())
s1.push(7)
s1.display()
s1.push(2)
print(s1.isempty())
s1.peek()
s1.pop()
s1.display()