class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        sAnagram = {}
        tAnagram = {}
        for i in range(len(s)):
            sAnagram[s[i]] = 1 + sAnagram.get(s[i], 0)  
            tAnagram[t[i]] = 1 + tAnagram.get(t[i], 0) 
        for c in sAnagram: 
            if sAnagram[c] != tAnagram.get(c,0):
                return False
        return True
        