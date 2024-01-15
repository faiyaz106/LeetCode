# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_curr=l1
        l2_curr=l2
        rem=0 
        count=0
        while l1_curr or l2_curr:
            if l1_curr is None:
                sum_=l2_curr.val+rem
                l2_curr=l2_curr.next
            elif l2_curr is None:
                sum_=l1_curr.val+rem
                l1_curr=l1_curr.next
            else:
                sum_=l1_curr.val+l2_curr.val+rem
                l1_curr=l1_curr.next
                l2_curr=l2_curr.next
            num=sum_ - (sum_//10)*10
            rem=sum_//10
            new_node=ListNode(num)
            if count==0:
                head=ListNode(num)
                curr_node=head
                count=count+1
            else:
                curr_node.next=ListNode(num)
                curr_node=curr_node.next
            
            
        if rem>0:
            curr_node.next=ListNode(rem)
        return head
            
             
                
            
            