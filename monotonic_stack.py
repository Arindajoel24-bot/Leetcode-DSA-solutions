class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i, n in enumerate(temperatures):
            while not stack == [] and temperatures[i] > temperatures[stack[-1]]:
                j = stack[-1]
                answer[j] = i - j
                stack.pop()
            stack.append(i)
        
        return answer    
            