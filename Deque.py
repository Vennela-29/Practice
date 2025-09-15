from collections import deque
class deque:
    def __init__(self):
        self.d=[]
        self.front=self.rear=-1
        self.MAX=5
    def append(self,data):
        if self.isfull():
            print("Overflow")
            return
        if self.front==-1:
            self.front+=1
        self.rear+=1
        self.d.append(data)
    def appendleft(self,data):
        self.d.insert(0,data)
    def pop(self):
        if self.isempty():
            print("Underflow")
            return
        if self.front==self.MAX-1:
            self.front=0
        elif self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front+=1
        return self.d.pop()
    def popleft(self):
        if self.isempty():
            print("Underflow")
            return
        item=self.d[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        elif self.front==self.MAX-1:
            self.front=0
        else:
            self.front+=1
        self.d.remove(item)
        print("Popped:",item)
        return
    def length(self):
        print("Length :",len(self.d))
    def display(self):
        for item in self.d:
            print(item,end=" ")
        print()
    def isfull(self):
        if (self.front==0 and self.rear==self.MAX-1) or self.front==self.rear+1:
            return True
        return False
    def isempty(self):
        if self.front==-1:
            return True
        return False
d1=deque()
d1.append(5)
d1.display()
d1.appendleft(3)
d1.display()
d1.append(7)
d1.display()
print("Popped :",d1.pop())
d1.display()
d1.length()
d1.popleft()
d1.display()