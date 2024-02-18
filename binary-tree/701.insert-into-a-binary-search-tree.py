# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBSTRecursion(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # time: O(H), H is the tree height. O(logN) in average case, and O(N) in worst case
        # space: O(H): H is the tree heigh. O(logN) in average case, and O(N) in worst case
        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left  = self.insertIntoBST(root.left, val)
        
        return root
    
    
    def insertIntoBSTIterative(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # time: O(H), H is the tree height. O(logN) in average case, and O(N) in worst case
        # space: O(1): constant space
        node = root
        while node:
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left

        return TreeNode(val)
