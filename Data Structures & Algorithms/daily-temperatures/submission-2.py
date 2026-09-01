class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (index - stackI)
            stack.append([temperature, index])
        return res
                    

        



        