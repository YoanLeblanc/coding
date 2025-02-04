class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_l = 0
        n = len(s)
        current_s = ""
        current_l = 0
        a = 0
        b = 0
        while b < n:
            for i in range(a,b):
                if s[i] == s[b]:
                    a = i+1
                    current_l = b-a+1
                    current_s = current_s[i-a:]
                    break
            else:
                current_l += 1
                current_s += s[b]
                if current_l > max_l:
                    max_l = current_l
            b += 1
        return max_l