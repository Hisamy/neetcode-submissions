class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        res = []
        dictionary = {
            2 : ["a", "b", "c"],
            3 : ["d", "e", "f"],
            4 : ["g", "h", "i"],
            5 : ["j", "k", "l"],
            6 : ["m", "n", "o"],
            7 : ["p", "q", "r", "s"],
            8 : ["t", "u", "v"],
            9 : ["w", "x", "y", "z"],
            }
        matrix = [dictionary.get(int(digit), []) for digit in digits]

        def backtrack(index, combination):
            if index == len(digits):
                string = "".join(combination)
                res.append(string)
                return 
            
            for letra in matrix[index]:
                combination.append(letra)
                backtrack(index + 1, combination)
                combination.pop()
            
        backtrack(0, [])
        return res


        
        