# https://leetcode.com/problems/happy-number/description/
# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

# Example 2:
# Input: n = 2
# Output: false
 
# Constraints:
# 1 <= n <= 231 - 1


def is_happy(n:int) -> bool:
    encountered = {} 

    while n != 1:

        n = sum([int(i) ** 2 for i in str(n)])

        if n in encountered:
            return False 

        encountered[n] = None 
    return True


def is_happy(n:int) -> bool:
    encountered = {} 

    while n != 1:

        value = 0 
        for i in str(n):
            value += int(i)**2

        if value in encountered.keys():
            return False
    
        encountered[n] = None 
        n = value 
    return True


def is_happy(n: int) -> bool:
    encounter = {}
    while True:
        
        value = 0
        for i in str(n):
            value += int(i) ** 2 
        
        if value == 1:
            return True 
        
        if value in encounter.keys():
            return False
        
        encounter[value] = True
        n = value


def is_happy(n: int) -> bool:
    encountered = set() 

    while n != 1:

        value = 0 
        for i in str(n):
            value += int(i)**2  
        
        if value in encountered:
            return False 
        
        encountered.add(value)
        n = value 
    return True


def is_happy(n :int) -> bool:
    def get_next(n:int) -> int:
        return sum(int(i) ** 2 for i in str(n))
    
    slow = n 
    fast = get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return fast == 1 



print(is_happy(19))
print(is_happy(2))
print(is_happy(1))



# === Happy Number Algorithm Approaches ===

# --- Approach 1: Hash Map + List Comprehension ---
# - For each number, convert to string and sum the squares of digits using a list comprehension.
# - Track encountered numbers in a dictionary to detect cycles (infinite loop if not happy).
# - If you reach 1 → it's a happy number; if you revisit a number → not happy.
# - Time Complexity: O(log n) iterations, each with O(log n) digit operations ⇒ O(log n * d)
# - Space Complexity: O(log n) to store previous results.
# - Pros: Concise and readable; easy to implement.
# - Cons: Uses a dictionary, which may use slightly more memory than needed.

# --- Approach 2: Hash Map + Explicit Loop ---
# - Same logic as Approach 1, but sums digits explicitly in a loop instead of using a list comprehension.
# - Slightly more verbose but identical logic and performance.
# - Time Complexity: O(log n * d)
# - Space Complexity: O(log n)
# - Pros: More transparent to beginners.
# - Cons: Same memory overhead from dictionary use.

# --- Approach 3: Infinite Loop + Manual Break ---
# - Uses `while True` with explicit checks for `value == 1` and cycle detection.
# - Slightly different control structure, but identical logic to above.
# - Time Complexity: O(log n * d)
# - Space Complexity: O(log n)
# - Pros: Direct, works the same way; useful if you want to emphasize control flow over loop condition.
# - Cons: Less clean termination condition than `while n != 1`.

# --- Approach 4: Hash Set for Cycle Detection ---
# - Instead of a dictionary, uses a set to track seen values — more memory efficient.
# - Checks if value already exists in set before adding.
# - Time Complexity: O(log n * d)
# - Space Complexity: O(log n)
# - Pros: Cleaner and slightly more efficient in space than using a dict.
# - Cons: Still not constant space.

# --- Approach 5: Floyd’s Cycle Detection (Fast and Slow Pointers) ---
# - Uses a helper function to compute the next number.
# - Two pointers (`slow` and `fast`) advance at different speeds.
# - If there's a cycle, fast and slow will meet (not happy); if fast reaches 1 → happy number.
# - Time Complexity: O(log n * d)
# - Space Complexity: O(1) — most space-efficient
# - Pros: Optimal space; does not use extra data structures.
# - Cons: Slightly less intuitive; harder to debug for beginners.
