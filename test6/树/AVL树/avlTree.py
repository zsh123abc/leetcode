from tree import BinarySerchTree
from node import TreeNode

class AVLTree(BinarySerchTree):
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


    def updateBalance(self, node):#更新平衡因子
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            pass
