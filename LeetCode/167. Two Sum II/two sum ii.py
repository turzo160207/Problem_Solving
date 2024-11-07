nums = [1,3,4,5,7,10]

target = 9

def two_sum(nums,target):
    l, r = 0, len(nums)-1

    while l<r:
        currentSum = nums[l]+nums[r]

        if currentSum>target:
            r-=1

        elif currentSum<target:
            l+=1

        else:
            return[l+1,r+1]
        
    return(l+1,r+1)
        

print(two_sum(nums,target))