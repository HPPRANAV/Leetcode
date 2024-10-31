class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0,0
        queue = deque([])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j)) 

        directions = [(0,-1), (-1,0),(1,0), (0,1)]
        while queue and fresh > 0:
            for i in range(len(queue)):
                a,b = queue.popleft()
                for x,y in directions:
                    x1,y1 = a + x, b + y
                    if (x1 == rows or y1 == cols or x1 < 0 or y1 < 0 or grid[x1][y1]!=1):
                        continue
                    queue.append((x1,y1))
                    grid[x1][y1] = 2
                    fresh-=1
            time+=1
        
        return time if fresh == 0 else -1
