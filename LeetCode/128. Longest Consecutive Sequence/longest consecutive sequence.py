nums = [100,1,2,200,3,101,4]

def longest_consecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if n-1 not in numSet:
            length = 0
            while (n+length) in numSet:
                length+=1
            longest = max(length,longest)

    return longest

print(longest_consecutive(nums))