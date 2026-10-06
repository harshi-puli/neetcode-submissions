class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        targets = [s[a] for a in range(len(s))]
        i = 0

        while i < len(t):
            if not targets:
                return True
            
            print(t[i], targets)

            if t[i] == targets[0]:
                print("removing " + t[i])
                targets.remove(t[i])
            
            i += 1

        if not targets:
            return True

        return False