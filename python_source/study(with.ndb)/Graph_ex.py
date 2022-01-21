# 그래프 탐색 알고리즘
# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

# 스택, 먼저 들어 온 데이터가 나중에 나가는 형식, 선입후출, 입구와 출구가 동일한 형태, 삽입과 삭제 연산으로 이루어진다. O(1)
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력

# 큐, 먼저 들어 온 데이터가 먼저 나가는 형식, 선입선출, 입구와 출구가 모두 뚫려 있는 터널과 같은 형태, 삽입과 삭제 연산으로 이루어진다.
from collections import deque # 리스트 자료형을 사용할 수도 있지만, 시간복잡도가 높아서 비효율적이다. 리스트를 사용하게 되면 원소를 꺼내고 난 뒤 원소의 위치를 다시 조정하는 과정이 필요하기에 O(k) 복잡도가 요구된다.

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque() # 스택과 큐 자료구조의 장점을 모두 합친 자료구조라고 볼 수 있다.
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 가장 왼쪽에 있는 데이터를 꺼내겠다.
print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

# 재귀 함수, 자기 자신을 다시 호출하는 함수
def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursive_function()

# recursive_function() # 무한 호출 예제임 (파이썬은 기본적으로 깊이 제한이 있기에 재귀 함수 도중 오류메세지가 발생된다.)

# 재귀 함수를 문제 풀이에서 사용할 때는 종료 조건을 반드시 명시해야 한다.
def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
# 재귀 함수는 마치 스택에 데이터를 넣었다가 빼는 것과 같다. 실제로 스택프레임에 데이터가 담기게 되어 차례대로 호출이 되었다가 마지막에는 호출했던 함수로 돌아온다. 그래서 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.

# 팩토리얼 구현 예제, n! = 1 * 2 * 3 * ... * (n-1) * n, 수학적으로 0!과 1!의 값은 1입니다.
# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!을 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print("반복적으로 구현:",factorial_iterative(5))
print("재귀적으로 구현:",factorial_recursive(5))

# 최대공약수 계산 (유클리드 호제법) 예제 , 재귀 함수를 효과적으로 사용할 수 있음
# 유클리드 호제법은 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 한다. 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다.
# ex) GCD(192, 162)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))
