strs = "A man, a plan, a canal: Panama"

def valid_palindrome(strs):
    l,r = 0,len(strs)-1
    
    while l<r:
        while l<r and not alpha_num(strs[l]):
            l +=1
        while r>l and not alpha_num(strs[r]):
            r-=1

        if strs[l].lower() != strs[r].lower():
            return False
        
        l = l+1
        r = r-1
        
    return True



def alpha_num(c):
    return (ord('A')<=ord(c)<=ord('Z') or 
            ord('a')<=ord(c)<=ord('z') or 
            ord('0')<=ord(c)<=ord('9'))


print(valid_palindrome(strs))