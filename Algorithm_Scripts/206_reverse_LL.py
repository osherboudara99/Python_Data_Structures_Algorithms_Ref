# https://leetcode.com/problems/reverse-linked-list/description/
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

from typing import Optional


class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next
def print_list(head:Optional[LinkedListNode]):
    tmp = head

    while tmp:
        print(tmp.val, end=' ')
        tmp = tmp.next
    print()


def reverse_LL(head:Optional[LinkedListNode]) -> Optional[LinkedListNode]:
    before = None 
    tmp = head 

    while tmp:
        after = tmp.next 
        tmp.next = before 
        before = tmp 
        tmp = after 
    return before
    
head = LinkedListNode(1)
head.next = LinkedListNode(2)
head.next.next = LinkedListNode(3)
head.next.next.next = LinkedListNode(4)


print_list(head)

head = reverse_LL(head)

print_list(head)

# Iterative Approach:
# Use two pointers: prev (starts as null) and curr (starts at head).
# At each step:
# 1 . Store curr.next in temp.
# 2 . Reverse curr.next to point to prev.
# 3 . Move prev to curr and curr to temp.
# Repeat until curr is null.
# prev becomes the new head of the reversed list.