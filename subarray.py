class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        large = float('-inf')
        current_max = 0
        for num in nums:
            current_max = max(num, current_max + num)
            large = max(large, num, current_max)
        return large