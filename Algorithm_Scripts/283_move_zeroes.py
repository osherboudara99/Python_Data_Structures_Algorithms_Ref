# https://leetcode.com/problems/move-zeroes/description/
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]
 

# Constraints:

# 1 <= nums.length <= 104
# -231 <= nums[i] <= 231 - 1
 

# Follow up: Could you minimize the total number of operations done?


def moves_zeroes(nums:list[int]):
    # O(n)
    slow = 0 
    for fast in range(len(nums)):
        if nums[fast]!= 0:
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1 

    return nums
    
def move_zeroes(nums:list[int]):
    #O(n) -> minimized operations
    slow = 0 

    for fast in range(len(nums)):
        if nums[fast] != 0:
            if slow != fast: # Swapping not done everytime
                nums[fast], nums[slow] = nums[slow], nums[fast]
            slow += 1 
    return nums

print(move_zeroes([0]))

print(move_zeroes([0,1,0,3,12]))

print(move_zeroes([1,2,3,0,4,5,6,0,3,4,0,8]))

#  Approach:
# Initialize slow variable 
# Iterate from beginning of list to end
#   If the number at fast index does not equal zero, 
#       If slow != fast
#            swap values at slow and fast index
#       increment left variable 
# (slow and fast will stay at same position if no zeroes in array
# (if zero is encountered slow stays and fast increments so then when we reach next non zero, we swap and zero is closer to end of list)
    

# Approach 1: Two-Pointer Swap
# - Use two pointers: 'fast' to scan the list, 'slow' to track the position to move non-zero elements.
# - Every time a non-zero element is found, swap it with the element at 'slow' and increment 'slow'.
# - This method may perform unnecessary swaps if fast == slow.

# Time Complexity: O(n)
# Space Complexity: O(1) — in-place


# Approach 2: Two-Pointer Swap (with Swap Check Optimization)
# - Same logic as above, but includes a condition to skip unnecessary swaps (when slow == fast).
# - This reduces the number of actual writes to memory, which matters in environments with expensive write operations (e.g., flash memory).

# Time Complexity: O(n)
# Space Complexity: O(1) — in-place
