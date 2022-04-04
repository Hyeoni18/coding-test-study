# <문제> 주사위 세개

a, b, c = map(int, input().split())

if a == b and b == c:
    print(10000 + a * 1000)
elif a == b or a == c or b == c:
    array = [a, b, c]
    array.sort()
    print(1000 + array[1] * 100)
else:
    array = [a, b, c]
    array.sort()
    print(array[2] * 100)
