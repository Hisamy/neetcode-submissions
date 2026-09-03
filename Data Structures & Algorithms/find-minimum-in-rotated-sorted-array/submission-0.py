class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[3,4,5,6,1,2]
        left, right = 0, len(nums) - 1 
        minNum = max(nums)

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] < minNum:
                minNum = nums[mid]

            if nums[left] > nums[right]:
                left += 1
            else:
                right -= 1
            
        return minNum  
                


        