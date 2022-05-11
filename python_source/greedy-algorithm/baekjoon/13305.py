# 주유소

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))

oil = price[0]
result = 0

for i in range(len(price)-1):
    if oil > price[i]:
        oil = price[i]
    result += oil * dis[i]

print(result)
