class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    grid, size = self.bfs(grid, row, col)
                    maxArea = max(size, maxArea)
                    
        return maxArea

    def bfs(self, grid, r, c) -> [List[List[int]], int]:
            if grid[r][c] == 0: return [grid, 0]

            grid[r][c] = 0
            count = 1

            if r - 1 > -1:
                grid, add_ = self.bfs(grid, r - 1, c)
                count += add_
            if r + 1 < len(grid):
                grid, add_ = self.bfs(grid, r + 1, c)
                count += add_
            if c - 1 > -1:
                grid, add_ = self.bfs(grid, r, c - 1)
                count += add_
            if c + 1 < len(grid[0]):
                grid, add_ = self.bfs(grid, r, c + 1)
                count += add_

            return grid, count




        