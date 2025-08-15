# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=oizxjoit
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# Example 2:
# Input: head = [1], n = 1
# Output: []

# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
 
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
 
# Follow up: Could you do this in one pass?


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def print_LL(tmp:Optional[ListNode]):
    while tmp:
        print(tmp.val, end=' ')
        tmp = tmp.next 
    print()
    

def remove_nth_node(head:Optional[ListNode], n:int) -> Optional[ListNode]:
    if head.next is None:
        return None 

    tmp = head 
    leng = 0 

    while tmp:
        tmp = tmp.next
        leng += 1 
    
    if leng == n:
        return head.next 
    
    node_to_remove = leng - n 

    tmp = head 

    for _ in range(node_to_remove-1):
        tmp = tmp.next 
    
    if tmp.next:
        tmp.next = tmp.next.next 
    else:
        tmp.next = None 
    return head 

def remove_nth_node(head:Optional[ListNode], n:int) -> Optional[ListNode]:
    # Create a dummy node that points to head
    # This handles cases where the head node itself is removed
    dummy = ListNode(0, next = head)

    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead so there's a gap of n nodes
    for _ in range(n+1):
        first = first.next 

    while first:
        first = first.next 
        second = second.next 

    second.next = second.next.next 

    return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)

print_LL(l1)
result = remove_nth_node(l1, n=2)
print_LL(result)


l1 = ListNode(1)
l1.next = ListNode(2)

print_LL(l1)
result = remove_nth_node(l1, n=2)
print_LL(result)



l1 = ListNode(1)
l1.next = ListNode(2)

print_LL(l1)
result = remove_nth_node(l1, n=1)
print_LL(result)



print_LL(l1)
result = remove_nth_node(ListNode(1), n=1)
print_LL(result)

# Approach: Two-Pass Length Count
# 1. Handle edge case: If the list has only one node, removing it results in None.
# 2. First pass: Traverse the linked list to find its length (leng).
# 3. Special case: If `n` equals `leng`, remove the head node by returning `head.next`.
# 4. Calculate the position from the front: `node_to_remove = leng - n`.
# 5. Second pass: Move to the node just before the one we want to remove.
# 6. Adjust pointers to skip the target node.
# 7. Return the head of the modified list.
#
# Time Complexity: O(L) — where L is the length of the list (two full traversals).
# Space Complexity: O(1) — constant extra space.

# Approach: One-Pass Two-Pointer
# - Goal: Remove the n-th node from the end without computing the list length.
# - Use a dummy node pointing to head to simplify head removal cases.
# - Maintain two pointers: `first` and `second`.
# Steps:
#   1. Advance `first` by n+1 steps, creating a gap of n between `first` and `second`.
#   2. Move both pointers together until `first` reaches the end.
#   3. Now `second` is just before the node to be removed.
#   4. Adjust `second.next` to skip the target node.
# - Return dummy.next (new head).
#
# Time Complexity: O(L)
# - Only one traversal of the list.
#
# Space Complexity: O(1)
# - No extra storage apart from pointers.








    

    