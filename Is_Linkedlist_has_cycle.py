class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def hasCycle(self, head) -> bool:
        if head and head.next:#This is the condition to check if the list contains more than one node
            slow=head
            fast=head
            while fast and fast.next:#checking both fast and fast.next because if we check only fast.next then we will get error when the list has even number of elements
                slow=slow.next
                fast=fast.next.next
                if slow==fast:#This is the condition to check if the list has a cycle.If there is cycle then slow and fast will meet at some point
                    return True
        return False

nums=input("Enter the list of number for Linked List: ").split()
pos=int(input("Enter the position of the node you want to connect to: ")) #This is the position of the node to which we want to connect the last node of the list
head=ListNode(int(nums[0]))
temp=head#Temporary variable to traverse the list
for i in range(1,len(nums)):
    temp.next=ListNode(int(nums[i]))
    temp=temp.next
if pos!=-1:
    temp=head
    for i in range(pos):#This is the loop to traverse the list until the node at the position we want to connect to connect the tail of the list
        temp=temp.next
    tail=temp#This is the node at the position we want to connect to connect the tail of the list
    while tail.next:
        tail=tail.next
    tail.next=temp#This is the statement to connect the tail of the list to the node at the position we want to connect to connect the tail of the list
s=Solution()
result=s.hasCycle(head)
print(result)

#note that in the question we dont have position as the parameter but we have it here because we need to create a cycle in the linked list to check if the linked list has a cycle or not
