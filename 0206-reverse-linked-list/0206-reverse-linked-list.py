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
        prev_ptr=None
        next_ptr=head
        while next_ptr:
            temp=next_ptr.next
            next_ptr.next=prev_ptr
            prev_ptr=next_ptr
            next_ptr=temp
        return prev_ptr

 

