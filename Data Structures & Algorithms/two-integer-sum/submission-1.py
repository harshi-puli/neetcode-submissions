class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        result = []

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in counter:
                result.append(counter[difference])
                result.append(i)

            counter[nums[i]] = i

        return result