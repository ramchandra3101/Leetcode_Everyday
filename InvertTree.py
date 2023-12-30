class TreeNode():
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
  
class Solution:
  def InvertTree(self, root):
    if not root:return
    temp=root.left
    root.left=root.right
    root.right=temp
    self.InvertTree(root.left)
    self.InvertTree(root.right)
    return root

def build_tree():
    value = int(input("Enter the value for the root node: "))
    root = TreeNode(value)
    build_tree_recursive(root)
    return root

def build_tree_recursive(node):
    left_value = int(input(f"Enter the value for the left child of {node.val} (enter -1 if none): "))
    if left_value != -1:
        node.left = TreeNode(left_value)
        build_tree_recursive(node.left)

    right_value = int(input(f"Enter the value for the right child of {node.val} (enter -1 if none): "))
    if right_value != -1:
        node.right = TreeNode(right_value)
        build_tree_recursive(node.right)

# Example usage
if __name__ == "__main__":
    root_node = build_tree()
    

    # Create a solution object and invert the tree
    

    # Print the inverted tree
    def print_tree(node):
      if not node:
          return
      print(node.val, end=" ")
      print_tree(node.left)
      print_tree(node.right)
      
    print("\nOriginal Tree:")
    print_tree(root_node)

    solution = Solution()
    inverted_tree_root = solution.InvertTree(root_node)

    print("\nInverted Tree:")
    print_tree(inverted_tree_root)
 
