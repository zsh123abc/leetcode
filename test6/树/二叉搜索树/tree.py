from test6.树.AVL树.node import TreeNode
class BinarySerchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size 

    def put(self,key,val):#重复键问题
        if self.root:#存在根节点
            self._put(key,val,self.root)#调用递归函数，找到叶子节点
        else:#不存在根节点
            self.root = TreeNode(key,val)#新节点设置为根节点
        self.size+=1#记录树有多少个节点

    def _put(self, key, val, currentNode):   
        if key <currentNode.key:#小放左边
            if currentNode.hasLeftChild():#左子节点存在就一直递归，知道最后左子节点不存在
                self._put(key,val,currentNode.left)
            else:#一直找到树的叶子节点
                currentNode.left = TreeNode(key,val)#设置新节点为当前节点的左子节点
        else:#大放右边
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.right)
            else:
                currentNode.right = TreeNode(key,val)

    def __setitme__(self,k,v):
        self.put(k,v)

    def get(self,key):#通过键key查找树中节点对应的值val
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.val
            else:
                return None    
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.left)
        else:
            return self._get(key,currentNode.right)

    def __getitem__(self,key):
        return self.get(key)


    def __contains__(self,key):
        if self.get(key):
            return True
        else:
            return False    

    def delete(self,key):#根据键删除节点
        if self.size == 1 and self.root.key == key:
            self.root == None
        elif self.size > 1:
            node = self._get(key, self.root)
            if node:
                self.remove(node)#找到待删除节点
            else:
                raise KeyError('节点不存在')
            self.size -= 1    
        else:
            raise KeyError('节点不存在')

    def remove(self,node):
        if node.isLeaf():#没有子节点
            if node.isLeftChild():#没有左子节点
                node.parent.left = None
            else:#没有右子节点
                node.parent.right = None

        elif node.hasBothChildren():#存在两个子节点
            curr = node.findSuccessor()
            curr.spliceOut()
            node.key = curr.key
            node.val = curr.val

        else:  
            if node.hasLeftChild():#左子节点存在
                if node.isLeftChild():#当前节点是左子节点
                    # 跳过当前节点，相当于删除了当前节点
                    node.left.parent = node.parent#当前节点的左子节点的父节点=当前节点的父节点
                    node.parent.left = node.left#父节点的左子节点=当前节点的左子节点
                elif node.isRightChild():#当前节点是右子节点
                    node.left.parent = node.parent
                    node.parent.right = node.left #将当前节点的左子节点接在父节点左边
                else:
                    node.replaceNodeData(node.left.key,
                                        node.left.val,
                                        node.left.left,
                                        node.left.right)
            else:#右子节点存在
                if node.isLeftChild():
                    node.right.parent = node.parent
                    node.parent.left = node.right #将当前节点的右节点接在父节点右边
                elif node.isRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replaceNodeData(node.right.key,
                                        node.right.val,
                                        node.right.left,
                                        node.right.right)    
                                

if __name__ == '__main__':
    tree = BinarySerchTree()
    tree.put(10,1)
    tree.put(20,2)
    tree.put(30,3)
    myiter = iter(tree.root)
    # print(next(myiter))
    # print(next(myiter))
    # print(next(myiter))
    # getkey = tree.get(30)
    tree.delete(100)
    getkey = tree.get(10)
    print(getkey)
    print(next(myiter))
    print(next(myiter))
    # print(next(myiter))