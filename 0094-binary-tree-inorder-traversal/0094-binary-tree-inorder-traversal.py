# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        1. Go left and perform inorder travrsal
        2. Perform an action to the current node (add to empty list)
        3. Go right and perform inorder traversal
        """
        return self.inorderTraversal(root.left) + [root.val] +self.inorderTraversal(root.right) if root else []