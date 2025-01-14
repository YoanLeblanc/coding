class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        def remove(t, i):
            t[i], t[-1] = t[-1], t[i]
            t.pop()
            return t

        n = len(A)
        res = [0] * n
        r_a = []
        r_b = []
        for i in range(n):
            res[i] = res[i-1]
            x = B[i]
            y = A[i]
            if x == y:
                res[i] += 1
            else:
                for j in range(len(r_a)):
                    if x == r_a[j]:
                        r_a = remove(r_a, j)
                        res[i] += 1
                        break
                else:
                    r_b.append(x)
                for j in range(len(r_b)):
                    if y == r_b[j]:
                        r_b = remove(r_b, j)
                        res[i] += 1
                        break
                else:
                    r_a.append(y)
        return res