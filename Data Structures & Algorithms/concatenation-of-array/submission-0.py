class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = nums

        result.extend(nums);

        return result
        