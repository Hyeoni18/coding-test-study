# 전자레인지

micro = [300, 60, 10]
t = int(input())
result = []
for i in micro:
    result.append(t // i)
    t %= i

if t > 0:
    print(-1)
else:
    for i in result:
        print(i, end=' ')
