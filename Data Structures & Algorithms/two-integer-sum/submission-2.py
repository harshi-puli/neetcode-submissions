class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        parts = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in parts:
                return [parts[complement], i]
            
            parts[nums[i]] = i
