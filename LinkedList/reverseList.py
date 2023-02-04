#!/usr/bin/python3

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Two pointer approach Solution
    def reverseList(self, head: Optional[ListNode])-> Optional[ListNode]:
        # T = O(n) and M = O(1)
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    # Recursive Approach Solution
    def reverseList(self, head: Optional[ListNode])-> Optional[ListNode]:
        # Recursive: T = M = O(n)
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
