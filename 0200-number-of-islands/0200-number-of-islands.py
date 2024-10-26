class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [ [0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0

        def bfs(visited, row, col):
            queue = deque([(row, col)]) 
            visited[row][col] = 1
            while queue:
                row, col = queue.popleft()
                directions = [(0,-1), (0,1), (1, 0), (-1,0)]
                for x,y in directions:
                    x1,y1 = row + x, col + y

                    if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and visited[x1][y1] == 0 and grid[x1][y1] == '1':
                        visited[x1][y1] = 1
                        queue.append((x1,y1))

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    res+=1
                    bfs(visited, i,j)
        return res
            