class stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.items:
            print("Empty stack")
            return
        item=self.items.pop()  
        print("Popped item:",item)
    def peek(self):
        if not self.items:
            print("Empty stack")
            return
        print("Top item :",self.items[-1])
    def length(self):
        print("length of stack is:",len(self.items))
    def traversal(self):
        for item in self.items:
            print(item)
s=stack()
s.push(1)
s.traversal()
s.push(12)
s.peek()
s.push(5)
s.peek()
s.pop()
s.traversal()
