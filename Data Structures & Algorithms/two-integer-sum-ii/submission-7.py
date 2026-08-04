class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(numbers) - 1
        '''
        while numbers[r] >= target and target > 0:
                r -= 1
        '''

        while l < r and not res:
            if numbers[l] + numbers[r] == target:
                res.append(l + 1)
                res.append(r + 1)
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
        
        return res
        