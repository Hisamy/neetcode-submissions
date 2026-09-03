class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            l, r = 0, len(matrix[mid]) - 1
            
            if target > matrix[mid][r]:
                left += 1
            elif target < matrix[mid][l]:
                right -= 1
            else:
                while l <= r:
                    m = l + (r - l) // 2
                    if target == matrix[mid][m]:
                        return True
                    elif target > matrix[mid][m]:
                        l += 1
                    else:
                        r -= 1
                return False 

        return False   

        