# <문제> 약수 구하기

n, k = map(int, input().split())
num = []

# 브루트 포스, 전체 탐색
for i in range(1, n+1):
    if n % i == 0:
        num.append(i)

if len(num) < k:
    print(0)
else:
    print(num[k-1])
