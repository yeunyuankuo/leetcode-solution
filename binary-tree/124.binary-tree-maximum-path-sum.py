# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # time: O(N)
        # space: O(N)
        maxSum = float("-inf")
        
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxSum
            
            if not node:
                return 0
            
            # compare node.val with maxSum
            maxSum = max(maxSum, node.val)
            
            # compare node.val + left with maxSum
            left = dfs(node.left)
            maxSum = max(maxSum, left + node.val)
            
            # compare node.val + right with maxSum
            right = dfs(node.right)
            maxSum = max(maxSum, right + node.val)
            
            # compare node.val + left + right with maxSum
            total = left + right + node.val
            maxSum = max(maxSum, total)
            
            # return max (node.val, node.val + left, node.val + right)
            # notice we won't compare and return node.val + left + right b/c this won't be a valid path when connected to other paths
            return max(node.val, max(left + node.val, right + node.val))
        
        dfs(root)
        return maxSum