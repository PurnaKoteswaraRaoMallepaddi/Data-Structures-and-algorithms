# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dum = []
        if head  == None or head.next == None:
            return False
        
        temp = head
        dum.append(temp)
        while temp != None:
            temp = temp.next
            
            for node in dum:
                if node is temp:
                    return True
            dum.append(temp)
        return False
        
        