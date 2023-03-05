#동적프로그래밍
n = int(input())
dp = [[0, []] for _ in range(n+1)] #[연산횟수, [연산과정리스트]], 최대 n번 채워넣음
dp[1][0] = 0 #dp[1]에서의 연산횟수 0(연산할 것도 없이 이미 1)
dp[1][1] = [1] #dp[1]에 저장된 숫자 리스트

#n을 계산해서 1을 만드는 것과 별개로 n이하의 모든 자연수에 대해 시행/결과 저장(1부터 n까지)
#n 보다 작거나 같은 모든 숫자에 대해 연산 123을 수행했을 때 얻을 수 있는 결과 넣음(dp에)
for i in range(2, n+1): #i: n보다 작거나 같은 숫자, 연산 결과로서의 숫자
    #1을 뺀다
    dp[i][0] = dp[i-1][0] + 1 #연산횟수 +1
    dp[i][1] = dp[i-1][1] + [i] #연산결과 리스트에 [i] 추가([i] 기록)
    #3으로 나누어 떨어질 때
    if i%3 == 0 and dp[i // 3][0] + 1 < dp[i][0]:#이번에 i//3하면서 얻게 될 연산횟수가 i까지 연산했을 때 얻는 연산횟수보다 작을 때(같으면 뭐든 상관x니까)
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    #2로 나누어 떨어질 때 
    if i%2 == 0 and dp[i // 2][0] + 1 < dp[i][0]:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

#idp를 모두 채움
print(dp[n][0]) #n까지의 연산횟수
print(*reversed(dp[n][1]))

'''
# @mingulmangul 풀이 - 엄청 빠름

def solution2(N):
    q = deque([N])
    dp = [0] * (N+1)
    while q:
        n = q.popleft()
        # 1에 도착했으면
        if n == 1:
            # N까지 거슬러 올라가기
            answer = deque([n])
            while n != N:
                n = dp[n]
                answer.appendleft(n)
            # 출력
            print(len(answer) - 1)
            print(*answer)
            return

        # 아직 방문한 적 없으면, 방문 + 직전 노드 저장
        if n % 3 == 0 and dp[n//3] == 0:
            dp[n//3] = n
            q.append(n//3)
        if n % 2 == 0 and dp[n//2] == 0:
            dp[n//2] = n
            q.append(n//2)
        if dp[n-1] == 0:
            dp[n-1] = n
            q.append(n-1)
'''