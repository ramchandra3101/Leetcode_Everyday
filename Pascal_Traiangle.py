from typing import List
class Solution:
    def Pascal_Trainagle(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res =[]
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j]= res[i-1][j-1] + res[i-1][j]
            res.append(row)
        return res
    
# Test Cases
sol = Solution()
print(sol.Pascal_Trainagle(11))
assert sol.Pascal_Trainagle(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
assert sol.Pascal_Trainagle(1) == [[1]]
assert sol.Pascal_Trainagle(2) == [[1],[1,1]]
assert sol.Pascal_Trainagle(0) == []
assert sol.Pascal_Trainagle(3) == [[1],[1,1],[1,2,1]]
assert sol.Pascal_Trainagle(4) == [[1],[1,1],[1,2,1],[1,3,3,1]]
assert sol.Pascal_Trainagle(6) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]

print("All test cases pass")

        
        


        