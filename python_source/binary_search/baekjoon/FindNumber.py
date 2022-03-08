# <문제> 수 찾기
# N개의 정수 A[1],A[2],...,A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# <입력> 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수의 범위는 -2의 31제곱 보다 크거나 같고 2의 31제곱보다 작다.
# <출력> M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
# <예제>
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
from bisect import bisect_right, bisect_left

n = int(input())
arrA = list(map(int, input().split()))
arrA.sort()
m = int(input())
arrM = list(map(int, input().split()))


def count_by_range(arr, left, right):
    right_cnt = bisect_right(arr, right)
    left_cnt = bisect_left(arr, left)
    return right_cnt - left_cnt


for i in arrM:
    count = count_by_range(arrA, i, i)
    if count == 0:
        print(0)
    else:
        print(1)

# <다른 사람 풀이 참고>
from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')

# <다른 사람 풀이 참고>
import sys
input = sys.stdin.readline
n = int(input())
li = input().split()
m = int(input())
li2 = input().split()
dic = {i:0 for i in li}

for i in li2:
    if i in dic:
        print('1')
    else:
        print('0')
