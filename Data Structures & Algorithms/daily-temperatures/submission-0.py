class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*(len(temperatures))
        temp_stack = []

        for i, temp in enumerate(temperatures):
            if temp_stack == []:
                temp_stack.append([temp, i])
                continue

            while temp_stack != [] and temp > temp_stack[-1][0]:
                result[temp_stack[-1][1]] = i - temp_stack[-1][1]
                temp_stack.pop()
            
            temp_stack.append([temp, i])
        
        return result
        