class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countChar = {}
        left = 0
        res = 0

        for right in range(len(s)):
            countChar[s[right]] = 1 + countChar.get(s[right], 0)

            if (right - left + 1) - max(countChar.values()) > k:
                countChar[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res





        



        