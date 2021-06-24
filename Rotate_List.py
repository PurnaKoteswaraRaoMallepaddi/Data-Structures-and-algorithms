# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = head
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        if count == 0 or k == 0:
            return head
        k = k%count
        start = head
        end = head
        for i in range(0,k):
            end = end.next
        
        while end.next != None:
            start = start.next
            end = end.next
            
        end.next = head
        final = start.next
        start.next = None
        return final
            
        
            
            