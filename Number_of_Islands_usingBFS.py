from collections import deque;
class Solution(object):
  def noOfIslands(grid):
    if not grid:
      return 0
    rows = len(grid)
    cols = len(grid[0])
    IsLands=0
    visited=set()
    def bfs(r,c):
      q=deque()
      q.append((r,c))
      visited.add((r,c))
      while q:
        r,c =q.popleft()
        directions=[[0,1],[0,-1],[1,0],[0,1]]
        for dr,dc in directions:
          row,column=dr+r,dc+c
          if row in range(rows) and column in range(cols) and grid[row][column]=="1" and (row,column) not in visited:
            q.append((row,column))
            visited.add((row,column))



    for r in range(rows):
      for c in range(cols):
        if grid[r][c]=="1" and (r,c) not in visited:
          bfs(r,c)
          IsLands+=1 
    return IsLands

if __name__ == "__main__":
  grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"]
  ]
  print(Solution.noOfIslands(grid))