from collections import defaultdict
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        l1 = []
        for x in words1:
            d = defaultdict(int)
            for y in x:
                d[y] += 1
            l1.append(d)
        l2 = [0] * 26
        for x in words2:
            d = defaultdict(int)
            for y in x:
                d[y] += 1
            for z in d:
                i = ord(z) - ord("a")
                l2[i] = max(l2[i], d[z])
        
        res = []
        i =0
        for x in l1:
            if all([x[alpha[i]] >= l2[i] for i in range(26)]):
                res.append(words1[i])
            i += 1
        return res

