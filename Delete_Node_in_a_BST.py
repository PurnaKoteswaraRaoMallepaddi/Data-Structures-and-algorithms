# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMin(self, root):
        if root.left is None:
            # print(root.val)
            return root
        else:
            root = self.findMin(root.left)
        return root
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        https://www.youtube.com/watch?v=gcULXE7ViZw
        """
        if root is None:
            return

        if key < root.val:
            # print("going left from node")
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            # print("going right from node")
            root.right = self.deleteNode(root.right,key)
        else:
            # print("found the node")
            if root.left is None and root.right is not None:
                # print("entered first case 1a")
                temp = root.right
                del root
                return temp
            elif root.left is not None and root.right is None:
                # print("entered first case 1b")
                temp = root.left
                del root
                return temp
            elif root.left is not None and root.right is not None:
                # print("entered second case 2")
                min_root = self.findMin(root.right)
                # print(min_root)
                min_root.left = root.left
                return root.right
            else:
                print("entered case 3")
                return None
        return root

        
