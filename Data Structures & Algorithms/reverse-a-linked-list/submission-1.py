# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next #next node saved before overwritten
            curr.next = prev #the current next node now points to the previous, bc it is overwritten

            # this part is used to move the pointers forward
            prev = curr #prev node moves up to the current node
            curr = next_node #the current node is now the next node
        return prev