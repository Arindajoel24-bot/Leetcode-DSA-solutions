class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        results = []
        for i, v in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            L = i + 1
            R = len(sorted_nums) - 1
            while L < R:
                sum = sorted_nums[i] + sorted_nums[L] + sorted_nums[R]
                if sum == 0:
                    add = [sorted_nums[i], sorted_nums[L], sorted_nums[R]]
                    results.append(add)
                    L += 1
                    while L < R and sorted_nums[L] == sorted_nums[L-1]:
                        L += 1
                elif sum < 0:
                    L += 1
                    
                else:   
                    R -= 1

        return results   