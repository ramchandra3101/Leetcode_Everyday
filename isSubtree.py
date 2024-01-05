class TreeNode():
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right=None

class solution:
  def isSubtree(self,root,subroot):
    if root and not subroot:
      return True
    if subroot and not root:
      return False
    if self.same(root,subroot): # checking each node of root and subroot here.
      return True
    return self.isSubtree(root.left,subroot) or self.isSubtree(root.right,subroot) #In case of parent node wont match then moving to child nodes to check with subRoot.
    
  def same(self,root,subroot):
    if not root and not subroot: #We will get to case where both are None When all the nodes we are passing through in root and subrroots are equal.Then we return True.If they are no equal the definitely the function will return False.
      return True
    if root and subroot and root.val==subroot.val:
      return self.same(root.left,subroot.left) and self.same(root.right,subroot.right)
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

if __name__ == "__main__":
  root_node = build_tree()
  subroot_node = build_tree()
  s = solution()
  print(s.isSubtree(root_node,subroot_node))
