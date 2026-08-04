class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        left = 0
        right = len(nums) - 1
        result = []

        nums.sort()
        
        while (left < right):
            curr = []
            middle = -nums[left] - nums[right]

            if middle in nums[left:right]:
                curr.append(left)
                curr.append(middle)
                curr.append(right)

                print(sum(curr))

                if curr not in result and sum(curr) == 3:
                    result.append(curr)
            
            if (min(nums[left], nums[right] == nums[left])):
                left = left + 1
            else:
                right = right - 1
            '''
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res