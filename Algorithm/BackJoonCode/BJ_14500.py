#dfs/깊이 우선 탐색/다음 분기로 넘어가기 전에 모든 노드를 탐색/막히면 이전 노드로 되돌아가 기록 리셋, 재탐색/visited
import sys
n, m = map(int, input().split())
numbers = []
for _ in range(n):
    numbers.append(list(map(int, sys.stdin.readline().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
mx = 0 #블럭 밑의 숫자들의 합(최대, 결과)
inimxnum = max(map(max, numbers)) #numbers 최댓값
visited = [[0]*m for i in range(n)]

def dfs(x, y, count, total):#(x, y) 현재 좌표
    global mx
    if total + inimxnum*(4-count) <= mx: #아래를 계산해도(탐색) 현재의 최댓값을 못 넘을 경우 -> 진행 x
        return
    
    if count == 4:#4개 다 만듦 -> 종료
        mx = max(mx, total)
        return
    
    #블럭 붙이기
    for i in range(4):#상하좌우 좌표 이동
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < n and 0 <= ty < m and visited[tx][ty] == 0: #범위 내 + 방문 이력 x
            # 2개 연결한 상태에서ㅏㅓㅗㅜ 만들기
            if count == 2:
                visited[tx][ty] = 1
                dfs(x, y, count + 1, total + numbers[tx][ty]) #새로 붙은 블럭에 대해서 진행x 기존 블럭에서 다시 탐색
                visited[tx][ty] = 0 #이전 블럭좌표에서의 탐색 기록 없애기(되돌리기)
            
            #기본 블럭 연결
            visited[tx][ty] = 1
            dfs(tx, ty, count + 1, total + numbers[tx][ty])
            visited[tx][ty] = 0

for i in range(n):
    for j in range(m): #모든 좌표에 대해
        visited[i][j] = 1
        dfs(i, j, 1, numbers[i][j]) #탐색 시작
        visited[i][j] = 0 #초기화
print(mx)