# <문제> 잃어버린 괄호

formula = input()
minus = formula.split('-')

result = 0
flag = False

for num in minus:
    if num.find('+') > 0:
        temp = 0
        for i in num.split('+'):
            temp += int(i)
        if flag:
            result -= temp
        else:
            result += temp
            flag = True # 연달아 플러스가 나올 경우 사이에 -가 존재하기에
    elif not flag: # 처음 들어온 수는 정수
        result += int(num)
        flag = True # 이후에 오는 식은 -를 기준으로 잘렸기에 - 부호 표시
    else:
        result -= int(num)

print(result)
# 맨 앞은 - 하지 않기
# 부호가 한 가지로만 구성됐을 경우