class Solution(object):
    def numIslands(self, grid):
        no_of_rows=len(grid)
        no_of_columns=len(grid[0])
        isLands=0
        def markVisited(row,column):
            grid[row][column]="X"
            if row-1 in range(no_of_rows) and grid[row-1][column]=="1":
                markVisited(row-1,column)
            if row+1 in range(no_of_rows) and grid[row+1][column]=="1":
                markVisited(row+1,column)
            if column-1 in range(no_of_columns) and grid[row][column-1]=="1":
                markVisited(row,column-1)
            if column+1 in range(no_of_columns) and grid[row][column+1]=="1":
                markVisited(row,column+1)
        for row in range(no_of_rows):
            for column in range(no_of_columns):
                if grid[row][column]=="1":
                    markVisited(row,column)
                    isLands+=1
        return isLands
    
if __name__=="__main__":
    grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","1","0"]]
    obj=Solution()
    print(obj.numIslands(grid))