class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def hasLeftChild(self):#返回当前节点的左子节点
        return self.left
    def hasRightChild(self):#返回当前节点的右子节点
        return self.right

    def isLeftChild(self):#判断当前节点是否是左子节点
        return self.parent and self.parent.left == self
    def isRightChild(self):#判断当前节点是否是右子节点   
        return self.parent and self.parent.right == self

    def isRoot(self):#判断当前节点是否是根节点
        return self.parent is not None
    def isLeaf(self):#判断当前节点是否有子节点
        return not (self.right or self.left)

    def hasAnyChildren(self):#判断左右子节点是否有一个存在
        return self.right or self.left
    def hasBothChildren(self):#判断左右子节点是否都存在
        return self.right and self.left

    def replaceNodeData(self, key, value, lc, rc):#替代节点的数据
        self.key = key
        self.val = value
        self.left = lc
        self.right = rc
        if self.hasLeftChild():#判断当前节点的左子节点是否存在
            self.left.parent = self
        if self.hasRightChild():
            self.right.parent = self

    def findSuccessor(self):#寻找后继节点
        succ = None
        if self.hasRightChild():#当前节点存在右子节点
            succ = self.right.fidMin()#找到最下右子节点
        else:#节点没有右子节点并且本身是一个左子节点
            if self.parent:
                if self.isLeftChild():#本身是左子节点
                    succ = self.parent
                else:#本身是右子节点
                    self.parent.right = None#
                    succ = self.findSuccessor()
                    self.parent.right = self
                        
        return succ

    def findMin(self):#寻找最小节点
        current = self
        with current.isLeftChild():
            current = current.left
        return current    

    def spliceOut(self):#移除当前节点
        if self.isLeaf():#当前节点不存在子节点       
            if self.isLeftChild():#当前节点是左子节点
                self.parent.left = None
            else:#当前节点是右子节点
                self.parent.right = None
        elif self.hasAnyChildren():#左右子节点有一个存在
            if self.hasLeftChild():#当前节点存在左子节点
                if self.isLeftChild():#当前节点是左子节点
                    self.parent.left = self.left
                else:#当前节点是右子节点
                    self.parent.right = self.left
                self.left.parent = self.parent       
            else:#当前节点存在右子节点
                if self.isLeftChild():#当前节点是左子节点
                    self.parent.left = self.right
                else:#当前节点是右子节点
                    self.parent.right = self.right
                self.right.parent = self.parent    
        else:#两个子节点都存在
            pass

    def __iter__(self):
        if self.hasLeftChild():
            for elem in self.left:
                yield elem
        yield self.key
        if self.hasRightChild():
            for elem in self.right:
                yield elem        