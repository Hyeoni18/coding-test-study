# <문제> 쉽게 푸는 문제

a, b = map(int, input().split())
number = []
num = 1

# 수열 생성
while len(number) < b:
    for _ in range(num):
        number.append(num)
    num += 1

result = 0
for i in range(a-1, b): # 일정한 구간의 합 구하기
    result += number[i]

print(result)

