# https://leetcode.com/problems/fizz-buzz/description/
# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


# Example 1:

# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


def fizzBuzz(n: int) -> list[str]:
    result = [] 

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizzBuzz(5))
print(fizzBuzz(15))
print(fizzBuzz(2))



# Approach: 
# Initialize result list
# Loop Through Numbers: The for loop iterates from 1 to n (inclusive), representing the numbers for which FizzBuzz needs to be computed.
    # The code checks if the current number is a multiple of both 3 and 5 (i % 3 == 0 && i % 5 == 0). If true, "FizzBuzz" is added to the result list.
    # If not, it checks if the current number is a multiple of 3 (i % 3 == 0). If true, "Fizz" is added to the result list.
    # Similarly, it checks if the current number is a multiple of 5 (i % 5 == 0). If true, "Buzz" is added to the result list.
    # Default Case: If the current number is not a multiple of 3 or 5, it adds the string representation of the number to the result list.
# The final result, which is a list of strings representing the FizzBuzz output for numbers from 1 to N, is returned.