class circular_queue:
    def __init__(self):
        self.front=-1
        self.rear=-1
        self.MAX_SIZE=3
        self.items=[0]*self.MAX_SIZE
    def enqueue(self,data):
        if self.front==-1:
            self.front+=1
            self.rear+=1
        elif self.rear==self.MAX_SIZE and self.front!=0:
            self.rear=0
        elif (self.rear+1)%self.MAX_SIZE==self.front:
                print("Overflow")
                return
        else:
            self.rear=(self.rear+1)%self.MAX_SIZE
        self.items[self.rear]=data
    def dequeue(self):
        if self.isempty():
            print("Empty circular queue")
            return
        item=self.items[self.front]
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.MAX_SIZE
        print("Dequeued :",item)
    def isempty(self):
        if self.front==-1:
            return True
        return False
    def display(self):
        if self.isempty():
            print("Underflow")
            return
        i=self.front
        while True:
            print(self.items[i])
            if i==self.rear:
                break
            i=(i+1)%self.MAX_SIZE
cq=circular_queue()
print(cq.isempty())
cq.enqueue(10)
cq.display()
print(cq.isempty())
cq.enqueue(20)
cq.display()
cq.dequeue()
cq.display()
cq.enqueue(4)
cq.display()
cq.enqueue(7)
cq.display()
cq.enqueue(12)
cq.enqueue(5)
cq.display()
