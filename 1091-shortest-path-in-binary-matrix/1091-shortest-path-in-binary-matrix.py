class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if grid[0][0] != 0:
            return -1
        visited = set()   #IMPORTANT: Using Set instead of List because searching in python set takes O(1) where as searching in python lists take O(n)
        queue = collections.deque()
        queue.append([0,0,1]) #Add 0,0 of the grid with depth 1 to queue
        N = len(grid) #N to check for bounds and end case
        while queue:
            [r,c,depth] = queue.popleft()
            if r == N-1 and c == N-1:  #If we are at the target location, return depth
                return depth
            for [nr,nc] in [[r-1,c-1],[r-1,c],[r-1,c+1],[r,c-1],[r,c+1],[r+1,c-1],[r+1,c],[r+1,c+1]]:
                if ((nr,nc) not in visited) and (0 <= nr < N) and (0 <= nc < N) and (grid[nr][nc] == 0):
                    visited.add((nr,nc))
                    queue.append([nr,nc,depth+1])
        return -1


                    
                
                