class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [] 
        res = 0

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = height[stack.pop()]
                if not stack:
                    break
                width = i - stack[-1] - 1
                bounded = min(h, height[stack[-1]]) - bottom
                res += width * bounded
            stack.append(i)

        return res

        return res