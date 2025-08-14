# https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=oizxjoit
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


def has_cycle(head:Optional[ListNode]) -> bool:
    if head is None or head.next is None:
        return False
    
    slow = head 
    fast = head 

    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next
         
        if fast == slow:
            return True
    return False


l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = l1.next
print(has_cycle(l1))

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = l1
print(has_cycle(l1))

l1 = ListNode(1)
print(has_cycle(l1))

l1 = ListNode(None)
print(has_cycle(l1))

# Approach: Floyd’s Tortoise and Hare (Cycle Detection)
# - Goal: Determine if a linked list has a cycle.
# - Idea:
#     - Use two pointers: `slow` moves one step at a time, `fast` moves two steps.
#     - If the linked list has a cycle, `fast` and `slow` will eventually meet.
#     - If `fast` reaches the end (`None`), there is no cycle.
# - Steps:
#     1. Handle edge cases: if list is empty or has only one node → no cycle.
#     2. Initialize both `slow` and `fast` at the head.
#     3. Move `slow` by 1 step, `fast` by 2 steps in each loop iteration.
#     4. If `slow` == `fast` at any point → cycle exists → return True.
#     5. If `fast` or `fast.next` becomes None → no cycle → return False.
#
# Time Complexity: O(n)
# - Each pointer traverses at most `n` steps.
#
# Space Complexity: O(1)
# - No extra data structures; only two pointers.
#
# Notes:
# - This is the optimal solution for cycle detection in linked lists.
# - The meeting point of `fast` and `slow` is not necessarily the start of the cycle.
