class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]

        i = 0
        while i < len(nums):
            if nums[i] < minNum:
                minNum = nums[i]
            i += 1
        
        return minNum
        
        






