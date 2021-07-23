# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        # self.once = False
        self.same = False
        # self.temp = []
        def baapInorder(root):
            temp = []
            def inorder(root):
                if root is None:
                    temp.append('N')
                    return

                inorder(root.left)
                temp.append(str(root.val))
                inorder(root.right)
            inorder(root)
            return temp
              
        def search(root,val):
            if root is None:
                return
            
            if root.val == val:
                # self.once = True
                
                if baapInorder(root) == baapInorder(subRoot):
                    self.same = True
                    
            search(root.left,val)
            search(root.right,val)
            
        search(root,subRoot.val)
        return self.same
                