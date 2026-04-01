class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] != "1":
                return 
            else:
                grid[r][c] = "0"
                dfs(r + 1, c)
                dfs(r - 1, c) 
                dfs(r, c + 1)
                dfs(r, c - 1)
            
    
        island = 0 
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island += 1
                    dfs(row,col)
        return island