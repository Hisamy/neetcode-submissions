class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        self.helper(0, 0, n, cur, res)
        return res
    
    def helper(self, left, right, n, cur, res):
        if left == n and right == n:
            res.append("".join(cur))
            return
        
        if left < n:
            cur.append('(')
            self.helper(left + 1, right, n, cur, res)
            cur.pop()
        
        if right < left:
            cur.append(')')
            self.helper(left, right + 1, n, cur, res)
            cur.pop()
    
        
        