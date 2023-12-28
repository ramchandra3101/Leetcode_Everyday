class ListNode(): #This is the class for creating a node
    def __init__(self, value):
        self.value = value
        self.next = None


class solution:
    def mergeKLists(self, lists):#This is the function to merge k sorted lists
        nums=[]
        head=ans=ListNode(None)#This is the head node of the list to return linkedlist from the function
        for l in lists:#This is the loop to traverse the list of linkedlists
            while l:#This is the loop to traverse each linkedlist
                nums.append(l.value)#This is the statement to append the value of each node of each linkedlist to the nums list
                l=l.next
        for num in sorted(nums):#This is the loop to traverse the sorted list of values of all the nodes of all the linkedlists
            ans.next=ListNode(None) #keeping this ListNode creation on top because if we keep it after ans.value =num,Then it will create extra Node 0 at the end of the list
            ans=ans.next #Keeeping this before to avoid the extra node 0 at the end of the list
            ans.value=num #This is the statement to assign the value of each node of the list to the ans list
        return head.next #by returning head,We will get 0 at the beginning of the list.So we are returning head.next to avoid 0 at the beginning of the list

#The below code is to take input from the user
n=int(input("Enter the number of linkedlists you want to keep in the list: ")) #This is the number of linkedlists we want to keep in the list
lists=[]
list=ListNode(None) #This is the head node of the list of linkedlists
for i in range(n):
    print("Enter the elements of linkedlist ",i+1)
    nums=input("Enter the elements for each linkedlist").split()
    current=list
    for num in nums:
        current.next=ListNode(int(num))
        current=current.next
    lists.append(list.next)
print(lists)
s=solution()
result=s.mergeKLists(lists)
while result:
    print(result.value,end=" ")
    result=result.next








    
