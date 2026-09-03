class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 
        res = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                return min(nums[left], res)

            m = (left + right) // 2
            res = min(res,nums[m])

            if nums[m] < nums[right]:
                right = m - 1 
            else:
                left = m + 1
        return res
                


        