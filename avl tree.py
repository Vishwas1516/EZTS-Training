#AVL TREE
'''class node:
    def _init_(self,data):
        self.val=data 
        self.left=None
        self.right=None
        self.height=1


def insert(root,key):
    if not root:
        return node(key)
    if key<root.val:
        root.left=insert(root.left,key)
    else:
        root.right=insert(root.right,key)
   
    root.height=1+max(ght(root.left),ght(root))
    bf=getbf(root)
#rr rotation
    if bf>1 and key<root.left.val:
        return rightRotate(root)
    #rl rotation
    if bf>1 and key<root.left.val:
        root.left=leftRotate(root.left)
        return rightRotate(root)
    #ll
    if bf<-1 and key>root.right.val:
        return leftRotation(root)
 
    #lr
    if bf<-1 and key>root.right.val:
        root.right=rightRotate(root.right)
        return leftRotation(root)
    return root

def ght(root):
    if not root:
        return 0
    return root.height

def getbf(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)

def leftRotate(A):
    B=A.right
    temp=B.left

    B.left=A
    A.right=temp

    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))
    return 0

def inorder(root):
    if  not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)



if __name__ == "_main_":
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i)'''



n= int(input())
commas = 1
res=0
cur=1000
while cur<=n:
    next=cur*1000
    nums=min(n-cur+1,next-cur)
    res+=nums*commas
    cur=next
    commas+=1
print(res)







    
