class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        rows,cols = len(grid), len(grid[0])
        fresh_orange = 0 

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh_orange += 1
        
        minutes = 0 
        while queue and fresh_orange > 0:
            minutes += 1 
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x + dx , y + dy 
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_orange -= 1
                        queue.append((nx,ny))
        return minutes if fresh_orange == 0 else -1