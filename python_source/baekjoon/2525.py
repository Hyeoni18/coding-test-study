# <문제> 오븐시계

a, b = map(int, input().split())
c = int(input())

hour = c // 60
min = c % 60

b += min
if b > 59:
    hour += 1
    b -= 60

a += hour
if a > 23:
    a -= 24

print(a,b)