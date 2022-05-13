# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())
nList = list(map(int, str(a * b * c)))
result = [0,0,0,0,0,0,0,0,0,0]

for i in nList:
    result[i] += 1

for i in result:
    print(i)
