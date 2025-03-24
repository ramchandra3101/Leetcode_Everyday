"""Given an array of integers, determine the number of triplets i, j, k such that i < j< k and arri]*arr]*arr[k] is even. Return the answer modulo
10° + 7.

Example
nums = [2, 4, 8, 2]

There are 4 triplets that meet the criteria:
(1,2,3): 2*4*8 = 64 (even)
(1,2, 4): 2*4*2 = 16 (even)
(1,3, 4): 2*8*2 = 32 (even)
(2,3, 4): 4*8*2 = 64 (even)
Function Description
Complete the function evenproduct in the editor below.
evenproduct has the following parameter: int nums[n]: an array of integers
Returns
int: the number of triplets, modulo (10% + 7)

Constraints
• 3 ≤n≤ 105
• 1 ≤ numsli] = 109 (0 si <n)

Sample Input For Custom Testing

1000000000
1000000000
size n = 3
nums = [1000000000, 1000000000, 1]
Sample Output
1
Explanation
There is one triplet:
1000000000*1000000000*1 =1000000000000000000"""

def EvenProduct(n, nums):
    if n!=len(nums):
        return("Incorrect Inputs")
    MOD = 10**9+7
    oddCount = 0
    totalTriplets = n*(n-1)*(n-2)//6
    for num in nums:
        if num%2!=0:
            oddCount+=1
    oddTriplets = oddCount*(oddCount-1)*(oddCount-2)//6
    evenTriplets = totalTriplets - oddTriplets
    return evenTriplets%MOD

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(EvenProduct(n, nums))





    