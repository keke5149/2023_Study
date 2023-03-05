import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
space = [list(input().split()) for _ in range(n)] #0: 청소되지 않음 1: 벽
visited = [[0]*m for i in range(n)]
#북(idx 0) 서(idx 3) 남(idx 2) 동(idx 1) 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited[r][c] = 1
count = 1
while 1:
    #(새로운) (r, c)에서 시작
    clean = 0
    for _ in range(4): #상하좌우 봐서 청소 안 한 곳 있으면 처리
        d = (d+3)%4
        x = r + dx[d]
        y = c + dy[d]
        if 0 <= x < n and 0 <= y < m and space[x][y] == "0":
            if visited[x][y] == 0:
                clean = 1
                visited[x][y] = 1
                count += 1
                r, c = x, y
                break

    if clean == 0: #상하좌우 한 군데도 청소 못함
        if space[r - dx[d]][c-dy[d]] == "1":
            print(count)
            break
        else:
            r, c = r - dx[d], c-dy[d] #되돌아감

