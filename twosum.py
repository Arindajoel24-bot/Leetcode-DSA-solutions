class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums):
            for n, x in enumerate(nums):
                if i != n:
                    sum = v + x
                    if sum == target:
                        return i, n 