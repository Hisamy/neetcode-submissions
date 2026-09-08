class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        countIslands = 0

        def bfs(r, c):
            queue = collections.deque()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                for directionRow, directionCol in directions:
                    neighborRow = row + directionRow
                    neighborCol = col + directionCol

                    if( 0 <= neighborRow < len(grid) and
                        0 <= neighborCol < len(grid[0]) and
                        (neighborRow,neighborCol) not in visited and
                        grid[neighborRow][neighborCol] == "1"
                        ):
                            queue.append((neighborRow, neighborCol))
                            visited.add((neighborRow, neighborCol))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    countIslands += 1
        return countIslands

        
                    

        
        