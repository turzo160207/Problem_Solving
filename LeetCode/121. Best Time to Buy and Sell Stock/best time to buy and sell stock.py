nums = [7,6,4,3,1]

def maxProfit(nums):
    maxProf = 0
    minBuy = nums[0]

    for i in range(len(nums)):
        if(nums[i]<minBuy):
            minBuy = nums[i]

        maxProf = max(maxProf, nums[i]-minBuy)

    return maxProf

print(maxProfit(nums))