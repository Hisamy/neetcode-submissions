class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        right = len(cleanS) - 1
        left=0

        while right > left:
            if cleanS[left] == cleanS[right]:
                left +=1
                right-=1
            else:
                return False
        
        return True


            


        