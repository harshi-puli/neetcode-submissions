class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1 

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1 
            else:
                a = s[l+1:r+1]
                b = s[l:r]

                return a == a[::-1] or b == b[::-1]
        
        return True