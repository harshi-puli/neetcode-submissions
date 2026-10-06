class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n):
            sub = arr[i+1:]
            print(arr)
            print(sub)
            if sub:
                arr[i] = max(sub)
            
        arr[-1] = -1
        return arr