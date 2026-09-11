# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root.val == subRoot.val:
            return self.isSubTree(root.left, subRoot.left) and self.isSubTree(root.right, subRoot.right)

        return False
        