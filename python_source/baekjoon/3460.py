# <문제> 이진수

# 테스트 개수
T = int(input())
test = [int(input()) for _ in range(T)]

for i in test:
    num = []
    count = 0
    while i > 0:
        num.append(i % 2)
        if i % 2 == 1:
            print(count, end=' ')
        count += 1
        i = i//2

