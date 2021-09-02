# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.final = []
        self.parent = []
        self.child = []
        self.parent = [root]
        reverse = False
        while len(self.parent) != 0:
            if not reverse:
                self.final.append([node.val for node in self.parent])
                reverse = True
            else:
                reverse = False
                self.final.append([node.val for node in self.parent[::-1]])
            for node in self.parent:
                if node.left is not None:
                    self.child.append(node.left)
                if node.right is not None:
                    self.child.append(node.right)
            self.parent = self.child.copy()
            self.child = []
        print(self.final)
        return self.final
            
                
            
            