s="anagram"
t="nagaran"

def valid_anagram(s,t):
    s = sorted(s)
    t = sorted(t)

    if s == t:
        return True
    
    else:
        return False
    
print(valid_anagram(s,t))