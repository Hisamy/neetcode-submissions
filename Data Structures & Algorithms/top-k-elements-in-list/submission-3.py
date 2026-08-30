class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for number, c in count.items():
            freq[c].append(number)
   
            
        for n in range(len(freq) - 1, 0, -1):
            for i in freq[n]:
                res.append(i)
                if len(res) == k:
                    return res
        return res

        