#톱니바퀴 회전
#현재의 맞닿아있는 상태가 ns면 회전 -> 같은 극이면 하나가 회전해도 다른 하나는 회전x
#deque -> rotate 함수
import sys
from collections import deque
input = sys.stdin.readline
wheel = [deque(list(input().replace("\n", ""))) for _ in range(4)] # n: 0, s: 1

k = int(input())
rotate = [list(map(int, input().split())) for _ in range(k)] #1:시계, -1:반시계

for idx, dir in rotate:
    flag = {} #판단 다 하고 진짜 회전할 때 씀 //그냥 리스트로 해도 ㅇㅋ
    flag[idx] = dir
    check = deque() #양옆에서 돌아가는 거 있으면 넣음
    check.append([idx, dir])
    visited = [0]*5 #ns 판단한 적 있는지 확인
    visited[idx] = 1

    while check:
        current, d = check.popleft()
        #current의 오른쪽
        if current+1 != 5 and visited[current+1] != 1 and wheel[current-1][2] != wheel[current][6]:
            if d == 1: #current가 우회전
                flag[current+1] = -1
                check.append([current+1, -1])
            else:
                flag[current+1] = 1
                check.append([current+1, 1])
            visited[current+1] = 1

        #current의 왼쪽
        if current-1 != 0 and visited[current-1] != 1 and wheel[current-1][6] != wheel[current -2][2]:
            if d == 1: #current가 우회전
                flag[current-1] = -1
                check.append([current-1, -1])
            else:
                flag[current-1] = 1
                check.append([current-1, 1])
            visited[current-1] = 1

    print(current,dir, flag)
    for i in flag.keys():
        wheel[i-1].rotate(flag[i])
    print(wheel)

#마지막 계산
answer = 0
if wheel[0][0] == '1': answer += 1
if wheel[1][0] == '1': answer += 2
if wheel[2][0] == '1': answer += 4
if wheel[3][0] == '1': answer += 8
print(answer)