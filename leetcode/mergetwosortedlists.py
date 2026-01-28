# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans = None
        if not list1 and not list2:
            return None
        elif not list2:
            return list1
        elif not list1:
            return list2
        
        if list1.val > list2.val:
            ans = ListNode(list2.val)
            list2 = list2.next
        else:
            ans = ListNode(list1.val)
            list1 = list1.next
        
        pivot = ans
        while list1 and list2:
            if list1.val > list2.val:
                pivot.next = list2
                list2 = list2.next
                pivot = pivot.next
            else:
                pivot.next = list1
                list1 = list1.next
                pivot = pivot.next
        if list1:
            while list1:
                pivot.next = list1
                list1 = list1.next
                pivot = pivot.next
        elif list2:
            while list2:
                pivot.next = list2
                list2 = list2.next
                pivot = pivot.next
        return ans