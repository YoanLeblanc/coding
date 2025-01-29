class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        n0 = nums[0]
        if n == 1:
            return n0
        elif n == 2:
            return max(nums)
        else:
            n1 = nums[1]
            a = n0
            if n0 >= n1:
                b = n0
                neigh = True
            else:
                b = n1
                neigh = False
            for x in nums[2:]:
                if neigh:
                    a,b = b, b+x
                    neigh = False
                else:
                    if a+x <= b:
                        neigh = True
                        a,b = b, b
                    else:
                        neigh = False
                        a,b = b, a+x
        return b