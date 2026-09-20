class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = {}

        for s in strs:
            s_letters = ''.join(sorted(s))

            if s_letters in bucket.keys():
                bucket[s_letters].append(s)
            else: 
                bucket[s_letters] = [s]
        
        res = []

        for k in bucket.keys():
            res.append(bucket[k])

        return res

        