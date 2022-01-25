# <문제> 미로 탐색
# N×M크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다. 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
# <입력> 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
# <출력> 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# <내 풀이>
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if 0 > x+dx[i] or x+dx[i] >= n or 0 > y+dy[i] or y+dy[i] >= m:
                continue
            if graph[x+dx[i]][y+dy[i]] == 1:
                queue.append((x+dx[i],y+dy[i]))
                graph[x+dx[i]][y+dy[i]] = graph[x][y]+1

bfs(0,0)
print(graph[n-1][m-1])

# <다른 사람 풀이 참고>
from sys import stdin
N, M = map(int, stdin.readline().split())
# matrix 배열
matrix = [stdin.readline().rstrip() for _ in range(N)]
# 방문경로 배열
visited = [[0]*M for _ in range(N)]
# 좌/우/위/아래 방향 이동
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))