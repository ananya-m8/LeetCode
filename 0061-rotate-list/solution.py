# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        n=0
        temp=head
        while(temp!=None):
            n+=1
            temp=temp.next
        if k>=n:
            k%=n
        if k==0:
            return head
        c=n-k
        beg=head
        ore=None
        for _ in range(c):
            pre=beg
            beg=beg.next
        end=beg
        while(end.next!=None):
            end=end.next
        end.next=head
        pre.next=None
        temp=beg
        while(temp!=None):
            temp=temp.next
        return beg

