# 검증수

array = list(map(int, input().split()))
result = 0
for i in array:
    result += (i * i)

print(result % 10)
