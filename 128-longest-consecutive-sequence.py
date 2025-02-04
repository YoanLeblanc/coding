class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        if len(nums) == 0:
            return 0
        for x in nums:
            if x not in d:
                a = x
                b = x
                if x-1 in d:
                    a = d[x-1][0]
                if x+1 in d:
                    b = d[x+1][1]
                d[x] = d[a] = d[b] = (a,b)
        return max([v[1]-v[0]+1 for v in d.values()])