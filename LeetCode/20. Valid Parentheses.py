def isValid(s: str) -> bool:
    stack = []

    for ss in s:

        if len(stack) and ss == ']' and stack[-1] == '[':
            stack.pop()
        elif len(stack) and ss == '}' and stack[-1] == '{':
            stack.pop()
        elif len(stack) and ss == ')' and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(ss)

    if len(stack):
        return False
    else:
        return True


class Solution:
    print(isValid("({{{{}}}))"))
