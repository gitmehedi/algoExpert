"""
Balance Brackets
"""
string = "([])(){}(())()()"


def balancedBrackets(string):
    pairs = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for st in string:
        if st not in list(pairs.keys()) + list(pairs.values()):
            continue
        elif not stack or pairs.get(stack[-1]) != st:
            stack.append(st)
        else:
            stack.pop()
    return len(stack) == 0


print(balancedBrackets(string))
