def count_strings_with_t():
    count = 0
    
    for _ in range(10):
        S = input().strip()
        if 'T' in S:
            count += 1
    
    return count

result = count_strings_with_t()
print(result)

# T-Finder
# Problem Statement

# Write a program that reads 10 strings, one string per line. Your task is to count how many of these 10 strings contain the character 'T'.
# Input

# Ten lines, each containing a string SS consisting of uppercase letters.
# Output

# An integer representing the number of strings that contain the character 'T'
# Constraints

#     33 ≤≤ ∣S∣∣S∣ ≤≤ 1515

# Example 1:
# Input:

# TIGER
# ELEPHANT
# LION
# ZEBRA
# APE
# PANDA
# KANGAROO
# TOUCAN
# PENGUIN
# CHEETAH

# Output:

# 4

# Example 2:
# Input:

# GORILLA
# PANTHER
# RHINOCEROS
# PUMA
# LEOPARD
# HIPPOPOTAMUS
# GIRAFFE
# ORANGUTAN
# KANGAROO
# CROCODILE

# Output:

# 2

# Notes:

# In the first example, the strings "TIGER", "ELEPHANT", "TOUCAN" and "CHEETAH" contain the character 'T' so the output is 4.