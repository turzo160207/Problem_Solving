def count_strings_with_t():
    count = 0
    
    for _ in range(10):
        S = input().strip()
        if 'T' in S:
            count += 1
    
    return count

result = count_strings_with_t()
print(result)
