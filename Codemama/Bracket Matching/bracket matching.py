def brackets_matching(s):
    stack = []
    matching_brackets = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != matching_brackets[char]:
                return "Brackets are not balanced."
            stack.pop()
    
    if not stack:
        return "Brackets are balanced."
    else: "Brackets are not balanced."

s = input()

print(brackets_matching(s))
