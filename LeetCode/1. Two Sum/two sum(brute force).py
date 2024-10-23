n=[2,1,4,3]

def two_sum(nums):
    target = 4
    for i in range(0,len(nums)):
        for j in range(1,len(nums)):
            if(nums[i]+nums[j]==target):
                return i,j
            

print(two_sum(n))
