# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root, subRoot):
        if not root:
            if not subRoot:
                return True
            else:
                return False
        elif not subRoot:
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        reste = []
        a = root
        while root or len(reste) != 0:
            if not root:
                root = reste.pop()
            else:
                if self.check(root, subRoot):
                    return True
                
                if root.left:
                    reste.append(root.left)
                root = root.right
        return False