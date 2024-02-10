# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0

    def height(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 0
        heightL, heightR = self.height(root.left), self.height(root.right)
        if heightL < 0 or heightR < 0 or abs(heightL - heightR) > 1:
            return -1

        return max(heightL, heightR) + 1
