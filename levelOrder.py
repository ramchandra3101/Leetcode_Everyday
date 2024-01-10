from collections import deque
class TreeNode():
  def __init__(self,val=None):
    self.val = val
    self.left = None
    self.right = None

class Solution():
  def levelOrder(self,root):
    queue=deque()
    queue.append(root)
    main_list=[]
    if not root:
      return main_list
    while queue:
      level_list=[]
      for i in range(len(queue)):
        current_node=queue.popleft()
        level_list.append(current_node.val)
        if current_node.left:
          queue.append(current_node.left)
        if current_node.right:
          queue.append(current_node.right)
      main_list.append(level_list) #append the level_list to the main_list each time when the level_list is filled with the values of the current level
      del level_list
    return main_list
  
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

# Example usage:
root=build_tree()
s=Solution()
result=s.levelOrder(root)
print(result)


  
      


    

