class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for s in strs:
            curr = "".join(sorted(list(s)))
            if curr in tracker.keys():
                tracker[curr].append(s)
            else:
                tracker[curr] = [s]
        
            
        res = [tracker[key] for key in tracker.keys()]
        
        return res