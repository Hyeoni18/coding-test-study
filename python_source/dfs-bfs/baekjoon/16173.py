# 점프왕 쩰리 (Small)
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# array = []
# for _ in range(n):
#     array.append(list(map(int, input().split())))
#
#
# def dfs(y,x,cnt):
#     val = array[y][x]
#     if val == -1:
#         return -1
#     if val == 0:
#         return cnt
#
#     dis = [(0,val), (val,0)]
#     for dy, dx in dis:
#         dx = x + dx
#         dy = y + dy
#         if cnt == -1:
#             break
#         if (0 <= dx < n) and (0 <= dy < n):
#             cnt = dfs(dy, dx, cnt)
#     return cnt
#
#
# if dfs(0,0,0) == -1:
#     print("HaruHaru")
# else:
#     print("Hing")

# BFS
from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

visited = [[0]*n for _ in range(n)]
visited[0][0] = 1 # 방문함
queue = [(0,0)]
result = 0

while queue:
    x, y = queue.pop(0)
    val = array[y][x]

    if val == -1:
        #최종 경로 도착
        result = 1
        break

    dis = [(0,val), (val,0)]
    for dy, dx in dis:
        dx = x + dx
        dy = y + dy
        if 0 <= dx < n and 0 <= dy < n:
            if visited[dy][dx] == 0:
                visited[dy][dx] == 1
                queue.append((dy,dx))

if result == 1:
    print("HaruHaru")
else:
    print("Hing")
