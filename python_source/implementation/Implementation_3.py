# <문제> 문자열 재정렬
# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
# <입력> 첫째 줄에 하나의 문자열 s가 주어집니다. ( 1 <= S의 길이 <= 10,000)
# <출력> 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

# <내 풀이>
# 문자열과 숫자를 나눈 뒤 문자열은 정렬하고 숫자는 더해줘서 다시 붙여준다
text_array = input().strip()
alphabet = ''
num = 0

for char in text_array:
    if ord(char) >= 65:
        alphabet += char
    else:
        num += int(char)

alphabet = sorted(alphabet)
text = ''
for char in alphabet:
    text += char

print(text+str(num))

# <답안 예시>
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append()
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))

# <추가> 알파벳 여부를 확인해주는 함수, 배열은 append 로 붙여주고 join함수를 통해 리스트를 문자열로 변환하는 것,,, 