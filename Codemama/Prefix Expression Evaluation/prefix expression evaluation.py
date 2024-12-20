def evaluate_prefix(expression):
    stack = []
    
    for char in reversed(expression):
        if char.isdigit():
            stack.append(int(char))
        elif char in "+-*/":
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 // operand2
            
            stack.append(result)

    return stack[0]

expression = input()

result = evaluate_prefix(expression)
print(result)
