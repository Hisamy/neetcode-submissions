class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    neigborRow = row + dr
                    neighborCol = col + dc

                    if (0 <= neigborRow < rows  and
                        0 <= neighborCol < cols and
                        grid[neigborRow][neighborCol] == "1" and
                        (neigborRow, neighborCol) not in visited
                        ):
                            queue.append((neigborRow, neighborCol))
                            visited.add((neigborRow, neighborCol))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands


        