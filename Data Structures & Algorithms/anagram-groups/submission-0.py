class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            my_map[key].append(i)
        
        return list(my_map.values())
        