class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        elif nums[0] == target:
            return 0
        elif nums[-1] == target:
            return n-1
        elif n <= 2:
            return -1
        elif n == 3:
            if nums[1] == target:
                return 1
            else:
                return -1
        else:
            a = 0
            b = n - 1
            x = nums[a]
            y = nums[b]
            if x > y:
                while b-a>1:
                    i = int((b+a)/2)
                    z = nums[i]
                    if z > x:
                        a = i
                        x = nums[a]
                    else:
                        b = i
                        y = nums[b]
                a,b = b,a
                x,y=y,x
            if target < x:
                return -1
            elif target > y:
                return -1
            elif target == x:
                return a
            elif target == y:
                return b
            else:
                if target > nums[0]:
                    a = 0
                elif target < nums[-1]:
                    b = n - 1 
                while b-a > 1:
                    x = nums[a]
                    y = nums[b]
                    i = int((b+a)/2)
                    z = nums[i]
                    if z == target:
                        return i
                    elif z < target:
                        a = i
                    else:
                        b = i
                return -1