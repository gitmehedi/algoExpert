def getNthFib(n):
    a, b = 0, 1
    fib = []
    fib.append(a)
    fib.append(b)
    for i in range(n - 2):
        c = a + b
        a, b = b, c
        fib.append(c)

    return fib[n-1]


print(getNthFib(2))






# def solution(word, cipher):
#     ciword = []
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     if len(set(cipher)) != len(cipher):
#         return ""
#
#     for ind, w in enumerate(word):
#         if alphabet.find(w) and cipher.find(w) > -1:
#             ciword.append(cipher[alphabet.find(w)])
#         else:
#             return ""
#
#     return "".join(ciword)
#
#
# word = 'helloworld'
# cipher = 'ofwsujkizntphbxycamreqvlgd'
# respose = solution(word, cipher)
# print(respose)
# rkwwjojnwz
# def fibo(num):
#     fib = []
#     n1, n2 = 0, 1
#     for i in range(2, num):
#         n3 = n1 + n2
#         n1, n2 = n2, n3
#         if isPrime(n3):
#             fib.append(n3)
#     return fib
#
#
# def isPrime(n):
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, n):
#             if (n % i) == 0:
#                 return False
#         return True
#
#
# num = 7
# print(fibo(num))
