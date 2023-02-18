#!/usr/bin/python3

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Two pointer approach Solution
    def reverseList(self, head: ListNode)-> ListNode:
        # T = O(n) and M = O(1)
        prev, curr = None, head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    # Recursive Approach Solution
    def reverseList(self, head: ListNode)-> ListNode:
        # Recursive: T = M = O(n)
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
