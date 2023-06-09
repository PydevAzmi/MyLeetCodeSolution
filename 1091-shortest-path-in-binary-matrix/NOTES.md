```python
class Solution(object):
def shortestPathBinaryMatrix(self, grid):
"""
:type grid: List[List[int]]
:rtype: int
"""
n = len(grid)
​
def next_step(i, j):
re = []
if (i+1 < n and j+1 < n) and not grid[i+1][j+1]:
re.append(i + 1)
re.append(j + 1)
elif j+1 < n and not grid[i][j+1]:
re.append(i)
re.append(j + 1)
elif i+1 < n and not grid[i+1][j]:
re.append(i + 1)
re.append(j)
return re
​
if grid[0][0] or grid[-1][-1]:
return -1
else:
nodes_visited = 1
i = 0