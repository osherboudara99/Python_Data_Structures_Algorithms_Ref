# https://leetcode.com/problems/merge-two-sorted-lists/description/

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]

from typing import Optional


class ListNode:
    def __init__(self, val = 0 , next = None):
        self.val = val 
        self.next = next 
    
def print_LL(ll:Optional[ListNode]):
    while ll:
        print(ll.val, end=' ')
        ll = ll.next
    print()


def merge_two_sorted_LL(list1:Optional[ListNode], list2:Optional[ListNode]): 

    dummy = ListNode(0)
    tmp = dummy 

    while list1 and list2:
        if list1.val < list2.val:
            tmp.next = list1 
            list1 = list1.next 
        else:
            tmp.next = list2 
            list2 = list2.next 
        tmp = tmp.next 
    
    if list1:
        tmp.next = list1 
    
    if list2:
        tmp.next = list2 
    
    return dummy.next 


list1 = ListNode(1)
list1.next = ListNode(2) 
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3) 
list2.next.next = ListNode(4)

sorted_ll = merge_two_sorted_LL(list1=list1, list2=list2)
print_LL(sorted_ll)


# Approach: Two-Pointer Iterative Merge using a Dummy Node
# - Use two pointers to traverse both sorted linked lists
# - Compare current nodes from each list
# - Append the smaller node to the merged list
# - Continue until one list is exhausted
# - Append the remainder of the non-empty list

# Dummy Node:
# - Acts as a placeholder to simplify edge case handling (like empty input lists)
# - The `dummy.next` will point to the head of the merged list

# Time Complexity: O(n + m)
# - n: number of nodes in list1
# - m: number of nodes in list2
# - Each node is visited exactly once

# Space Complexity: O(1)
# - Iterative solution, uses constant space (in-place merge)

# Notes:
# - Elegant and efficient way to merge two sorted linked lists
# - Dummy node pattern is common to simplify list manipulations
