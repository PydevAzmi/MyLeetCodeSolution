class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        counter = 0
        #updated_cells = [[1 if ([r,c] in walls or [r,c] in guards) else 0  for c in range(n)] for r in range(m)]

        updated_cells = [[0] * n for _ in range(m)]
        
       
        for x, y in guards:  
            updated_cells[x][y] = 1    
        for x, y in walls:
            updated_cells[x][y] = 1
            
        dirs = [(-1, 0),(0,-1),(1,0),(0,1)]
        for gx, gy in guards:
            for dx, dy in dirs: 
                x, y = gx, gy
                while True:
                    x += dx
                    y += dy
                    if x < 0 or x >= m or y < 0 or y >= n or updated_cells[x][y] == 1:
                        break
                    updated_cells[x][y] = -1
        for r in updated_cells:
            counter += r.count(0)
        return counter