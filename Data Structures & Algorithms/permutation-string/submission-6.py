class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : 
            return False

        count = {}
        for char in s1:
            count[char] = 1 + count.get(char, 0)
        
        left = 0
        for right in range(len(s2)):
            if s2[right] in count:
                count[s2[right]] -= 1
            if right - left + 1 > len(s1):
                if s2[left] in count:
                    count[s2[left]] += 1
                left += 1
            if right - left + 1 == len(s1) and all(value==0 for value in count.values()):
                return True

        return False
            




        