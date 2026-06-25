# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        prev=None
        while second:
            nextnode=second.next
            second.next=prev
            prev=second
            second=nextnode
        first,second=head,prev
        while first and second:
            t1=first.next
            t2=second.next
            first.next=second
            second.next=t1

            first=t1
            second=t2
        # return head

        
