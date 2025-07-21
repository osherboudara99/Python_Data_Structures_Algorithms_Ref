#  https://leetcode.com/problems/missing-number/description/
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation:
# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation:
# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation:
# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

 

def missing_number(nums:list[int]) -> int:
    for i in range(len(nums)+1):
        if i not in nums:
            return i 

print(missing_number( nums = [3,0,1]))
print(missing_number( nums = [0,1]))
print(missing_number(nums = [9,6,4,2,3,5,7,0,1]))

def missing_number(nums:list[int]) -> int:
    missing = len(nums)
    for i in range(len(nums)):
        missing ^= nums[i] ^ i 
    return missing 

print(missing_number( nums = [3,0,1]))
print(missing_number( nums = [0,1]))
print(missing_number(nums = [9,6,4,2,3,5,7,0,1]))


def missing_number(nums:list[int]) -> int:
    n = len(nums)
    expected_sum = sum(range(n+1)) # n * (n+1) // 2 
    actual_sum = sum(nums)
    return expected_sum - actual_sum


print(missing_number( nums = [3,0,1]))
print(missing_number( nums = [0,1]))
print(missing_number(nums = [9,6,4,2,3,5,7,0,1]))


# Approach: Brute Force Linear Scan
# - Iterate through numbers from 0 to n (inclusive)
# - For each number, check if it's in the input list
# - Return the first number that is not found

# Time Complexity: O(n²)
# - The `in` operation is O(n) inside a loop of O(n+1)

# Space Complexity: O(1)
# - No additional data structures are used

# Notes:
# - Very easy to understand and implement
# - Not efficient for large input sizes
# - Not recommended in interviews or performance-critical applications




# Approach: Bit Manipulation (XOR)
# - Initialize `missing` to n (the length of the array)
# - XOR all indices and all elements in the array together
# - The result will be the missing number due to XOR canceling out equal pairs

# Explanation:
# - A ⊕ A = 0 and A ⊕ 0 = A
# - XOR all indices [0..n] and all values in `nums`
# - All matching pairs cancel out, and the missing value remains

# Time Complexity: O(n)
# - Single pass through the array

# Space Complexity: O(1)
# - No extra space is used

# Notes:
# - Very efficient and clever
# - Often used as a follow-up to the summation method in interviews
# - Avoids overflow issues that could occur with summation in lower-level languages




# Approach: Math (Sum Difference)
# - Use the formula for the sum of the first n natural numbers: n * (n + 1) // 2
# - Calculate the expected sum from 0 to n
# - Subtract the actual sum of the array from the expected sum
# - The result is the missing number

# Time Complexity: O(n)
# - Summing the list and computing the range sum each take O(n)

# Space Complexity: O(1)
# - Only constant extra space used

# Notes:
# - Very efficient and concise
# - Works only if there is exactly one number missing in range [0, n]
# - Recommended approach for interviews and production