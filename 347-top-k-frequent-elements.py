class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for x in nums:
            d[x] += 1
        d = sorted(d.items(), key=lambda x: x[1], reverse = True)[:k]
        return [x for x,y in d]