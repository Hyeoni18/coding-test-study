# <문제> 좌표 정렬하기
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
# <입력> 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
# <출력> 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# <내 풀이>
# x, y 좌표를 각각 받은 배열을 x 배열 sorting index 값으로 y 배열 값을 가져오고 x 값이 같을 경우 y 값 비교 후 출력
import sys

n = int(sys.stdin.readline())
xi, yi = [], []
for _ in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    xi.append(num[0])
    yi.append(num[1])

xiSort = sorted(range(len(xi)), key=lambda k: xi[k])
yiSort = [yi[xiSort[0]]] # 1
for i in range(1, n):
    def equals(arr, iRange):
        arr.sort()
        for j in arr:
            print(xi[xiSort[iRange]], j)

    if xi[xiSort[i - 1]] == xi[xiSort[i]] and i < n - 1:
        yiSort.append(yi[xiSort[i]])
        continue
    elif xi[xiSort[i - 1]] == xi[xiSort[i]] and i == n - 1:
        yiSort.append(yi[xiSort[i]])
        equals(yiSort, i - 1)
        continue

    if len(yiSort) < 2 and i < n - 1:
        print(xi[xiSort[i - 1]], yi[xiSort[i - 1]])
        yiSort = [yi[xiSort[i]]]
    else:
        equals(yiSort, i - 1)

    yiSort = [yi[xiSort[i]]]

    if i == n - 1:
        print(xi[xiSort[i]], yi[xiSort[i]])

# <다른 사람 풀이 참고>
import sys

result = []
for i in range(int(input())):
    result.append(list(map(int,sys.stdin.readline().split())))

result.sort()
for i in result:
    print(*i) # 리스트의 압축을 푸는 거래

# <추가> 이렇게 단순한 방법을 왜 생각 못했을까..?
