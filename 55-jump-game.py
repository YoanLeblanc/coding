class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        ## SOLUTION 1
        # l = [False] * n
        # l[0] = True
        # for i in range(n):
        #     if not l[i]:
        #         return False
        #     else:
        #         x = nums[i]
        #         if x + i >= n-1:
        #             return True
        #         for j in range(i, i+x+1):
        #             l[j] = True
        # return l[n-1]

        ## SOLUTION 2
        c = n-1
        for i in range(n-2, -1, -1):
            if nums[i] + i >= c:
                c = i
        return c == 0