# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, temp, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if temp is None:
            return TreeNode(val)
        if temp.val > val:
            if temp.left is not None:
                self.insertIntoBST(temp.left,val)
            else:
                temp.left = TreeNode(val)
        elif temp.val <= val:
            if temp.right is not None:
                self.insertIntoBST(temp.right,val)
            else:
                temp.right = TreeNode(val)
                
        return temp