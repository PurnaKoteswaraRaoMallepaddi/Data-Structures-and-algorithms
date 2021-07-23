# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.check = True
        def ST(root1,root2):
            if root1 is None and root2 is None:
                return
            
            if root1 is not None and root2 is not None and root1.val == root2.val:
                ST(root1.left,root2.left)
                ST(root1.right,root2.right)
            else:
                self.check = False
        ST(p,q)
        return self.check
        