class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product, zeros = 1, 0
        for num in nums:
            if num:
                product *= num
            else:
                zeros +=  1

        if zeros > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i, c in enumerate(nums):
            if zeros: res[i] = 0 if c else product
            else: res[i] = product // c
        return res
    
            
