"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        cur=head
        ow={}
        while cur:
            ow[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            copy=ow[cur]
            copy.next=ow.get(cur.next)
            copy.random=ow.get(cur.random)
            cur=cur.next
        return ow[head]
