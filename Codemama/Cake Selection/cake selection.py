W,S,C = map(int,input().split())

def cake_selection(W,S,C):
    if ((W>=200 and W<=300) and S>=50 and C>=150):
        print("Yes")
    else:
        print("No")

cake_selection(W,S,C)