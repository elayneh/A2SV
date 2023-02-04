#!/usr/bin/python3
"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the secodnd middle node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastPtr = slowPtr = head
        while slowPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        return slowPtr
