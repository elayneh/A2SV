#!/usr/bin/python3

"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
Given a pointer to the head of a linked list, determine if it contains a cycle.
If it does, return . Otherwise, return .
"""
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow = fast = head

    # Bussiness logic
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        # check if these two pointers point the same node
        if fast == slow:
            return True

    return False

if __name__ == "__main__":
    ...

