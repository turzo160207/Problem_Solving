n,x = map(int,input().split())

def lazyWalking(n,x):
    x*=n
    while n>0:
        x+= n-1
        n-=1

    return x

print(lazyWalking(n,x))