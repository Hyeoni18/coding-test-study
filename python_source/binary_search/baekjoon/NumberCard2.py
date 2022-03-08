# <문제> 숫자 카드 2
# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
# <입력> 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
# <출력> 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.

# <내 풀이>
from sys import stdin, stdout
from bisect import bisect_right, bisect_left
n = int(stdin.readline())
arrN = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
arrM = list(map(int, stdin.readline().split()))
arrN.sort()
flag = True

def count_by_range(array, left, right):
    right_count = bisect_right(array, right)
    left_count = bisect_left(array, left)
    return right_count-left_count


for i in arrM:
    if not flag:
        stdout.write(" ")
    if flag:
        flag = False
    count = count_by_range(arrN, i, i)
    stdout.write(str(count))

# <다른 사람 풀이 참고>
import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
t = list(map(int,sys.stdin.readline().split()))
d = {}
for x in A:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for x in t:
    if x in d:
        print(d[x],end=' ')
    else:
        print(0,end=' ')

# <다른 사람 풀이 참고>
from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
nl = list(map(int, input().split()))
c = Counter(nl)
m = int(input())
for i in list(map(int, input().split())):
    print(c[i], end=" ")