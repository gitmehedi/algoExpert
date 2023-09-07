"""

"""
# digits = [1, 2, 3]
#
#
# def plusOne(digits):
#     res = 0
#     length = len(digits)
#     base = 10
#     for val in range(length):
#         res = res + base ** (length - 1 - val) * digits[val]
#
#     res = res + 1
#     return [i for i in str(res)]
#
#
# print(plusOne(digits))

# path = "/home/"
#
#
# def simplifyPath(path):
#     stack = []
#     path = path.split('/')
#     for pt in path:
#         if stack and pt == '..':
#             stack.pop()
#         elif pt not in ['.', '', '..']:
#             stack.append(pt)
#     return "/" + "/".join(stack)
#
#
# print(simplifyPath(path))

tokens = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]


def evalRPN(tokens):
    stack = []
    op = ['+', '-', '*', '/']
    for tk in tokens:
        if tk not in op:
            stack.append(int(tk))
        else:
            right = stack.pop()
            left = stack.pop()
            res = float('inf')
            if tk == '+':
                res = left + right
            elif tk == '-':
                res = left - right
            elif tk == '/':
                res = left / right
            elif tk == '*':
                res = left * right
            stack.append(int(res))

    return stack[-1]


print(evalRPN(tokens))
