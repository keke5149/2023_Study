#뱀은 (0,0)에서 출발, 길이는 1, 시작방향 오른쪽, 매초 이동, 왼쪽L, 오른쪽D
#벽 또는 자기자신과 부딪히면 게임끝
#time++ 위치 헷갈림
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
k = int(input())
apples = [list(map(int, input().split())) for _ in range(k)] #사과위치
l = int(input()) #방향전환횟수
direction = {}
for i in range(l):
    time, dir = input().split()
    direction[int(time)] = dir

dx = [0, 1, 0, -1]#우회전 기준
dy = [1, 0, -1, 0]


snake = deque()
snake.append([1, 1])

x, y, d, time =  1, 1, 0, 0 #초기 정보(좌표, 방향, 시간)

while 1:
    time += 1
    tx = x + dx[d] #방향에 맞게 이동
    ty = y + dy[d]
    if not (1 <= tx <= n and 1 <= ty <= n): #벽인지
        print("벽이다")
        break
    if [tx, ty] in snake: #자기 자신과 만나는지
        print("자기랑 만남")
        break
    
    snake.append([tx, ty])
    if [tx, ty] in apples: #사과가 있다면
        apples.remove([tx, ty])
    else:
        snake.popleft() #사과가 없으니 꼬리 펑
    print(snake)
    x, y = tx, ty
    if time in direction.keys(): #방향 전환할 타이밍인지
        print(str(time) + " 방향전환")
        if direction[time] == "L": #왼쪽
            d = (d-1) %4
        else:
            d = (d+1) %4
print(time)