# <문제> 보물
# 옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
# 길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
# S의 최솟값을 출력하는 프로그램을 작성하시오.
# <입력> 첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다.
# N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.
# <출력> 첫째 줄에 S의 최솟값을 출력한다.

# <내 풀이>
# A랑 B를 곱할 때 최대한 수의 차이가 많이 나도록 A를 재배열
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True) # A를 내림차순으로 정렬
bSort = sorted(range(len(b)), key=lambda k:b[k]) # B를 내림차순으로 정렬한 인덱스 값을 추출
ab = map(lambda x,y: x*b[y], a, bSort)  # A값과 인덱스의 해당하는 B의 값을 곱셈
result = 0
for i in ab:
    result+=i

print(result)

# <다른 사람 풀이 참고>
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

print(sum([a[i] * b[i] for i in range(n)]))

# <추가>  B에 있는 수는 재배열 하면 안 된다는데 대부분의 풀이가 재배열되어 있다. 내가 뭘 잘못 이해했나 봐,,