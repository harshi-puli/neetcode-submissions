class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = min(heights[i], heights[j]) * (j - i)

        while (i < j):
            if (min(heights[i], heights[j]) == heights[i]): 
                i = i + 1
            else:
                j = j - 1
            
            area = min(heights[i], heights[j]) * (j - i)
            print(area)

            maxArea = max(maxArea, area)

        return maxArea


        
        