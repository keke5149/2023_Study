#루머 퍼트리기
#deque 사용, 
import sys
from collections import deque
input = sys.stdin.readline
n = int(input()) #사람 수
connect = [[]] + [list(map(int, input().split())) for _ in range(n)]
m = int(input()) #최초 유포자 수
rumor = deque(map(int, input().split()))
time = [-1]*(n+1) #-2로 초기화하고 0(최초유포자), -1(타인과 연결x)부터 처리하려니까 시간초과뜸
for i in rumor:
    time[i] = 0

rest = [0] + [len(connect[i])//2 for i in range(1, n+1)]

while rumor:
    current = rumor.popleft() #루머를 믿고 있는 사람(current)
    for c in connect[current]: #의 주변인 탐색
        if c == 0: break
        rest[c] -= 1 #current가 루머를 믿고 있으므로 -1
        if time[c] == -1 and rest[c] <= 0:
            rumor.append(c) #루머
            time[c] = time[current] + 1

print(" ".join(map(str, time[1:])))
    