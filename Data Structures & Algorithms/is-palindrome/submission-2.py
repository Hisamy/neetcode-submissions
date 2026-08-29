class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS=''
        
        for i in s:
            if i.isalnum():
                cleanS += i.lower()
            else:
                continue

        right = len(cleanS) - 1
        left=0

        while right > left:
            if cleanS[left] == cleanS[right]:
                left +=1
                right-=1
            else:
                return False
        
        return True


            


        