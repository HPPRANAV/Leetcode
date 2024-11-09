def dfs(grid1, grid2, visited, i, j):
    rows = len(grid2)
    cols = len(grid2[0])
    stack = [(i,j)]
    directions = [(-1,0), (0,-1), (1,0), (0,1)]
    visited.add((i,j))
    is_sub = True

    while stack:
        a,b = stack.pop()
        if grid2[a][b] == 1 and grid1[a][b]!= 1:
            is_sub = False
        
        for x, y in directions:
            x1, y1 = x + a, y + b
            
            if x1 < 0 or y1 < 0 or x1 >= rows or y1 >= cols or grid2[x1][y1] == 0 or (x1, y1) in visited:
                continue  
            
            stack.append((x1, y1))
            visited.add((x1, y1))
    
    return is_sub


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        count = 0
        rows = len(grid2)
        cols = len(grid2[0])

        for i in range(rows):
            for j in range(cols):
                if( grid2[i][j] == 1 and (i,j) not in visited):
                    val = dfs(grid1, grid2, visited, i, j)
                    if val:
                        count+=1
        return count
        
        