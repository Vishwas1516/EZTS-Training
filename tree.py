#preorder
'''class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def preorder(root):
    if root == None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)


if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)

    root.left.left=node(4)
    root.left.right=node(5)

    root.right.left=node(6)
    root.right.right=node(7)

    preorder(root)'''






#postorder
'''class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def postorder(root):
    if root == None:
        return
    print(root.value)
    postorder(root.right)
    postorder(root.left)


if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)

    root.left.left=node(4)
    root.left.right=node(5)

    root.right.left=node(6)
    root.right.right=node(7)

    postorder(root)'''



#levelorder
'''class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def levelorder(root):
    q=[root]
    q.append(None)


    while len(q)>0:
        curr =q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                print()
                q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)

if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)

    root.left.left=node(4)
    root.left.right=node(5)

    root.right.left=node(6)
    root.right.right=node(7)

    root.left.right.left=node(8)
    root.left.right.right=node(9)

    root.right.right.right=node(10)
    root.left.right.left.left=node(11)

    root.left.right.left.right=node(13)
    

    levelorder(root)'''



#height 
'''class node:
    def __init__(self,data):
        self.left=None
        self.value=data
        self.right=None
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def preorder(root):
    if root==None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
def postorder(root):
    if root==None:
        return
    
    postorder(root.left)
    
    postorder(root.right)
    print(root.value)

def bfs(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        cur=Q.pop(0)
        if  cur == None:
            if len(Q)==0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(cur.value,end=" ")
            if (cur.left!=None):
                Q.append(cur.left)
            if (cur.right!=None):
                Q.append(cur.right)
def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1
    
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    root.right.left=node(6 )
    root.right.right=node(7)
    root.right.right.right=node(11)
    inorder(root)
    print()
    preorder(root)
    print()
    postorder(root)
    bfs(root)
    print(height(root))'''








