class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        i = 0
        maxArea = 0 
        

        while l < r:
            width = len(heights) - 1 - i 
            height = min(heights[l], heights[r])
            area = width * height

            if area > maxArea:
                maxArea = area
            if heights[l] <= heights[r]:
                l += 1
                i += 1
            else: 
                r -= 1
                i += 1
        
        return maxArea
            
             

        
        