class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        freshFruit = 0
        rottenFruit = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rottenFruit.append((r, c))
                elif grid[r][c] == 1:
                    freshFruit += 1
        
        while rottenFruit and freshFruit > 0:

            for i in range(len(rottenFruit)):
    
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                row, col = rottenFruit.popleft()

                for dr, dc in directions:
                    newRow = row + dr
                    newCol = col + dc

                    if(newRow < 0 or 
                        newCol < 0 or
                        newRow >= len(grid) or
                        newCol >= len(grid[0]) or
                        grid[newRow][newCol] != 1):
                        continue
                    grid[newRow][newCol] = 2
                    freshFruit -= 1
                    rottenFruit.append((newRow, newCol))
            minutes += 1

        return minutes if freshFruit == 0 else -1

        




        