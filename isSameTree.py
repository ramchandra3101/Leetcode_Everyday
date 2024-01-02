from collections import deque #deque has special feature that it can be operated from both ends for both appending and removing elements.
class TreeNode():
   def __init__(self, val):
      self.val = val
      self.left = None
      self.right = None

class solution(): #BFS solution
   def isSameTree(self,p,q):
     queue1,queue2=deque([p]),deque([q])
     while queue1 and queue2:
            for i in range(len(queue1)):
                currentp,currentq=queue1.popleft(),queue2.popleft()
                if currentp and currentq:
                    if currentp.val != currentq.val:
                        return False
                    queue1.append(currentp.left)
                    queue2.append(currentq.left)
                    queue1.append(currentp.right)
                    queue2.append(currentq.right)
                elif currentp or currentq: #using elif instead of if because it will override the previous conditions.
                    return False
                
     return not queue1 and not queue2
 
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
  root_node1 = build_tree()
  s = solution()
  print(s.isSameTree(root_node,root_node1))
  
      