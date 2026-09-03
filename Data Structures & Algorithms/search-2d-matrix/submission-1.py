class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        top, bottom = 0, m - 1

        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            elif target >= matrix[mid][0] and target <= matrix[mid][-1]:
                for i in range(n):
                    if target == matrix[mid][i]:
                        return True
                return False 

        return False   

        