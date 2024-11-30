A,B = map(int,input().split())
totalSeeds = 0

if(A<B):
    for i in range(A,B+1):
        if(i%2!=0):
            totalSeeds += i
else:
    for i in range(B,A+1):
        if(i%2!=0):
            totalSeeds += i


print(totalSeeds)

