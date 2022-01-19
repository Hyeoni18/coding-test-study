# <문제> 곱하기 혹은 더하기
# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
# 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
# 예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0 + 2) * 9) * 8) * 4) = 576입니다. 또한 만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수가 되도록 입력이 주어집니다.
# (이렇게 입력이 주어지는 이유는, 일반적인 프로그래밍 언어에서 정수 데이터를 위해 기본 int형을 사용할 경우 약 21억 정도까지 값이 형성될 수 있기 때문이다.)

# <내 풀이>
# 0이 아니면 다 x를 해준다.
s = list(map(int, input().strip()))
# result = 0 초기값을 이렇게 설정하면 안 됨,, 빡대가린가;
result = s[0]
for i in range(1, len(s)): #for i in s 로 했었는데, 초기값을 수정하면서 범위도 수정
# 처음 풀이 했을 때 준 조건문
#   if result==0:   단, 이렇게 할 경우 1도 *를 수행하게 되므로 최대 값을 만들 수 없다. 틀린 방법임.
    if s[i]==0 or result==1: #result==0 or result==1 로 했었는데, 이렇게도 하면 안 됨; 0을 배열에서 찾아야지,,,하
        result+=s[i]    #그냥 i를 더하고 곱했었는데 range 로 변경되면서 s[i]로 변경
        continue
    result*=s[i]

print(result)

# <답안 예시>
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1,len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1: # 1일 때도 *보다 +를 진행해야 한다.
        result += num
    else:
        result *= num

print(result)

# <추가> 풀이 완전 틀렸음! 천천히 케이스를 잘 살펴보기