#一个列表包含三个列表，根节点，左子树，右子树
def BinaryTree(r):
    return [r,[],[]]
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        left = [newBranch,t,[]]
        root.insert(1,left)
    else:
        root.insert(1,[newBranch,[],[]])  
    return root
def insertRigth(root,newBranch):
    t = root.pop(2)
    root.insert(newBranch,[],t)
    return root    
def getRootVal(root):
    return root[0]
def setRootVal(root, newVal):         
    root[0] = newVal
def getLeftChild(root):    
    return root[1]
def getRightChild(root):   
    return root[2] 

root = BinaryTree(3)
print(insertLeft(root,4))