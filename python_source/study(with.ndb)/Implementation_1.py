# <문제> 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야 하는 시각입니다.
# 00시 00분 03초 , 00시 13분 30초
# 반면에 다음은 3이 하나도 포함되어 있지 않으므로 세면 안 되는 시각입니다.
# 00시 02분 55초, 01시 27분 45초
# <입력> 첫째 줄에 정수 N이 입력됩니다. (0 <= N <= 23)
# <출력> 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력합니다.

# <내 풀이>
n = int(input())
result = 0

for i in range(n*10000+5959):
    time = i % 10000
    if time//100 < 60 and time%100 < 60:
        if '3' in str(i):
            result += 1

print(result)

# <해결 아이디어> 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있다. *완전 탐색 문제 유형이다.
# 하루는 24 * 60 * 60 = 86,400 초 이기 때문에 모든 경우를 고려하더라도 우리 컴퓨터는 이를 빠르게 처리할 수 있다.

# <답안 예시>
h = int(input())

count = 0
for i in range(h+1): # 시
    for j in range(60): # 분
        for k in range(60): # 초
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)