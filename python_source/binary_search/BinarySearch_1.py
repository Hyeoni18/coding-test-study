# 파라메트릭 서치, 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
# 예시) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서 파라메트릭 서치 문제는 이진 탐색을 이용하여 해결할 수 있다.

# <문제> 떡볶이 떡 만들기
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어집니다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
# 둘째 줄에는 떡의 개별 높이가 주어집니다. 떡 높이의 총합은 항상 M 이상이므로,  손님은 필요한 양만큼 떡을 사갈 수 있습니다.
# 높이는 10억보다 작거나 같은 양의 정수 또는 0입니다.
# <출력 조건> 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력합니다.
# <입력 예시>       <출력 예시>
# 4 6              15
# 19 15 10 17

# <해결 아이디어>
# 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야 합니다.

# <내 풀이>
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    arrSum = 0
    for i in range(0, len(arr)):
        if arr[i] > mid:
            arrSum += arr[i] - mid
    if arrSum == target:
        return mid
    elif arrSum > target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


print(binary_search(arr, m, 0, arr[n-1]))

# <답안 예시>
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)

# <추가> max(array) 최대값 찾는 방법