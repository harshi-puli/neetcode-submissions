class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return min(nums)

        minNum = nums[0]

        for i in range(len(nums)):
            if nums[i] < minNum:
                minNum = nums[i]
                return minNum
        return minNum


        