def calculate_shift_duration(S, E):
    if E > S:
        duration = E - S
    elif E==S:
        duration = 24
    else:
        duration = (24 - S) + E

    return duration


S, E = map(int, input().split())

duration = calculate_shift_duration(S, E)
print(duration)

# Shift Duration
# Problem Statement

# You are tasked with calculating the duration of a work shift, knowing the start and end times in hours. A work shift can start on one day and end on another day, but it should not exceed 24 hours.
# Input

# Two integer numbers SS and EE representing the start and end times of a work shift in hours.
# Output

# Print the duration of the work shift in hours.
# Constraints

#     00 ≤≤ SS ≤≤ 2323
#     00 ≤≤ EE ≤≤ 2323

# Example 1:
# Input:

# 21 3

# Output:

# 6

# Example 2:
# Input:

# 10 10

# Output:

# 24

# Notes:

# In the second example, the start time of the shift is 10 am and end time is on the next day at 10 am. So total work time duration is 24 hours.