class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        count = nums[right]
        res = len(nums) + 1
        
        while left < len(nums):
            if count >= target:
                res = min(res, right - left + 1)
                print(res)
                count -= nums[left]
                left += 1
                
            else:
                if right < len(nums) - 1:
                    right += 1
                    count += nums[right]
                else:
                    count -= nums[left]
                    left += 1
         
        return res if res != len(nums) + 1 else 0


        