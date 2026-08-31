class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        
        stack = []

        for char in s:
            if char in parentheses:
                if not stack or stack.pop() != parentheses[char]:
                    return False    
                continue        
            else:
                stack.append(char)

        return False if len(stack) > 0 else True
