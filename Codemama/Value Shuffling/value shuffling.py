def value_shuffling(A, B, C, S):
    B,C,A = A,B,C

    result = []
    for char in S:
        if char == 'A':
            result.append(A)
        elif char == 'B':
            result.append(B)
        elif char == 'C':
            result.append(C)

    print(*result)

input_values = input()
A, B, C = input_values.split()
S = input()

value_shuffling(A, B, C, S)

# Value Shuffling
# Problem Statement

# You are given three integers AA, BB, CC and one string SS. Your task is to swap the values among them in in the following sequence:

#     A→B
#     B→C
#     C→A

# After these swaps, the values of AA, BB, and CC should be replaced accordingly.

# Write a program that performs the specified swaps and outputs the values of AA, BB, and CC in the given order in string SS.
# Input

# Three integers AA, BB, and CC, separated by spaces. Additionally, a string representing the order in which to show the values after performing the swap, consisting of three uppercase letters ('A', 'B', 'C'). The order string will not contain any spaces.
# Output

# After performing the swaps, print three integers in a single line representing the values of AA, BB, and CC according to the given order. Separate the integers by spaces.
# Constraints

#     0≤A,B,C≤10000≤A,B,C≤1000

# Example 1:
# Input:

# 5 10 15
# ABC

# Output:

# 15 5 10

# Example 2:
# Input:

# 3 8 0
# BAC

# Output:

# 3 0 8 

# Notes:

# In second example, after swapping the values. A, B, and C becomes 0, 3 and 8. So, output is printed in the given order B(3) A(0) C(8).