# <문제> 일곱 난쟁이

from collections import deque

height = [int(input()) for _ in range(9)]
# queue = deque()
# 함수 없이 풀어보기
result = []
flag = False


def findChild(cnt):
    if cnt == 7:
        if sum(result) == 100:
            result.sort()
            for i in result:
                print(i)
            global flag
            flag = True
        return

    for i in range(len(result), 9):
        if result.count(height[i]) == 0:
            result.append(height[i])
            findChild(cnt+1)
            if flag:
                return
            result.remove(height[i])


findChild(0)

# from itertools import combinations
#
# nanjaengs = [int(input()) for _ in range(9)]
# nanjaengs.sort()
# for nanjaeng_7 in list(combinations(nanjaengs, 7)):
#     if sum(nanjaeng_7) == 100:
#         for person in nanjaeng_7:
#             print(person)
#         break