class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
            
        for i in range(len(nums)):
            number_to_find = target - nums[i]

            if number_to_find in my_map:
                return [my_map.get(number_to_find), i]
                
            elif nums[i] not in my_map:
                my_map[nums[i]] = i
            

            
            


           

        