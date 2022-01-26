# <문제> 숨바꼭질
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다.
# 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
# <입력> 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
# <출력> 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# <내 풀이>
# BFS
n, k = map(int, input().split())

from collections import deque
checkNum = [0] * 1000000

queue = deque()
queue.append(n)
while queue:
    x = queue.popleft()
    if x == k:
        break
    x1, x2, x3 = x - 1, x + 1, x * 2
    if 0 <= x1 <= 100000 and checkNum[x1] == 0:
        checkNum[x1] = checkNum[x] + 1
        queue.append(x1)
    if 0 <= x2 <= 100000 and checkNum[x2] == 0:
        checkNum[x2] = checkNum[x] + 1
        queue.append(x2)
    if 0 <= x3 <= 100000 and checkNum[x3] == 0:
        checkNum[x3] = checkNum[x] + 1
        queue.append(x3)
print(checkNum[k])

# <다른 사람 풀이 참고>
# DFS 같은데
def find(n, k):
    if n >= k:  
        return n-k
    elif k == 1:
        return 1
    elif k%2:
        return min(find(n, k-1), find(n, k+1)) + 1
    else:
        return min(k-n, find(n, k//2) + 1)

n, k = map(int, input().split())
print(find(n, k))

# <추가> 지금 풀이보다 좀 더 깔끔한 방법을 생각해 봐야겠다.