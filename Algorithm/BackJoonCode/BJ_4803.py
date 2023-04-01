#4803 그래프 중에서 트리인 거 개수 세기
#dfs로 노드 하나씩 돌아가면서 끝까지 길찾기
#이미 루트에 들어간 적 있는 것은 패스(continue)
import sys
input = sys.stdin.readline

def dfs(current, parent):
    global connect
    visited[current] = 1
    for c in connect[current]:
        if c == parent: #직전 노드
            continue
        if visited[c] == 1: #이미 루트에 들어가 있으면
            return False
        if not dfs(c, current): #이후 길 찾다가 사이클 발견
            return False
    return True

case = 0
while 1:
    n, m = map(int, input().split()) #n개 정점 m개 간선
    case += 1
    count = 0 #트리 개수
    if n == 0:
        break
    connect = [[] for _ in range(n+1)]
    for _ in range(m):
        c1, c2 = map(int, input().split())
        connect[c1].append(c2)
        connect[c2].append(c1)
    visited = [0 for _ in range(n+1)]

    for i in range(1, n+1): #시작 노드 i
        if visited[i] == 1: #이미 어떤 루트에 들어가 있으면 패스
            continue
        if dfs(i, 0):
            count += 1
    
    if count == 0: print("Case " + str(case) + ": No trees.")
    elif count == 1: print("Case " + str(case) + ": There is one tree.")
    else: print("Case " + str(case) + ": A forest of "+ str(count) + " trees.")



 
    



