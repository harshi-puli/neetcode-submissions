class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half = int(len(nums)/3)
        majority = (0,0)

        count = Counter(nums)

        for key in count.keys():
            if count[key] >= half and count[key] > majority[1]:
                majority = (key, count[key])

        return majority[0]
    