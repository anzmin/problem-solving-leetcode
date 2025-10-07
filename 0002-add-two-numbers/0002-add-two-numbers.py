# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        a, b, carry = l1, l2, 0

        curr_node = dummy_node
        while a != None or b != None:
            s = carry

            if a != None:
                s += a.val
                a = a.next
            if b != None:
                s += b.val
                b = b.next
                
            if s >= 10:
                carry = 1
                s -= 10
            else:
                carry = 0

            curr_node.next = ListNode(s)
            curr_node = curr_node.next
        
        if carry == 1:
            curr_node.next = ListNode(1)
        
        return dummy_node.next
        
            