# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        curr = head
        prev = None
        # nex = head.next
        
        while curr != None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            
        return prev
        
        
        
#         if head == None or head.next == None:  # this has a space complexity of O(n) but the above soution is just pointer manipulation
#             return head
#         temp = head
#         dummy = []
#         while temp != None:
#             dummy.append(temp)
#             temp = temp.next
#         final_head = dummy[-1]
#         temp = final_head
#         for node in reversed(dummy[:-1]):
#             temp.next = node
#             temp = temp.next
#         temp.next = None
            
        # return final_head