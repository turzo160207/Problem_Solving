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
