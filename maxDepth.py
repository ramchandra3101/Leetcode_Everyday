from collections import deque #deque has special feature that it can be operated from both ends for both appending and removing elements.
class TreeNode():
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right=None

#main function to find the depth of Tree

class solution():
  def maxDepth(self,root):
    if not root : #if there is no node in the tree return 0
      return 0
    queue=deque([root]) #creating double ended queue and initialising with root node.
    level=0 # giving level 0 not 1 because the value will get incremented once the root node is removed from queue
    while queue:
      for i in range(len(queue)): #when a node has both right and left nodes,We need to check both nodes first before moving to child nodes of right and left nodes.
        current_node=queue.popleft()
        if current_node.left:
          queue.append(current_node.left)
        if current_node.right:
          queue.append(current_node.right)
      level+=1
    return level
  



#input code for test cases

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
 
# Example usage
if __name__ == "__main__":
  root_node = build_tree()
  s = solution()
  print(s.maxDepth(root_node))



