class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda p: p[0])
        res = [intervals[0]]
        r = 0

        for i in range(1,len(intervals)):
            if res[r][1] >= intervals[i][0]:
                if intervals[i][1] >= res[r][1]:
                    res[r] = [res[r][0], intervals[i][1]]
            else:
                res.append(intervals[i])
                r += 1

        return res