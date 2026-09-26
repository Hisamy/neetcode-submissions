class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(index, substring):
            if index == len(s):
                res.append(substring[:])
                return
            
            for end in range(index + 1, len(s) + 1):
                if isPalindrome(s[index : end]):
                    substring.append(s[index : end])
                    backtrack(end, substring)
                    substring.pop()

        backtrack(0, [])
        return res

        