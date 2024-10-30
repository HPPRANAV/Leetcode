class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time,fresh = 0, 0
        row, col = len(grid), len(grid[0])
        queue = deque()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    queue.append((i,j))

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue and fresh > 0:

            for i in range(len(queue)):
                a,b = queue.popleft()
                for x,y in directions:
                    x1,y1 = a+x, b+y
                    if(x1 < 0 or x1 == row or y1 < 0 or y1 == col or grid[x1][y1]!=1):
                        continue
                    grid[x1][y1] = 2
                    queue.append((x1, y1))
                    fresh-=1
            time+=1
        if fresh == 0:
            return time
        return -1

        