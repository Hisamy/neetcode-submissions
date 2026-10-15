class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes, freshFruit = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        rottenFruits = deque()

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    freshFruit += 1
                elif grid[row][col] == 2:
                    rottenFruits.append([row, col])

        while rottenFruits and freshFruit > 0:
            for rotten in range(len(rottenFruits)):
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                r, c = rottenFruits.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row < 0 or col < 0 or
                        row >= ROWS or col >= COLS or
                        grid[row][col] != 1):
                        continue

                    freshFruit -= 1
                    rottenFruits.append([row, col])
                    grid[row][col] = 2

            minutes += 1
            
        return minutes if freshFruit == 0 else -1
                
        