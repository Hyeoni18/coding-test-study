# 거스름돈

money = 1000-int(input())

money_list = [500, 100, 50, 10, 5, 1]
result = 0

for i in money_list:
    result += money // i
    money = money % i

print(result)