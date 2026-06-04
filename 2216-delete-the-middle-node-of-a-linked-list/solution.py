# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        pre=None
        while(fast!=None and fast.next!=None):
            pre=slow
            slow =slow.next
            fast=fast.next.next
        if(pre!=None):
            pre.next =slow.next
        else:
            head=None
        return head
