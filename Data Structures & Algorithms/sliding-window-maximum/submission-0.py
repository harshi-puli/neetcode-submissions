class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []

        while r <= len(nums) -1:
            curr = nums[l: r + 1]

            res.append(max(curr))
            
            l += 1
            r += 1
        
        return res
