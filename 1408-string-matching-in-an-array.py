from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        res = []
        for i in range(n):
            x = words[i]
            for j in range(n):
                if x in words[j] and i != j:
                    res.append(x)
                    break
        return res