# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        addresses = []

        curr = head
        while curr:
            if id(curr) in addresses:
                return True
            addresses.append(id(curr))
            curr = curr.next

        return False
