# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prv, tmp = head, None, None

        while current:
            tmp = current.next
            current.next = prv
            prv = current
            current = tmp
        
        return prv
        