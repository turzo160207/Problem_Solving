n = [1,2,3,4,1,2]

def contains_duplicate(n):
    new_set = set()
    for i in n:
        if i in new_set:
            return True
        else:
            new_set.add(i)

    return False

print(contains_duplicate(n))

