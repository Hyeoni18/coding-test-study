# <문제> 소수 찾기

def check(num):
    if num == 1:
        return 0

    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1


n = int(input())
number = map(int, input().split())
result = 0

for i in number:    # 소수 판별할 수
    result += check(i)

print(result)
