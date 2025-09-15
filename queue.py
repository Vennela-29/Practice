class queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        if not self.items:
            print("empty queue")
            return
        print("Removed :",self.items.pop())
    def length(self):
        print("length :",len(self.items))
    def traversal(self):
        for item in self.items:
            print(item)
q=queue()
q.dequeue()
q.length()
q.enqueue(1)
q.traversal()
q.enqueue(5)
q.traversal()
q.dequeue()
q.traversal()