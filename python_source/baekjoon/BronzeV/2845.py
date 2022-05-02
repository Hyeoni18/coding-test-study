# 파티가 끝나고 난 뒤

l, p = map(int, input().split())
array = list(map(int, input().split()))
result = l*p
for i in array:
    print(i - result, end = ' ')
