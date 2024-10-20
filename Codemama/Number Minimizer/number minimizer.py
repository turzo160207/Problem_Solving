# -*- coding: utf-8 -*-
# Write Python code from here
def minimize_number(S, K):
    num_list = list(S)
    length = len(num_list)
    
    changes = 0

    for i in range(length):
        if changes < K:
            if i == 0 and num_list[i] != '1':
                num_list[i] = '1'
                changes += 1
            elif i > 0 and num_list[i] != '0':
                num_list[i] = '0'
                changes += 1

    minimized_number = ''.join(num_list)
    
    print("Min =", minimized_number)


S, K = input().split()
K = int(K)


# Number minimizer
# Problem Statement

# Given a string SS representing a very large integer, minimize SS by changing at most KK digits, such that SS still doesn't contain any leading zeros. Input length and output length should be same.
# Input

# Will contains a string SS, and an integer KK separated by spaces in a single line.
# Output

# Print "Min = " then print minimum number after the change(If any) of the string without leading zeros.
# Constraints

#     10≤∣S∣≤10010≤∣S∣≤100
#     1≤K≤∣S∣1≤K≤∣S∣

# Example 1:
# Input:

# 9876543210 5

# Output:

# Min = 1000043210
