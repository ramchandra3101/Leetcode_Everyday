class ListNode(): #This is the class for creating a node
    def __init__(self, value):
        self.value = value
        self.next = None


class solution:
    def mergeKLists(self, lists):#This is the function to merge k sorted lists
        # nums=[]
        # head=ans=ListNode(None)#This is the head node of the list to return linkedlist from the function
        # for l in lists:#This is the loop to traverse the list of linkedlists
        #     while l:#This is the loop to traverse each linkedlist
        #         nums.append(l.value)#This is the statement to append the value of each node of each linkedlist to the nums list
        #         l=l.next
        # for num in sorted(nums):#This is the loop to traverse the sorted list of values of all the nodes of all the linkedlists
        #     ans.next=ListNode(None) #keeping this ListNode creation on top because if we keep it after ans.value =num,Then it will create extra Node 0 at the end of the list
        #     ans=ans.next #Keeeping this before to avoid the extra node 0 at the end of the list
        #     ans.value=num #This is the statement to assign the value of each node of the list to the ans list
        # return head.next #by returning head,We will get 0 at the beginning of the list.So we are returning head.next to avoid 0 at the beginning of the list

        if not lists or len(lists)==0:
            print("Empty list")
        while len(lists)>1:
            mergedlists=[]
            for i in range(0,len(lists),2):
                mergedlists.append(self.mergeTwoLists(lists[i],lists[i+1] if (i+1)<len(lists) else None))
            lists=mergedlists
        return lists[0]
       
    
    def mergeTwoLists(self, l1, l2):
        dummy=ListNode(0)
        current=dummy
        while l1 and l2:
            if l1.value<l2.value:
                current.next=l1
                l1=l1.next
            else:
                current.next=l2
                l2=l2.next
            current=current.next
        if l1:
            current.next=l1
        if l2:
            current.next=l2
        return dummy.next
    
if __name__=="__main__":
    #The below code is to take input from the user
    n=int(input("Enter the number of linkedlists you want to keep in the list: ")) #This is the number of linkedlists we want to keep in the list
    lists_input=[]
    list=ListNode(None) #This is the head node of the list of linkedlists
    for i in range(n):
        print("Enter the elements of linkedlist ",i+1)
        nums=input("Enter the elements for each linkedlist").split()
        current=list
        for num in nums:
            current.next=ListNode(int(num))
            current=current.next
        lists_input.append(list.next)

    lists_input_copy = [node for node in lists_input] #taking copy because ,after printing the lists_input,lists_input will be empty.Because we are traversing to end for printing
    for i in range(len(lists_input)):
        while lists_input[i]:
            print(lists_input[i].value,end=" ")
            lists_input[i]=lists_input[i].next
        
    s = solution()
    result=s.mergeKLists(lists_input_copy)
    print("Merged List:")
    while result:
        print(result.value, end=" ")
        result = result.next









    
