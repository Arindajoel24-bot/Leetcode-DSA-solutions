class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        length = float('inf')
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target: 
                length = min(length, (r - i) + 1)
                total -= nums[i]
                i += 1 
        if length == float('inf'):
            return 0
        return length
        
        

        
                
        
