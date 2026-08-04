class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        need = {}

        for s in s1:
            need[s] = 1 + need.get(s, 0)

        while r <= len(s2) - 1:
            have = {}
            curr = s2[l:r+1]

            for c in curr:
                have[c] = 1 + have.get(c, 0)
            
            if have == need:
                return True

            l += 1
            r += 1
        
        return False
