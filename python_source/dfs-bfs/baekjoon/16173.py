# 점프왕 쩰리 (Small)
import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))


def dfs(y,x,cnt):
    val = array[y][x]
    if val == -1:
        return -1
    if val == 0:
        return cnt

    dis = [(0,val), (val,0)]
    for dy, dx in dis:
        dx = x + dx
        dy = y + dy
        if cnt == -1:
            break
        if (0 <= dx < n) and (0 <= dy < n):
            cnt = dfs(dy, dx, cnt)
    return cnt


if dfs(0,0,0) == -1:
    print("HaruHaru")
else:
    print("Hing")
