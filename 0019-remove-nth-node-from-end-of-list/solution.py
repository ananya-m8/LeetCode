# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        temp=head
        while(temp!=None):
            l+=1
            temp=temp.next
        temp=head
        pre=None
        while(temp!=None and n!=l):
            pre=temp
            temp=temp.next
            l-=1
        if(pre!=None):
            pre.next=temp.next
        else:
            head=temp.next
        return head
