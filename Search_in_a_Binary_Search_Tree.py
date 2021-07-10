# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.final = None
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            print("didnt find")
            return None
        elif root.val == val:
            print("found the value",root.val)
            # return root
            self.final = root
        
        elif root.val < val:
            print("found less",root.val)
            root = root.right
            self.searchBST(root,val)
        elif root.val > val:
            print("found great",root.val)
            root = root.left
            self.searchBST(root,val)
            
        return self.final
        