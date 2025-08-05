# https://leetcode.com/problems/add-two-numbers/description/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 

def print_LL(ll:Optional[ListNode]):
    while ll:
        print(ll.val, end=' ')
        ll = ll.next 
    print() 


def add_two_numbers(l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
    num_str_1 = '' 
    num_str_2 = '' 

    while l1 or l2:
        if l1:
            num_str_1 += str(l1.val)
            l1 = l1.next 
        if l2:
            num_str_2 += str(l2.val)
            l2 = l2.next 
    num_1 = int(num_str_1[::-1])
    num_2 = int(num_str_2[::-1])

    result = num_1 + num_2 

    result_str = str(result)[::-1]

    dummy = ListNode()
    result_ll = dummy 

    for i in result_str:
        dummy.next = ListNode(int(i))
        dummy = dummy.next 
    return result_ll.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = add_two_numbers(l1, l2) 
print_LL(l3)

l1 = ListNode(0)
l2 = ListNode(0)

l3 = add_two_numbers(l1, l2) 
print_LL(l3)

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

l3 = add_two_numbers(l1, l2) 
print_LL(l3)

def add_two_numbers(l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
    total = 0 
    carry = 0 

    dummy = ListNode()
    res = dummy 

    while l1 or l2 or carry:
        total = carry 

        if l1:
            total += l1.val 
            l1 = l1.next 

        if l2:
            total += l2.val 
            l2 = l2.next 
        
        num = total % 10 
        carry = total // 10 

        dummy.next = ListNode(num)
        dummy = dummy.next 
    return res.next 

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

l3 = add_two_numbers(l1, l2) 
print_LL(l3)

l1 = ListNode(0)
l2 = ListNode(0)

l3 = add_two_numbers(l1, l2) 
print_LL(l3)

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

l3 = add_two_numbers(l1, l2) 
print_LL(l3)

# Approach 1: Convert Linked Lists to Integers and Back
# - Traverse both linked lists and build strings representing their digits.
# - Reverse the strings to convert them into the correct integer values.
# - Add the two integers together.
# - Convert the sum back into a string, reverse it, and build a new linked list from it.
#
# Time Complexity: O(n + m)
# - Traversing both linked lists, reversing strings, and integer conversion are all linear.
#
# Space Complexity: O(n + m)
# - Additional space for strings and the new linked list.
#
# Notes:
# - Simple to implement but not optimal for very large numbers.
# - Relies on Python’s big integer handling, which may be disallowed in some interview settings.
# - Not the standard LeetCode solution but valid if constraints allow.


# Approach 2: Digit-by-Digit Addition with Carry (Optimal)
# - Use a dummy node to build the result linked list incrementally.
# - Initialize carry = 0.
# - While there are digits left in either list or a carry:
#     1. Add l1.val and l2.val (if they exist) to carry.
#     2. Extract the digit: num = total % 10.
#     3. Update the carry: carry = total // 10.
#     4. Append the digit as a new node in the result linked list.
# - Return res.next (skipping the dummy placeholder node).
#
# Time Complexity: O(n + m)
# - Single pass through both linked lists.
#
# Space Complexity: O(max(n, m))
# - A new linked list of size proportional to the larger input list.
#
# Notes:
# - This is the standard and most optimal solution.
# - Does not depend on converting to strings or integers.
# - Correctly handles very large numbers without integer overflow.






    