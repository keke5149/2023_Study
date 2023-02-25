import sys
r, c = map(int, input().split())
cheese = []
for i in range(r):
    cheese.append(list(map(int, sys.stdin.readline().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(): #다 녹았는지 확인
    global cheese, r, c
    for i in range(r):
        for j in range(c):
            if cheese[i][j] == 1:
                return False
    return True

def dfs(i, j): #모든 좌표 확인
    global dx, dy, r, c, cheese
    for k in range(4): #상하좌우확인
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < r and 0 <= y < c and visited[x][y] == 0: #확인 안 한 좌표
            if cheese[x][y] != 0: #치즈라면
                cheese[x][y] += 1 #외부 공기와 만남 +1
            else:
                visited[x][y] = 1
                dfs(x, y)
def melt():
    global cheese, r, c
    for i in range(r):
        for j in range(c):
            if cheese[i][j] >= 3:
                cheese[i][j] = 0 #녹음
            elif cheese[i][j] > 0: #치즈긴 한데 2면 이상 안 만남
                cheese[i][j] = 1 #되돌림

time = 0
while True: 
    if check():
        print(time)
        break
    visited = [[0 for i in range(c)] for j in range(r)] #좌표 하나씩 확인
    visited[0][0] = 1
    dfs(0, 0)
    melt()
    time += 1
