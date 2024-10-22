n=input()
def funny_string(n):
    for i in range(len(n)):
        if((i%2==0 and not n[i].islower()) or (i%2!=0 and not n[i].isupper())):
            return "No"
        
       
    return "Yes"
        

print(funny_string(n))



