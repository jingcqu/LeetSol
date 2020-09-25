# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root
                

"""
Runtime: 28 ms, faster than 79.93% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14 MB, less than 10.44% of Python3 online submissions for Invert Binary Tree.

"""