from typing import List
class LIS:
    def LongestIncreasingSubsequence(self,nums:List[int])->int:
        temp =[nums[0]]
        for num in nums:
            if num > temp[-1]:
                temp.append(num)
            if num in temp:
                continue
            else:
                closest = self.findClosest(temp,num)
                if closest == len(temp):
                    temp[-1]=num
                else:
                    temp[closest] = num
        return len(temp)
    
    def findClosest(self,temp:List[int],num:int)->int:
        left,right = 0,len(temp)-1
        nearest = len(temp)
        while left < right:
            mid = (left+right)//2
            if temp[mid] < num:
                left = mid + 1
            else:
                nearest = mid
                right = mid-1
        return nearest

if __name__ == "__main__":
    nums = [[10,9,2,5,3,7,101,18],[0,1,0,3,2,3],[7,7,7,7,7,7,7]]
    lis = LIS()
    for num in nums:
        print(lis.LongestIncreasingSubsequence(num))

    