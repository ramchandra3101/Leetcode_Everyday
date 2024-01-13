class TreeNode():
  def __init__(self,val):
    self.val = val
    self.left = None
    self.right = None

class solution: #DFS approach for inorder traversal
  def kthSamllest(self,root,k):
    stack=[]
    current_node=root
    while stack or current_node:
      while current_node:
        stack.append(current_node)
        current_node=current_node.left #we have go to the leftmost node the depth of the tree
      current_node=stack.pop() #once we reach the leftmost node we pop it from the stack and check if it is the kth smallest node or not else we go to the right of the node
      k-=1
      if k==0:
        return current_node.val
      current_node=current_node.right


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

if __name__=="__main__":
  root=build_tree()
  k=int(input("Enter the value of k: "))
  print(solution().kthSamllest(root,k))
    
