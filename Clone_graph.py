from collections import deque

node=[[2,4],[1,3],[2,4],[1,3]]
q=deque([node])

cur=q.popleft()
print(cur)