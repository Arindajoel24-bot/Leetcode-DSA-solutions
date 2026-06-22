
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for i, n in enumerate(temperatures):
            for j in range(i + 1, len(temperatures)):
                if n < temperatures[j]:
                    answer.append(j - i)
                    break
            else:
                answer.append(0)
        return answer
            