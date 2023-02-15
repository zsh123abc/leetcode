class TreeNode:
    def __init__(self ,v=None):
        self.val = v#节点值
        self.left = None#左子节点
        self.right = None#右子节点
        self.parent = None#父节点


class BST():
    def __init__(self ,node=None):#初始化树
        node = TreeNode(node)
        self.root_node = node#新建根节点
    def insert(self, x):#加入节点
        if self.is_exist(x):#判断节点是否已经存在树中
            return   

        node = TreeNode(x)#新节点
        if self.root_node == None:#根节点为空，为空树
            self.root = node#新节点设置为空节点
        else:#根节点不为空
            par = None#记录当前节点的父节点
            cur = self.root_node#获取根节点
            while cur != None:#当前节点不为空
                par = cur#先记录当前节点，在往后迭代
                if cur.val < x:#新节点值>当前节点值
                    cur = cur.right#往树的右边放
                else:
                    cur = cur.left #往树的左边放

            node.parent = par#新节点的父节点 为 当前节点的父节点
            if par.val<x:#判断为左子节点还是右子节点
                par.right = node#右子节点
            else:
                par.left = node#左子节点

    def is_exist(self, key):
        cur = self.root_node#获取根节点
        while cur != None and cur.val != key:#当前节点！=none并且当前节点值！=要插入节点值
            if key<cur.val:#要插入节点值小于当前节点值
                cur = cur.left#小于往左子树
            else:
                cur = cur.right#大于往右子树
        #三元运算 成立 if 条件 else 不成立        
        return True if cur != None else False #三元运算 当前节点不为None，返回true

    def preorder_tree_walk(self, node):#递归前序遍历树
        if node!=None:#终止条件，节点为空
            print(node.val)
            self.preorder_tree_walk(node.left)
            self.preorder_tree_walk(node.right)


if __name__ == '__main__':
    bs_tree = BST(16)#初始化二叉树,根节点
    #对二叉树做插入操作
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(12)
    bs_tree.insert(6)
    # bs_tree.insert(6)
    bs_tree.insert(20)
    bs_tree.insert(30)
    # bs_tree.insert(30)
    root = bs_tree.root_node
    bs_tree.preorder_tree_walk(root)