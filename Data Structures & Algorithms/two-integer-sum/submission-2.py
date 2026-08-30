class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i, a in enumerate(nums):
            find = target - a
            if find in my_map:
                return [my_map.get(find), i]
            
            my_map[a] = i
        return []

        