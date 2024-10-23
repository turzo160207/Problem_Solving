nums=[2,1,4,3]

def two_sum(nums):
    target = 4
    newMap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in newMap:
            return(newMap[diff],i)
        
        newMap[n]=i
            

print(two_sum(nums))
