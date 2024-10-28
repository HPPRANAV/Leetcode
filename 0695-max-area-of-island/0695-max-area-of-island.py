

def bfs(x, y, graph):
    queue = deque([(x, y)])
    count = 1 
    graph[x][y] = 0 
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        a, b = queue.popleft()
        
        for dr, dy in directions:
            x1, y1 = a + dr, b + dy
            if 0 <= x1 < len(graph) and 0 <= y1 < len(graph[0]) and graph[x1][y1] == 1:
                queue.append((x1, y1))
                graph[x1][y1] = 0 
                count += 1 
                
    return count

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j, grid))
        return res
