height = [0,1,0,2,1,0,1,3,2,1,2,1]

def trapping_rain_water(height):
    if not height:
        return 0
    
    l,r = 0, len(height)-1
    leftMax = height[l]
    rightMax = height[r]
    res = 0

    while l<r:
        if(leftMax<rightMax):
            l+=1
            leftMax = max(leftMax,height[l])
            res += leftMax - height[l]

        else:
            r-=1
            rightMax = max(rightMax,height[r])
            res += rightMax - height[r]

    return res

print(trapping_rain_water(height))