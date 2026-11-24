class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        elems = set()

        for num in nums:
            if num not in elems:
                elems.add(num)
            else:
                return num
        