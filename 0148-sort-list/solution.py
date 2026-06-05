# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findMiddle(self,head):
        if not head and not head.next:
            return head
        slow=head
        fast=head.next
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow
    def merge(self,left,right):
        d=ListNode(-1)
        temp=d
        while(left and right):
            if left.val<=right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next
        if left:
            temp.next=left
        else:
            temp.next=right
        return d.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head
        middle=self.findMiddle(head)
        right=middle.next
        middle.next=None
        left=head
        left=self.sortList(left)
        right=self.sortList(right)
        return self.merge(left,right)
