​
if grid[0][0] or grid[-1][-1]:
return -1
else:
nodes_visited = 1
i = 0
j = 0
while True:
if not grid[i][j]:
un = next_step(i, j)
if un:
i, j = un[0], un[1]
else:
return -1
nodes_visited += 1
if i == n-1 and j == n-1:
break
else:
return -1
return nodes_visited
​
ll = [[1,0,0],[1,1,0],[1,1,0]]
re = Solution().shortestPathBinaryMatrix(ll)
print(re)
​
```