class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
  def reorderList(self,head1):
    head=head1
    if not head1.next:
      return head1
    slow,fast=head1,head1.next
    while fast and fast.next:
      slow=slow.next
      fast=fast.next.next
    
    head2=slow.next
    slow.next=Prev=None
    while head2:
      nxt=head2.next
      head2.next=Prev
      Prev=head2
      head2=nxt
    
    head2=Prev
    while head2:
      temp1,temp2=head1.next,head2.next
      head1.next=head2
      head2.next=temp1
      head1,head2=temp1,temp2
    return head
        
nums=input("Enter the values for list you want to create with spaces:").split()
Linked_list=ListNode(None)

current=Linked_list
for i in nums:
  current.next=ListNode(int(i))
  current=current.next
Linked_list=Linked_list.next #we are doing this because we have initialised Linked_list with None

s=Solution()
result=s.reorderList(Linked_list)
while result:
  print(result.val,end=" ")
  result=result.next





