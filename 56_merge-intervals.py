class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = itemgetter(0))
        res = [intervals[0]]
        for x in intervals[1:]:
            if res[-1][1] >= x[0]:
                if res[-1][1] < x[1]:
                    res[-1][1] = x[1]
            else:
                res.append(x)
        return res