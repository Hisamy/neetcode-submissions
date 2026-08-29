class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        end = len(cleanS) - 1
        mid = len(cleanS) // 2 

        for i in range(mid):
            if cleanS[i] != cleanS[end]:
                return False
            else:
                end -= 1
                continue
        
        return True


            


        