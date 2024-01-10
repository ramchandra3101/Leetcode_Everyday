class TreeNode():
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None
#SOLUTION1:
class solution():
  def leastcommonancestor(self,root,p,q): #In Binary search tree we have The left child nodes are always smaller than the parent node and the right child nodes are always bigger than the parent node:
    if p.val<root.val and q.val<root.val:
      return self.leastcommonancestor(root.left,p,q)
    elif p.val>root.val and q.val>root.val:
      return self.leastcommonancestor(root.right,p,q)
    else:
      return root
    
  

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

# Example usage:
root=build_tree()
pvalue=input("Enter the value of the p node: ")
qvalue=input("Enter the value of the q node: ")
p=TreeNode(int(pvalue))
q=TreeNode(int(qvalue))
s=solution()
result=s.leastcommonancestor(root,p,q)
print(result.val)






  

