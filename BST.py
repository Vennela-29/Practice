  
class BinarySearchTree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def add(self,item):
        node=BinarySearchTree(item)
        if item<self.data:
            if self.left is None:
                self.left=node
            else:
                self.left.add(item)
        if item>self.data:
            if self.right is None:
                self.right=node
            else:
                self.right.add(item)
    def InOrderdisplay(self):
        if self.left:
            self.left.InOrderdisplay()
        print(self.data,end=" ")
        if self.right:
            self.right.InOrderdisplay()
    def PreOrder(self):
        print(self.data,end=" ")
        if self.left:
            self.left.PreOrder()
        if self.right:
            self.right.PreOrder()
    def PostOrder(self):
        if self.left:
            self.left.PostOrder()
        if self.right:
            self.right.PostOrder()
        print(self.data,end=" ")
    def search(self,item):
        if item==self.data:
            return True
        elif item<self.data:
            if self.left is None:
                return False
            return self.left.search(item)
        else:
            if self.right is None:
                return False
            return self.right.search(item)
bt=BinarySearchTree(6)
bt.add(10)
bt.add(5)
bt.add(3)
print("Inorder:")
bt.InOrderdisplay()
print("\nPost Order:")
bt.PostOrder()
print("\nPre Order:")
bt.PreOrder()
print("\n",bt.search(3))
print(bt.search(2))