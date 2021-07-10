#code
class newNode():
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
        
def inorder(temp):
    if temp == None:
        return
    inorder(temp.left)
    print(temp.val,end = " ")
    inorder(temp.right)
    
def preorder(temp):
    if temp == None:
        return
    print(temp.val,end = " ")
    inorder(temp.left)
    inorder(temp.right)
    
def postorder(temp):
    if temp == None:
        return
    inorder(temp.left)
    inorder(temp.right)
    print(temp.val,end = " ")
    
def insertion(temp,val):
    if temp is None:
        return newNode(val)
    elif temp.val > val:
        temp.left = insertion(temp.left,val)
    elif temp.val < val:
        temp.right = insertion(temp.right,val)
    return temp
    
def findMin(root):
    if root.left is None:
        # print(root.val)
        return root
    else:
        root = findMin(root.left)
    return root
        
def deletionBT(root, key):
    '''
    root: root of tree
    key:  key to be deleted
    return: root after deleting 
    https://www.youtube.com/watch?v=gcULXE7ViZw
    '''
    if root is None:
        return
    
    if key < root.val:
        print("going left from node")
        root.left = deletionBT(root.left,key)
    elif key > root.val:
        print("going right from node")
        root.right = deletionBT(root.right,key)
    else:
        print("found the node")
        if root.left is None and root.right is not None:
            print("entered first case 1a")
            temp = root.right
            del root
            return temp
        elif root.left is not None and root.right is None:
            print("entered first case 1b")
            temp = root.left
            del root
            return temp
        elif root.left is not None and root.right is not None:
            print("entered second case 2")
            min_root = findMin(root.right)
            print(min_root)
            min_root.left = root.left
            return root.right
        else:
            print("entered case 3")
            return None
    return root

if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(5)
    root.left.right = newNode(7)
    root.right = newNode(15)
    root.right.left = newNode(13)
    root.right.right = newNode(19)
    root.right.right.left = newNode(17)
    
    insertion(root,12)
    deletionBT(root,15)
    print("\n***inorder***")
    inorder(root)
    print("\n***preorder***")
    preorder(root)
    print("\n***postorder***")
    postorder(root)
    