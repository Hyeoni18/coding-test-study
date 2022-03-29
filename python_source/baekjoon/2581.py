# <문제> 소수

m = int(input())
n = int(input())
array = []


def check(n):
    if n == 1:
        return False

    for i in range(2,n//2+1):
        if n % i == 0:
            return False

    return True


for i in range(m, n+1):
    if check(i):
        array.append(i)

result = 0
for i in array:
    result += i

if len(array) == 0:
    print(-1)
else:
    print(result)
    print(array[0])
