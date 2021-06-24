# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # youtube first link for solution explanation''''
        slow = head
        fast = head
        for i in range(0,n):
            fast = fast.next
            
        if fast == None:
            head = head.next
            return head
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return head
        
        # temp = head
        # def remove_rec(cur,n):
        #     temp_ = cur
        #     i = 0
        #     while i <= n-1 and temp_ != None:
        #         temp_ = temp_.next
        #         i+=1
        #     if temp_ == None and i == n:
        #         return True
        #     else:
        #         return False
        # parent_temp = None
        # while temp != None:
        #     print(temp.val,remove_rec(temp,n))
        #     if remove_rec(temp,n) and parent_temp != None:
        #         parent_temp.next = temp.next
        #         return head
        #     elif remove_rec(temp,n) and parent_temp == None:
        #         return temp.next
        #     parent_temp = temp
        #     temp = temp.next
        # return head
            
                 
        