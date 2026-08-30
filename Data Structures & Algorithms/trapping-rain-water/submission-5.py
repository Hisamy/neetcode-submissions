class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRigth = height[l], height[r]
        total = 0

        while l < r:
            if maxLeft <= maxRigth: 
                l += 1 
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r -= 1 
                maxRigth = max(maxRigth, height[r])
                total += maxRigth - height[r]

        return total



       
            


            


        