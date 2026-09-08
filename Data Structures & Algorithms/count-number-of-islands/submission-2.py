class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if(grid[x][y]) == "1":
                    counter = counter + 1
                    self.dfs(grid, x,y)
        
        return counter
        
    def dfs(self, grid, x, y):
        if(x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0])):
            return
        if(grid[x][y] == "0") or grid[x][y] == "X":
            return
        else:
            grid[x][y] = "X"
            self.dfs(grid, x+1, y)
            self.dfs(grid, x-1, y)
            self.dfs(grid, x, y-1)
            self.dfs(grid, x, y+1)
       


        