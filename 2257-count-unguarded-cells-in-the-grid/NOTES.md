```
class Solution:
def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
counter = 0
updated_cells = [[2 if ([r,c] in walls or [r,c] in guards) else 0  for c in range(n)] for r in range(m)]
​
for (x,y) in guards:
# down
for i in range(x+1, m):
if updated_cells[i][y] == 2:
break
updated_cells[i][y] = -1
​
# up
for i in range(x-1, -1,-1):
if updated_cells[i][y] == 2:
break
updated_cells[i][y] = -1
​
# rigth
for i in range(y+1, n):
if updated_cells[x][i] == 2:
break
updated_cells[x][i] = -1
​
# left
for i in range(y-1,-1,-1):
if updated_cells[x][i] == 2:
break
updated_cells[x][i] = -1
​
for r in updated_cells:
counter += r.count(0)
return counter
```