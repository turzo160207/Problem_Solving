N,A,B = map(int,input().split())

def assignment_deadline(N,A,B):
    if N>=A+B:
        print("Yes")

    else:
        print("No")

assignment_deadline(N,A,B)