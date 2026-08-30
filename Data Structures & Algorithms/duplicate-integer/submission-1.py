class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}

        for i in range(len(nums)):

            if nums[i] in my_map:
                return True
            else:
                my_map[nums[i]] = i

        return False

        