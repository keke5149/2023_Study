#이퍼 연습 문제(하)
#백준1388 바닥장식 DFS
import sys
input = sys.stdin.readline
m, n = map(int, input().split()) #세로길이 m, 가로길이 n
design = list(input() for _ in range(m))

visited = [[False]*n for _ in range(m)]
answer = 0

def dfs(i, j):
    visited[i][j] = True
    x, y = 0, 0
    if design[i][j] == '-':
        x = i
        y = j+1
    else:
        x = i+1
        y = j
    if x < m and y < n and design[x][y] == design[i][j] and not visited[x][y]:
        dfs(x, y)

for i in range(m): #행
    for j in range(n): #열
        if visited[i][j]:
             continue
        dfs(i, j)
        answer += 1
print(answer)