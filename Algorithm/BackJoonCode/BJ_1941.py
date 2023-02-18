seat = [input() for i in range(5)]
visited = [[0] * 5 for _ in range(5)]
result = 0
princess = []
directionR = (-1,1,0,0)
directionC = (0,0,-1,1)
        
def check(s):
    global available    
    r = s // 5
    c = s % 5
    for d in range(4):
        nr = r + directionR[d]
        nc = c + directionC[d]
        if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
            continue
        next = nr*5+nc
        if next in princess: #7명 중에 있는지 확인
            visited[nr][nc] = 1
            available += 1
            check(next)

def dfs(depth, yeon, idx): #idx: 학생 1-25
    global available, result, visited
    if yeon > 3 or 25-idx < 7-depth: #다솜4명 못맞추면 미리 자름
        return

    if depth == 7:
        available = 1 #좌표연결시작점(초기화)
        visited = [[0] * 5 for _ in range(5)]
        sr = princess[0]//5 
        sc = princess[0]%5
        visited[sr][sc] = 1
        check(princess[0]) # 공주0번부터 연결되어 있는지 확인
        if available == 7: # 전부 연결
            result += 1
        return

    r = idx // 5    
    c = idx % 5

    #7명조합에 넣기
    if seat[r][c] == "Y":
        princess.append(idx)
        dfs(depth+1, yeon+1, idx+1)
        princess.pop()
    else:
        princess.append(idx)
        dfs(depth+1, yeon, idx+1)
        princess.pop()
    dfs(depth, yeon, idx+1)
    
dfs(0, 0, 0)
print(result)