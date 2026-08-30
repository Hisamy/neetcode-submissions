class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0 

        while l < r:
            maxArea = max(maxArea, (r - l) * min(heights[l], heights[r]))
             
            if heights[l] < heights[r]:
                hToBeat = heights[l]
                while heights[l] <= hToBeat and l < r:
                    l += 1
                
            else: 
                hToBeat = heights[r]
                while heights[r] <= hToBeat and l < r:
                    r -= 1
        
        return maxArea
            
             

        
        