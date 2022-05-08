# <문제> N번째 큰 수

t = int(input())
case = [list(map(int, input().split())) for _ in range(t)]

for i in case:
    result = i
    for j in range(len(i)):
        max_index = j  # 가장 큰 원소의 인덱스
        print(result[max_index], max_index)
        for k in range(j + 1, len(i)): # 나머지 수 확인
            if result[max_index] < result[k]: # 현재 가장 큰 원소의 인덱스보다 새로운 인덱스의 수가 크다면
                max_index = k   # 인덱스 변경
        print(result[max_index], max_index)
        result[j], result[max_index] = result[max_index], result[j] # 현재 비교 중인 값과 (가장 크다고 생각 했던 값), 위의 반복문을 통해 새로 발견된 가장 큰 값의 위치를 변경
print(result[2])


for i in case:
    result = sorted(i, reverse=True)
    print(result[2])

