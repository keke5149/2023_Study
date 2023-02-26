import sys
from collections import deque
r, c = map(int, input().split())
cheese = []
for i in range(r):
    cheese.append(list(map(int, sys.stdin.readline().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#bfs/큐 사용/외부 공기 기준
def bfs():
    q = deque() #외부 공기 좌표 넣을 큐
    q.append([0,0]) #외부 공기 처리 시~작

    #새로운 외부 공기 만나면 큐에 넣고 하나씩 pop 하면서 상하좌우 확인 -
    # > 외부 공기 모두 확인할 때까지
    while q:
        i, j = q.popleft() #큐에 들어있는 외부 공기 하나 확인(꺼냄)
        for k in range(4): #상하좌우확인
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < r and 0 <= y < c and visited[x][y] == 0: #확인 안 한 좌표
                if cheese[x][y] != 0: #치즈라면
                    cheese[x][y] += 1 #외부 공기와 만남 +1
                else: #새로운 외부 공기
                    visited[x][y] = 1
                    q.append([x, y]) #새로운 외부 공기를 큐에 추가

def melt():
    global cheese, r, c
    for i in range(r):
        for j in range(c):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0 #녹음
            elif cheese[i][j] > 0: #치즈긴 한데 2면 이상 안 만남
                cheese[i][j] = 1 #되돌림

def check(): #다 녹았는지 확인
    global cheese, r, c
    for i in range(r):
        for j in range(c):
            if cheese[i][j] == 1:
                return False
    return True

time = 0
while True: #check() 만족할 때까지 계속 돌림
    if check():
        print(time)
        break
    visited = [[0 for i in range(c)] for j in range(r)] #좌표 하나씩 확인
    visited[0][0] = 1 #(0,0)은 무조건 외부공기 -> 별다른 처리 x
    bfs() #dfs(0,0)
    melt()
    time += 1

'''
#런타임 에러, dfs

def dfs(i, j): #외부 공기 (i, j)
    global dx, dy, r, c, cheese
    for k in range(4): #상하좌우확인
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < r and 0 <= y < c and visited[x][y] == 0: #확인 안 한 좌표
            if cheese[x][y] != 0: #치즈라면
                cheese[x][y] += 1 #외부 공기와 만남 +1
            else:
                visited[x][y] = 1
                dfs(x, y) #외부공기에 대해 dfs 돌림
'''
