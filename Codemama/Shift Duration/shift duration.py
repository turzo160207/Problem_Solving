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
