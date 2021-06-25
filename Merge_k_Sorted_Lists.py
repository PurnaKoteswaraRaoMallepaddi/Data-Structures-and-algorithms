# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dumm = []
        if len(lists) == 0:
            return None
        for list_ in lists:
            temp = list_
            while temp != None:
                dumm.append(temp.val)
                temp = temp.next
        dumm.sort()
        if len(dumm) == 0:
            return None
        
        temp = ListNode()
        head = temp
        head.val = dumm[0]
        for val in dumm[1:]:
            temp1 = ListNode()
            temp1.val = val
            temp.next = temp1
            temp = temp.next
        return head