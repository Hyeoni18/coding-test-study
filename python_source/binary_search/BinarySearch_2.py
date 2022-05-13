# <문제> 정렬된 배열에서 특정 수의 개수 구하기
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 예를 들어 수열 {1,1,2,2,2,2,3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
# 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다.

# <내 풀이>
from bisect import bisect_right, bisect_left

n, x = list(map(int, input().split()))
arr = list(map(int, input().split()))


def count_by_range(a, left, right):
    right_cnt = bisect_right(a, right)
    left_cnt = bisect_left(a, left)
    if right_cnt - left_cnt == 0:
        return -1
    else:
        return right_cnt - left_cnt


print(count_by_range(arr, x, x))


# <답안 예시>
count = count_by_range(arr, x, x)
if count == 0:
    print(-1)
else:
    print(count)
