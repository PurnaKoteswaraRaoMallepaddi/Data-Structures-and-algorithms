# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.final = []
        def inorder(root):
            if root is None:
                return

            inorder(root.left)
            self.final.append(root)
            inorder(root.right)
            return
        
        inorder(root)
        temp_list = [temp.val for temp in self.final]
        temp_list.sort()
        for i in range(0,len(self.final)):
            if self.final[i].val != temp_list[i]:
                print("changing the values",self.final[i].val,temp_list[i])
                self.final[i].val = temp_list[i]
        return root
            
        