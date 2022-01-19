# <문제> 회의실 배정
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
# 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
# <입력> 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다.
# <출력> 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

# <내 풀이>
# 회의시간 짧은 순으로 정렬 후 빠른 시간으로 정렬해서 배정
n = int(input())
meeting = (list(map(int, input().split())) for i in range(n))

result = 0
meeting = sorted(meeting, key=lambda x: (x[0], x[1]-x[0]))
stTm = 0
edTm = 0
for i in meeting:
    if stTm <= i[0] and edTm > i[1]:
        stTm = i[0]
        edTm = i[1]
    elif i[0] >= edTm:
        stTm = i[0]
        edTm = i[1]
        result += 1

print(result)

# <다른 사람 풀이 참고>
n = int(input())
time = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
result = end = 0

for s, e in time:
    if s >= end:
        result += 1
        end = e

print(result)

# <추가> 속도가 10배 넘게 차이 난다. 내 풀이도 보면 끝나는 시간을 기준으로 +1 이 되는데 전혀 생각하지 못했다. 좀 더 나은 생각을 해야 할 텐데,