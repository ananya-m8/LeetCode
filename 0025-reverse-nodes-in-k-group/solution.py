# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        grp=0
        while temp!=None:
            grp+=1
            temp=temp.next
        grp//=k
        dummy=ListNode()
        dummy.next=head
        prevg=dummy
        nextg=None
        while grp>0:
            grp-=1
            kth=prevg
            for _ in range(k):
                kth=kth.next
            nextg=kth.next
            pre=nextg
            curr=prevg.next
            for _ in range(k):
                nxt=curr.next
                curr.next=pre
                pre=curr
                curr=nxt
            old_head=prevg.next
            prevg.next=kth
            prevg=old_head
        return dummy.next
