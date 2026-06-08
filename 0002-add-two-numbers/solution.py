# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify handling the result list
        dummy = ListNode()
        # Pointer to the current node in the result list
        temp = dummy  
        # Carry from the previous digit addition
        carry = 0     

        # Loop until both lists are fully traversed and no carry remains
        while (l1 is not None or l2 is not None) or carry:
            sum_val = 0  # Holds the sum of current digits and carry

            # Add l1's value to sum if l1 exists
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next

            # Add l2's value to sum if l2 exists
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next

            # Add any carry from the previous step
            sum_val += carry

            # Update carry for the next addition
            carry = sum_val // 10

            # Create a new node with the digit value (sum % 10)
            node = ListNode(sum_val % 10)
            # Append the new node to the result list
            temp.next = node  
            # Move temp forward
            temp = temp.next  

        # Return the result list, skipping the dummy node
        return dummy.next
