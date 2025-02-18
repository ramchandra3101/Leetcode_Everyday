from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        CurrMax , currMin = 1,1
        res = nums[0]
        for num in nums:
            temp = num*CurrMax
            currMax = max(num*CurrMax,num*currMin,num)
            currMin = min(temp,num*currMin,num)
            res = max(res,currMax)
        return res
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))
    print(sol.maxProduct([-2,0,-1]))
