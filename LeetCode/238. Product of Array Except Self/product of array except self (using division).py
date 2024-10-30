nums = [1,2,3,4]

def product_array(nums):
    product = 1
    for i in range(len(nums)):
        product *= nums[i]

    for i in range(len(nums)):
        nums[i] = product//nums[i]


    return nums


print(product_array(nums))