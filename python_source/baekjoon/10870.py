# <문제> 피보나치 수 5

num = int(input())
# n1 = 0
# n2 = 1
#
# for _ in range(1, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#
# if num == 0:
#     print(0)
# else:
#     print(n2)


# <재귀 함수>
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(num))
