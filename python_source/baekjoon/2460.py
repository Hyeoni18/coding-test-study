# <문제> 지능형 기차2

train = [input() for _ in range(10)]
people = 0
result = 0

for i in train:
    down, up = map(int, i.split())
    people -= down
    people += up
    if result < people:
        result = people

print(result)
