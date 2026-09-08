class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, fresh = 0, 0
        q = deque()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    neighbor_dr = r + dr
                    neighbor_dc = c + dc

                    if (0 <= neighbor_dr < len(grid) and
                        0 <= neighbor_dc < len(grid[0]) and
                        grid[neighbor_dr][neighbor_dc] == 1 
                        ):
                            grid[neighbor_dr][neighbor_dc] = 2
                            q.append((neighbor_dr, neighbor_dc))
                            fresh -= 1
            time += 1
                    
        return time if fresh == 0 else -1



            

                
                
                





    
        