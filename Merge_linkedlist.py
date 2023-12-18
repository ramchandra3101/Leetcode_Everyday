class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1, list2):
        ans = ListNode(None)
        current = ans
        while list1 and list2: # we are using AND operation because if any of the list is empty then we don't need to compare
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1: # if list1 is not empty then we need to add the remaining values of list1 to the ans list
            current.next = list1
        if list2:# if list2 is not empty then we need to add the remaining values of list2 to the ans list
            current.next = list2
        return ans.next

a = input("Enter the first linked list values separated by space: ").split()
b = input("Enter the second linked list values separated by space: ").split()

list1 = ListNode(None)
list2 = ListNode(None)

current = list1 #

for i in a:
    current.next = ListNode(int(i))
    current = current.next
 
current = list2
for i in b:
    current.next = ListNode(int(i))
    current = current.next

list1 = list1.next # we are doing this because we have initialized the list1 and list2 with None
list2 = list2.next # we are doing this because we have initialized the list1 and list2 with None

s = Solution()
result = s.mergeTwoLists(list1, list2)

while result:
    print(result.val, end=" ")
    result = result.next
