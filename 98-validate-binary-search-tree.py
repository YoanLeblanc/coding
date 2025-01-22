class Solution:
    def minmaxbst(self, root):
        if not root:
            return 2**31, -2**31-1, True
        else:
            a1,a2,a3 = self.minmaxbst(root.left)
            b1,b2,b3 = self.minmaxbst(root.right)
            if not a3 or not b3:
                return 0,0,False
            else:
                x = root.val
                print(a1,a2,b1,b2,x)
                if a2 >= x or b1 <= x:
                    return 0,0,False
                else:
                    return min(a1,x), max(b2,x), True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.minmaxbst(root)[2]