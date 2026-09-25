class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        visited = set()

        def backtracking(index, row, col):
            if index == len(word):
                return True
            if (row < 0 or row >= ROW or
                col < 0 or col >= COL or
                word[index] !=  board[row][col] or
                (row,col) in visited):
                return False
            
            visited.add((row, col))

            res = (backtracking(index + 1, row + 1, col) or
                    backtracking(index + 1, row - 1, col) or
                    backtracking(index + 1, row, col + 1) or
                    backtracking(index + 1, row, col - 1))
            visited.remove((row, col))
            return res
        
        for r in range(ROW):
            for c in range(COL):
                if backtracking(0, r, c):
                    return True
            
        return False

            

        


        
        
        
        