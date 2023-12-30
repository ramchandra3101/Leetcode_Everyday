class Solution:
  def Longest_repeating_character_replacement(str,k):
    left=0
    Alpha_count={}
    max_frequency=0 #To count the maximum frequency of maximum repeating character in the string

    for right in range(len(str)):
      Alpha_count[str[right]]=1+Alpha_count.get(str[right],0) #get function usually increments if the key already there in dictionary otherwise it will create a new key with value 1
      max_frequency=max(max_frequency,Alpha_count[str[right]]) #We are taking this max frequency because ww want to store the frequency of character which is maximum in the current window between left and right

      while(right-left+1)-max_frequency>k: #This is key,Here if the current window consists of more changes in characters than k then we have to shrink the window from left side
      
        Alpha_count[str[left]]-=1 #This is the statement to decrement the frequency of character which is maximum in the current window between left
        left+=1
    return right-left+1

string=input("Enter the string: ")
k=int(input("Enter the value of k: "))
result=Solution.Longest_repeating_character_replacement(string,k)
print(result)


#Time Complexity: O(N) where N is the length of the string
#In the above program ,Always consider a window with number character changes. If the number of character changes in the window is greater than k, then shrink the window from left side.