# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = { v:i for i,v in enumerate(inorder) }
        
        def dfs(l, r):
            if l > r:
                return None
            node = TreeNode(postorder.pop())
            i = inorderIdx[node.val]
            node.right = dfs(i+1, r)
            node.left = dfs(l, i-1)
            return node
        
        return dfs(0, len(inorder)-1)