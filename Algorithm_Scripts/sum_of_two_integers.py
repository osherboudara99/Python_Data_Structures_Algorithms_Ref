# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5
 
# Constraints:
# -1000 <= a, b <= 1000

def get_sum(a:int, b:int) -> int:

    bit_shortener = 0xffffffff

    while (b & bit_shortener) != 0:
        carry = (a&b) << 1
        a = a ^ b 
        b = carry 
    return a & bit_shortener if b > 0 else a


print(get_sum(1, 2))
print(get_sum(3, 4))


# Goal:
# Simulate addition of two integers without using '+' or '-' operators.
# We use bitwise operations to handle binary addition manually.

# Key Concepts:
# 1. XOR (^) gives the **sum without carry**.
#    - It adds bits like normal addition, except it ignores the carry.
#    - Examples:
#        0 ^ 0 = 0
#        1 ^ 0 = 1
#        0 ^ 1 = 1
#        1 ^ 1 = 0 (this is where carry would normally happen)

# 2. AND (&) finds **where a carry is needed**.
#    - Carry only happens when both bits are 1.
#    - Examples:
#        0 & 0 = 0
#        1 & 0 = 0
#        1 & 1 = 1 (this is where carry happens)
#    - We shift the carry left by 1 (carry << 1) because in binary,
#      a carry affects the next higher bit.

# 3. Repeat the process:
#    - sum = a ^ b       (adds without carry)
#    - carry = (a & b) << 1  (where to carry)
#    - Then, set a = sum and b = carry, and repeat.
#    - We continue until there is no carry left (i.e., b == 0).

# Example:
#   a = 3 (011), b = 2 (010)
#   Step 1: a ^ b = 001  (partial sum)
#           a & b = 010 → carry = 100
#   Step 2: a = 001, b = 100
#           a ^ b = 101, a & b = 000 → carry = 0
#   Done. Final answer is 101 (which is 5).

# Note on Python:
# Python integers can be arbitrarily large, but Leetcode uses 32-bit integers.
# To simulate 32-bit behavior and handle negatives correctly:
# - Use mask = 0xFFFFFFFF to limit values to 32 bits
# - Use MAX_INT = 0x7FFFFFFF to check for overflow and return signed result
# Python integers can grow beyond 32 bits, but we need to simulate 32-bit signed integer behavior (as expected by Leetcode).
# To do this:
# - We use a mask `0xFFFFFFFF` (which is 32 bits of 1s) to keep results within the 32-bit range (11111111 11111111 11111111 11111111).
# - This helps simulate overflow and wraps values just like in languages like C or Java.
# - After the addition loop, if the result exceeds the max 32-bit signed int (`0x7FFFFFFF`), 
#   we convert it to a negative value using two's complement: `~(result ^ 0xFFFFFFFF)`


# def get_sum(a:int, b:int) -> int:
#     # Algo if Python had no bit shortener issue

#     while b != 0:
#         carry = (a&b) << 1
#         a = a ^ b 
#         b = carry 
#     return a 


