# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.max_depth = 0
        return self.in_order(root)
        
    def in_order(self, root):
        if root is None:
            return 0

        self.depth += 1

        # First recur on left subtree
        self.in_order(root.left)
        if self.max_depth < self.depth:
            self.my_dict = {}
            self.my_dict[root.val] = self.depth
            self.max_depth = self.depth
            
        # Then recur on right subtree
        self.in_order(root.right)
        self.depth -= 1 

        return max(self.my_dict)
    