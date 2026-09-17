class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * temperatures 
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([i, t])
        return res

            

