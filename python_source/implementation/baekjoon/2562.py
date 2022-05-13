# 최댓값

number = []
for _ in range(9):
    number.append(int(input()))

result = 0
for i in number:
    if result < i:
        result = i

print(result)
print(number.index(result)+1)
