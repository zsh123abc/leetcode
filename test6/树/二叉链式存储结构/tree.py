class TreeNode:
    def __init__(self,data = None,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self,root = None):
        self.root = root
    def preOder(self,root):#递归遍历二叉树
        if root is not None:
            print(root.data)
            self.preOder(root.left)
            self.preOder(root.right)

    def preOder2(self,root):#非递归遍历二叉树，利用栈保存节点
        s = []
        node = root #获取到根节点
        s.append(node)#讲根节点存入列表末尾
        while s:
            node = s.pop()#取出列表末尾的节点
            print(node.data)
            while node is not None:
                if node.left is not None:
                    print(node.left.data)
                if node.right is not None:
                    s.append(node.right)
                node = node.left

    def search(self,value):
        s = []
        node = root #获取到根节点
        s.append(node)#讲根节点存入列表末尾
        while s:
            node = s.pop()#取出列表末尾的节点
            if node.data == value:
                return True
            while node is not None:
                if node.left is not None:
                    if node.left.data == value:
                        return True
                if node.right is not None:
                    s.append(node.right)
                node = node.left

if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    left2 = TreeNode(4)
    r = TreeNode(5)
    right = TreeNode(3)
    root.left = left
    root.right = right
    root.left.left = left2
    root.left.right = r

    myTree = Tree(root)
    myTree.preOder2(root)
    print("..")
    value = myTree.search(5)
    print(value)

