# #Intuition
# My initial idea is to initially count the total number of nodes in the list. Then, by subtracting 'n' from this count, we can determine the position of the element we want to remove.

# Approach
# My approach begins by first determining the number of nodes in the list. To achieve this, I employed a temporary variable to traverse the list, incrementing the count value for each node until the next value for a particular node becomes 'None.'

# Next, I introduced a variable 'j' to locate the node that precedes the one we intend to remove. In cases where the list contains only one node, the only option is to remove that node itself. In such instances, I set 'head' to 'None.' If 'j' equals '0,' it signifies that we need to remove the first element. In this scenario, I simply updated 'head' to 'head.next,' effectively deleting the first node.

# The pivotal step in this process involves traversing the list until reaching the node just before the one to be deleted. I achieved this by navigating through the 'before' variable until I reached the target node, then unlinking the node slated for removal from its preceding element.

# Complexity
# Time complexity:
# O(n) in worst case scenario

# Space complexity:
# O(1)

# Code
# Definition for singly-linked list.
class ListNode: #This is the class for creating a node
    def __init__(self, val=0, next=None):#This is the constructor for creating a node
        self.val = val#This is the value of the node
        self.next = next#This is the pointer to the next node
class Solution:
    def removeNthFromEnd(self, head, n):#This is the function to remove the nth node from the end of the list
        temp=head#This is the temporary variable to traverse the list
        count=1#This is the variable to count the number of nodes in the list
        while temp.next:#This is the loop to traverse the list
            temp=temp.next#This is the statement to traverse the list
            count+=1#This is the statement to increment the count
        n=count-n#This is the statement to determine the position of the node to be removed
        if n==0:#This is the condition to check if the node to be removed is the first node
            if head.next:return head.next#This is the condition to check if the list contains more than one node
        elif n==1:#This is the condition to check if the node to be removed is the second node
            if head.next:#This is the condition to check if the list contains more than two nodes
                head.next=head.next.next
            return head
        else:#This is the condition to check if the node to be removed is not the first or second node
            current=head
            while(n-1):#This is the loop to traverse the list until the node just before the node to be removed
                current=current.next#
                n-=1
            if current.next:
                current.next=current.next.next#This is the statement to unlink the node to be removed from the list
                
            return head
    
nums=input("Enter the values for list you want to create with spaces:").split()
n=int(input("Enter the value of n(The index of node you want to remove from end):"))
Linked_list=ListNode(None)

current=Linked_list
for i in nums:
  current.next=ListNode(int(i))
  current=current.next
Linked_list=Linked_list.next #we are doing this because we have initialised Linked_list with None

s=Solution()
result=s.removeNthFromEnd(Linked_list,n)
while result:
  print(result.val,end=" ")
  result=result.next

