class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        mid = low + (high - low) // 2

        if (nums[low] <= nums[mid]) and (target >= nums[low] and target <= nums[mid]):
            high = mid

        elif nums[low] <= nums[mid] or (target >= nums[mid] and target <= nums[high]):
            low = mid
        else:
            high = mid

        
        while low <= high:
            if nums[low] == target:
                return low 
            low += 1

        return -1

        