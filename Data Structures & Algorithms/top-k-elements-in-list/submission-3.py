class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq.keys():
                freq[n] += 1
            else: 
                freq[n] = 1
        

        res = sorted(freq, key=freq.get, reverse=True)
        return res[:k]