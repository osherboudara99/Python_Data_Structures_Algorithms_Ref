# https://leetcode.com/problems/climbing-stairs/description/
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:
# 1 <= n <= 45

def climb_stairs(n:int) -> int:
    if n == 1 or n ==2:
        return n 
    
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(5))

def climb_stairs(n:int) -> int:
    result = [1,2]

    for i in range(2, n):
        next_value = result[i-1] + result[i-2]
        result.append(next_value)
    
    return result[n-1]

print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(5))


def climb_stairs(n:int) -> int:
    if n <= 3:
        return n 
    
    prev1 = 3
    prev2 = 2 
    current = 0 

    for _ in range(3,n):
        current = prev1 +prev2 
        prev2 = prev1 
        prev1 = current 
    
    return current

print(climb_stairs(1))
print(climb_stairs(2))
print(climb_stairs(3))
print(climb_stairs(5))


# Approach 1: Recursive (Top-Down)
# - Use recursion to compute the number of ways to climb stairs.
# - Each call branches into two subproblems: n-1 and n-2.
# - This mimics the Fibonacci sequence where each step can be taken 1 or 2 stairs at a time.

# Time Complexity: O(2^n)
# - Exponential time due to repeated subproblem computations.

# Space Complexity: O(n)
# - Stack depth can go up to n due to recursive calls.

# Notes:
# - Elegant but highly inefficient for large inputs.
# - Can be improved with memoization or bottom-up DP.


# Approach 2: Dynamic Programming (Bottom-Up)
# - Use an array `result` to store number of ways to reach each step.
# - Initialize with base cases: 1 way to climb 1 stair, 2 ways to climb 2 stairs.
# - For each i from 2 to n-1, calculate result[i] = result[i-1] + result[i-2].

# Time Complexity: O(n)
# - Single pass through the range from 2 to n.

# Space Complexity: O(n)
# - Stores all intermediate results in a list.

# Notes:
# - Much more efficient than recursion.
# - Can be optimized further to O(1) space using two variables.

# Approach 3: Dynamic Programming with Space Optimization
# - Instead of storing all intermediate results in an array, we only keep track of the last two results.
# - Uses the observation that climbing stairs is like the Fibonacci sequence: f(n) = f(n-1) + f(n-2)
# - Initialize:
#   - prev1 = number of ways to reach step 3
#   - prev2 = number of ways to reach step 2
# - Iteratively calculate the number of ways to reach each step up to n by updating prev1 and prev2.

# Time Complexity: O(n)
# - Single pass through the range from 3 to n.

# Space Complexity: O(1)
# - Only three variables used regardless of input size.

# Notes:
# - Highly efficient in both time and space.
# - Ideal approach for large values of n.

