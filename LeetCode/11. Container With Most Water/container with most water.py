height = [1,8,6,2,5,4,8,3,7]

def contains_most_Water(height):
    maxWater = 0
    l,r = 0,len(height)-1

    while l<r:
        width = r - l
        minHeight = min(height[l],height[r])
        maxWater = max(maxWater,width*minHeight)
        if height[l]<=height[r]:
            l+=1
        elif height[r]<height[l]:
            r-=1

    return maxWater
    

print(contains_most_Water(height))