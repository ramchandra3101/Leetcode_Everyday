from math import inf 
class TreeNode():
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class solution():
  def validBST(self,root):
    # def BFS(root,min_value=float(-inf),max_value=float(inf)):
    #   if not root:
    #     return True
    #   if not min_value<root.val<max_value:
    #    return False
    #   return BFS(root.left,min_value,root.val) and BFS(root.right,root.val,max_value)
    # return BFS(root)
    def DFS(root,l):
      if not root:
        return True
      DFS(root.left,l)
      l.append(root.val)
      DFS(root.right,l)
      return l
    p=DFS(root,[])
    if not p==sorted(p): #This will return False if the lists is same as sorted because if any node i
      return False
    
    if len(set(p))==len(p):
      return True
    
    return False
      

def build_tree():
  values=input("Enter the values for the tree in the form of list separated by space: ").split()
  if not values:
    return None
  root_node=TreeNode(int(values[0]))
  queue=[root_node]
  i=1
  while i < len(values):
    current_node=queue.pop(0)
    if i<len(values) and values[i]!="null":
      left_child=TreeNode(int(values[i]))
      current_node.left=left_child
      queue.append(left_child)
    i+=1

    if i<len(values) and values[i]!="null":
      right_child=TreeNode(int(values[i]))
      current_node.right=right_child
      queue.append(right_child)
    
    i+=1
  return root_node

#Example Usage
root=build_tree()
print(solution().validBST(root))


    
    
