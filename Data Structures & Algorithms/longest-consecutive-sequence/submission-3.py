class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        sequence = set()
        count = 1
        nums.sort()
        for i in range(len(nums)):
            next = i + 1
            if(next < len(nums)):
                if(nums[next] == nums[i]):
                    continue
                elif nums[next] - nums[i] == 1:
                    count += 1
                else:
                    sequence.add(count)
                    count = 1
            else:
                sequence.add(count)
        return max(sequence)