class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.left = None
        self.rigth = None
    def getRightChild(self):
        return self.rigth
    def getLeftChild(self):
        return self.left
    def setRootVal(self, obj):
        self.key = obj
    def getRootVal(self):
        return self.key

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
            
            
    def insertRight(self, newNode):
        b = True
        while b:
            if self.rigth == None:
                self.rigth = BinaryTree(newNode)
                b = False
            else:
                self.rigth = self.rigth.getRightChild()
                # print('aaaaa')
                    
    def preorder(self):
        print(self.key)
        if self.left!=None:
            self.left.preorder()
        if self.rigth!=None:
            self.rigth.preorder()
            
root = BinaryTree('a')
# myTree2 = BinaryTree('b')
# myTree3 = BinaryTree('c')
# myTree4 = BinaryTree('d')
# print(root.getRootVal())

# root.insertLeft('b')
# root.insertLeft('c')
# print(root.getLeftChild().getRootVal())

root.insertLeft('b')
root.insertLeft('d')
root.insertRight('c')
root.preorder()
# print(root.getRightChild().getRootVal())
    