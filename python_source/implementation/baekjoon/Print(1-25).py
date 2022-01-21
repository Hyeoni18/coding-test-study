# Hello World! 출력
print("Hello World!")

# A+B
a, b = input().split()
print(int(a)+int(b))

# A-B
a, b = input().split()
print(int(a)-int(b))

# A*B
a, b = input().split()
print(int(a)*int(b))

# A/B
a, b = input().split()
print(int(a)/int(b))

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
score = int(input())
result = ''
if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 70:
    print('C')
elif 70 > score >= 60:
    print('D')
else:
    print('F')

# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
n = int(input())
for x in range(1,10):
    print(n, "*", x, "=", n*x)

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
n = int(input())
for i in range(1, n+1):
    print("*"*i)

# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 강아지 출력
print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
n = int(input())
for i in range(1, n+1):
    print(i)

# 고양이 출력
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
a, b = input().split()
a = int(a)
b = int(b)
if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+"*"*i)

# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
n = int(input())
for i in reversed(range(1, n+1)):
    print(i)

# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
n = int(input())
count = 0
for i in range(1, n+1):
    count += i
print(count)

# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
year = int(input())
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("1")
else:
    print("0")

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
n = int(input())

for i in range(n):
    a, b = input().split()
    print(int(a)+int(b))

# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
n, x = input().split()
a = input().split()
x = int(x)
result = []

for i in a:
    if x > int(i):
        result.append(i)

print(' '.join(result))

# "45분 일찍 알람 설정하기"
# 설정한 알람 시각이 주어졌을 때, 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 설정한 놓은 알람 시간 H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.
h, m = input().split()

h = int(h)
m = int(m) - 45
clock_h = 24
clock_m = 60

if m < 0:
    m += clock_m
    h -= 1
if h < 0:
    h += clock_h

print(h, m)

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.
while True:
    a, b = input().split()
    result = int(a)+int(b)
    if result == 0:
        break
    print(result)

# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# 다음 예를 보자. 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
init_n = input()
result = 1
n = init_n
while True:
    if len(n) < 2:
        n = '0' + n
    a, b = n.strip()
    num = int(a) + int(b)
    if num < 10:
        num += 10
    if int(b+str(num)[-1]) == int(init_n):
        break
    result += 1
    n = b+str(num)[-1]

print(result)

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
t = int(input())

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)
    num = i+1
    print(f"Case #{i+1}: {int(a)+int(b)}")
