def isValid(s):
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."""
    stack = []
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif i == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False
        elif i == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
    return len(stack) == 0

