class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        if len(nums) == 1 and nums[0] == target:
            res.append(nums[0])
            return res

        def backtrack(index, current_subset, total):
            if total == target:
                res.append(current_subset.copy())
                return

            if index >= len(nums) or total > target:
                return

            current_subset.append(nums[index])
            backtrack(index, current_subset, total + nums[index])

            current_subset.pop()
            backtrack(index + 1, current_subset, total)
        
        backtrack(0, [], 0)
        return res

