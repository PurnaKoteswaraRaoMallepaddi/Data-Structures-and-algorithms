# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        temp = head
        nums = []
        while temp is not None:
            nums.append(temp.val)
            temp = temp.next
            
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