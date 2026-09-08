class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def bfs(r, c) -> int:
            queue = collections.deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            queue.append((r, c))
            visited.add((r, c))
            count = 1

            while queue:
                row, col = queue.popleft()
                
                for dr, dc in directions:
                    neighbor_row = dr + row
                    neighbor_col = dc + col

                    if (0 <= neighbor_row < rows and
                        0 <= neighbor_col < cols and
                        grid[neighbor_row][neighbor_col] == 1 and
                        (neighbor_row, neighbor_col) not in visited):
                            queue.append((neighbor_row, neighbor_col))
                            visited.add((neighbor_row, neighbor_col))
                            count += 1

            return count

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(bfs(row, col), maxArea)
                    
        return maxArea




        