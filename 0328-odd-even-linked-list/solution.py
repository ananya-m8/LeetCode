# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        evenh=event=None
        oddh=oddt=None
        cur=head
        pos=0
        while(cur!=None):
            if(pos%2!=0):
                if(evenh==None):
                    evenh=event=cur
                else:
                    event.next=cur
                    event=cur
            else:
                if(oddh==None):
                    oddh=oddt=cur
                else:
                    oddt.next=cur
                    oddt=cur
            cur=cur.next
            pos+=1
        if not oddh:
            return evenh
        elif not evenh:
            return oddh
        oddt.next=evenh
        event.next=None
        return oddh


