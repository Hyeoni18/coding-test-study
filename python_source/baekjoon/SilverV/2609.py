# <문제> 최대공약수와 최소공배수
import sys
sys.setrecursionlimit(10001)

n, m = map(int, input().split())
# 약수 구하기
ns = []
for i in range(1, n+1):
    if n % i == 0:
        ns.append(i)
ms = []
for i in range(1, m+1):
    if m % i == 0:
        ms.append(i)


# 최대 공약수 구하기
def findMax():
    if len(ns) > len(ms):
        ms.reverse()
        for i in ms:
            if ns.count(i) == 1:
                 return i
    else:
        ns.reverse()
        for i in ns:
            if ms.count(i) == 1:
                return i


# 최소 공배수 구하기
# def findMin(n2, m2):
#     if n2 == m2:
#         return n2
#     print(n2, m2)
#     if n2 > m2:
#         m2 += m
#     else:
#         n2 += n
#
#     return findMin(n2, m2)

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# print(findMax())
# n2 = n
# m2 = m
#print(findMin(n2,m2))

print(gcd(n,m))
print(n*m//gcd(n,m))
