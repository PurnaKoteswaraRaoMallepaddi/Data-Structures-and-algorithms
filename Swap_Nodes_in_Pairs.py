# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        if head == None:
            return head
        else:
            second = head.next
        parent = None
        
        while first != None and second != None:
            first.next = second.next
            second.next = first
            
            if first == head:
                head = second
            if parent != None:
                parent.next = second   
            parent = first
            
            if first != None and first.next != None:
                first = first.next
            else:
                first = None
                
            if first != None and first.next != None:
                second = first.next
            else:
                second = None
        return head
        
#         first = head
#         if head == None:
#             return head
#         else:
#             second = head.next
#         parent = None
#         while first != None and second != None:
#             temp = first.val
#             first.val = second.val
#             second.val = temp
            
#             if second.next != None:
#                 first = second.next
#             else:
#                 first = None
            
#             if first != None and first.next != None:
#                 second = first.next
#             else:
#                 second = None
            
        
        # return head