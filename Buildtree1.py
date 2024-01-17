from collections import deque
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    #solution1
    def Buildtree(self,preorder,inorder):
        preorder_queue=deque(preorder)
        inorder_map={}
        for i in range(len(inorder)):
            inorder_map[inorder[i]]=i
        return self.Buildtreehelper(preorder_queue,inorder_map,0,len(inorder)-1)
    def Buildtreehelper(self,preorder,inorder,inorder_start,inorder_end):
        if not preorder:
            return None
        n=preorder.popleft()
        index=inorder[n]
        root=TreeNode(n)
        if index-inorder_start>0:
            root.left=self.Buildtreehelper(preorder,inorder,inorder_start,index-1)
        if inorder_end-index>0:
            root.right=self.Buildtreehelper(preorder,inorder,index+1,inorder_end)
        return root
    
if __name__ == "__main__":
    s=Solution()
    preorder=input("Preorder: ").split()
    inorder=input("Preorder: ").split()
    root=s.Buildtree(preorder,inorder)
    #printing Tree
    queue=deque()
    queue.append(root)
    while queue:
        node=queue.popleft()
        print(node.val,end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


            
