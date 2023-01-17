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
        if head is None or head.next is None:
            return False
        p_s=head
        f_p=head
        while f_p and f_p.next:
            p_s=p_s.next
            f_p=f_p.next.next
            if p_s==f_p:
                return True

        return False
            