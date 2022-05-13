# <문제> 섬의 개수
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
# <입력> 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다. 입력의 마지막 줄에는 0이 두 개 주어진다.
# <출력> 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
import sys
sys.setrecursionlimit(10000)

w = 0
h = 0
graph = []
result_arr = []

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(len(dx)):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

dx = [1,-1,0,0,-1,1,-1,1]
dy = [0,0,1,-1,1,1,-1,-1]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j):
              result += 1
    result_arr.append(result)

for i in range(len(result_arr)):
    print(result_arr[i])

# <다른 사람 풀이 참고>
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(r, c):
    for k in range(8):
        ni = r + di[k]
        nj = c + dj[k]
        if 0 <= ni < h and 0 <= nj < w and arr[ni][nj] and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj)
    return


# 상 하 좌 우 좌상 좌하 우상 우하
di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, -1, 1, -1, -1, 1, 1]
while True:
    w, h = map(int, input().split())
    ans = 0
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                dfs(i, j)
                ans += 1
    print(ans)

# <다른 사람 풀이 참고>
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):

    dx = [-1,0,1,0,-1,-1,1,1]
    dy = [0,1,0,-1,-1,1,-1,1]
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<h) and (0<=ny<w):
            if graph[nx][ny] == 1: # 방문처리
                graph[nx][ny] = -1
                dfs(nx, ny)



while True :
    w,h = map(int, input().split())
    if not w and not h:
        break
    graph = []
    cnt = 0
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                graph[i][j] = -1
                dfs(i,j)

    print(cnt)
    