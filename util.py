def pop(stack):
    if len(stack) == 0:
        return 0
    else:
        return stack.pop()

def push(stack, num):
    stack.append(num)