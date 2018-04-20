# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left),maxDepth(root.right))