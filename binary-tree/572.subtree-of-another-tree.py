# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, t: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        if not t and not s:
            return True
        elif t and s and t.val == s.val:
            return self.isSameTree(t.left, s.left) and self.isSameTree(t.right, s.right)
        else:
            return False
