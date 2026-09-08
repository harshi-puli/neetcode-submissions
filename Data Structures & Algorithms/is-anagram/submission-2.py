class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = list(s)
        tCount = list(t)

        sCount = sorted(sCount)
        tCount = sorted(tCount)

        return sCount == tCount
