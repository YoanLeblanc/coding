from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                n_i = len(words[i])
                n_j = len(words[j])
                if n_i <= n_j and words[i] == words[j][:n_i] == words[j][n_j-n_i:]:
                    res += 1
        return res