#!/usr/bin/python3
"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

# class ListNode:
#     def __init__(self, val =0, next = None) -> None:
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        curr = node

        carry = 0
        while l1 or l2 or carry:
            curr.val += l1.val if l1 else 0
            curr.val += l2.val if l2 else 0
            carry = curr.val // 10

            curr.val %= 10
            # result

            # Update current pointer to point to the next node.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 or l2 or carry:
                curr.next = ListNode(carry)
                curr = curr.next
        return node

