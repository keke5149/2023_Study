#비밀번호 찾기
#화살표 방향에 따라 왼/오 스택 두 개 활용
#left 리스트를 기본으로 right 리스트를 temp로 사용 //right는 문자가 역순으로 들어감
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
pw = [input().strip() for _ in range(n)]

def getpw(password):
    left, right = [], []
    for p in password:
        if p == "<":
            if left:
                right.append(left.pop())
        elif p == ">":
            if right:
                left.append(right.pop())
        elif p == "-":
            if left:
                left.pop()
        else:
            left.append(p)
    print(''.join(left) + ''.join(reversed(right)))

'''
#안 됨...
def getpw2(password):
    result = deque()
    cursor = 0
    for p in password:
        if p == "<":
            if cursor > 0:
                cursor -= 1
        elif p == ">":
            if cursor < len(result):
                cursor += 1
        elif p == "-":
            if cursor > 0:
                result.pop()
                cursor -= 1
        else:
            result.insert(cursor, p)
            cursor += 1
    print(''.join(result))
'''

for i in pw:
    getpw(i)
