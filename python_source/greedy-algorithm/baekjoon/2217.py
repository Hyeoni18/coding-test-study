# 로프

n = int(input())
array = [int(input()) for i in range(n)]
array.sort()
result = 0
while len(array) > 0:
    stand = array[0]
    temp = len(array) * stand
    array.remove(stand)
    if result < temp:
        result = temp

print(result)

# 다른 사람 풀이
import sys
input = sys.stdin.readline
rope = []
for i in range(int(input())):
    rope.append(int(input()))
rope.sort(reverse=True) #큰 수 부터
answer = []
mount = 0
for i in range(len(rope)):
    answer.append(int(rope[i]*(i+1))) # 계산된 값 배열을 만들어서
print(max(answer)) # 제일 큰 수를 출력

# while(if)으로 인해 시간복잡도가 높아짐,,