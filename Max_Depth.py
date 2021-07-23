# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        height = 0
        self.final = 0
        def MD(root,height):
            if root.right is None and root.left is None:
                if self.final < height:
                    self.final = height
                return
            
            if root.right is not None:
                MD(root.right,height+1)
            
            if root.left is not None:
                MD(root.left,height+1)
        MD(root,0)
        return self.final+1
        