class Solution:
    def search(self, nums: List[int], target: int) -> int:
        curr = -1

        for i in range(len(nums)):
            if nums[i] == target:
                curr = i

        return curr