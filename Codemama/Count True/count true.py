n=list(map(int,input().split()))

def count_true(n):
    count = 0
    length = n[0]
    for i in range(1,length+1):
        if(n[i]==1):
            count +=1

    return count

print(count_true(n))