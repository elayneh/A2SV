#!/usr/bin/python3

"""
Given the head of a linked list, remove the nth node from the end of the list and return its head
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0, head)

        left = result
        right = head

        while right and n > 0:
            right = right.next
            n -= 1

        while right.next:
            left = left.next
            right = right.next

        # Delete nth node here
        left.next = left.next.next

        return result.next
