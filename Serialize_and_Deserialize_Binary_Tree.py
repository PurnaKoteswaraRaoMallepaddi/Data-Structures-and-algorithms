# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://www.youtube.com/watch?v=u4JAi2JJhI8

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.final = []
        def preorder(root):
            if root is None:
                self.final.append('N')
                return
            self.final.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(self.final)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = 0
        self.vals = data.split(',')
        print(self.vals)
        def dfs(): 
            if self.vals[self.i] =='N':
                self.i += 1
                return None
            node = TreeNode(self.vals[self.i])
            self.i += 1 #we only update it here because only here we are using the value from list
            node.left = dfs()
            node.right = dfs() #no parameters because we are using a pointer to locate the value
            return node # as this is returning the node no need to use a self.final
        root = dfs()
        return root
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))