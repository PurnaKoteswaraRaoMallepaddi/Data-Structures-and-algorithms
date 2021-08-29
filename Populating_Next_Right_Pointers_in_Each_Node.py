"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        child = []
        parent = []
        parent.append(root)
        root.next = None
        while len(parent) != 0:
            for node in parent:
                if node.left is not None:
                    child.append(node.left)
                if node.right is not None:
                    child.append(node.right)
            for i,node in enumerate(child[:-1]):
                node.next = child[i+1]
            if len(child) != 0:
                child[-1].next = None
            parent = child.copy()
            child = []
        return root