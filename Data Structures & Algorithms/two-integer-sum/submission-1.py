class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in passed:
                return [passed[diff], index]
            
            passed[num] = index