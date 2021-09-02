# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root = TreeNode(nums[int(len(nums)/2)])
        def treebuilder(treel):
            if len(treel) == 0:
                return None
            temp = TreeNode(treel[int(len(treel)/2)])
            left = treel[:int(len(treel)/2)]
            right = treel[int(len(treel)/2)+1:]
            
            temp.left = treebuilder(left)
            temp.right = treebuilder(right)
            
            return temp
        root.left = treebuilder(nums[:int(len(nums)/2)])
        root.right = treebuilder(nums[int(len(nums)/2)+1:])
        return root