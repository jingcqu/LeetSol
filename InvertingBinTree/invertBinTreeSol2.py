# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class container:
    def __init__(self, node):
        self.val = node
        self.next = None

class queue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
    def push(self, val):
        if self.head == None:
            curr = container(val)
            self.head = curr
            self.tail = curr
        else:
            curr = container(val)
            self.tail.next = curr
            self.tail = curr
        self.length += 1
    def pop(self):
        ret = self.head.val
        self.head = self.head.next
        self.length -= 1
        return ret
    def empty(self):
        return self.length == 0

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        nodeQueue = queue()
        nodeQueue.push(root)
        while nodeQueue.empty() != True:
            curr = nodeQueue.pop()
            if(curr.left != None):
                nodeQueue.push(curr.left)
            if(curr.right != None):
                nodeQueue.push(curr.right)
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
        return root
            
            
"""

Runtime: 32 ms, faster than 56.28% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 14.1 MB, less than 5.31% of Python3 online submissions for Invert Binary Tree.

"""