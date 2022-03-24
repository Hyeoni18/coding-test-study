# <문제> 영역 구하기
#
import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(y, x, cnt):
    graph[y][x] = 1
    for dy, dx in d:
        nx = x + dx
        ny = y + dy
        if (0 <= nx < n) and (0 <= ny < m) and graph[ny][nx] == 0:
            cnt = dfs(ny, nx, cnt+1)
    return cnt


result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(dfs(i, j, 1))

print(len(result))
print(*sorted(result))
