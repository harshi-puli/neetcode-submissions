class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        res = []

        for i in range(len(nums)):
            n = nums[i]
            if n in pairs.keys():
                res.append(pairs[n])
                res.append(i)
                return res
            else:
                pairs[target - n] = i
            
    
        return res
