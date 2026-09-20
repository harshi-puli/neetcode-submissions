class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        res = []
        while k > 0:
            most_freq = max(freq, key = freq.get)
            res.append(most_freq)

            freq.pop(most_freq)
            k -= 1
        
        return res