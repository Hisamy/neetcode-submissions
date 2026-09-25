class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(clo, ope, string):
            if clo == ope == n:
                res.append(string)
                return  
            if ope <= n:
                backtrack(clo, ope + 1, string + "(")
            if clo < ope:
                backtrack(clo + 1, ope, string + ")")
            

        backtrack(0, 0, "")
        return res 
        