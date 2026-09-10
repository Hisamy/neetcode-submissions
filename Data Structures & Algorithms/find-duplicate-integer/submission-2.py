class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 1

        while not nums[slow] == nums[fast]:
            if fast == len(nums) - 1:
                fast = 0
            elif slow == len(nums) - 1:
                slow = 0
                fast += 1
            elif nums[slow] == nums[fast]:
                return nums[slow]
            else:
                fast += 1
                slow += 1
            
        return nums[slow]

        