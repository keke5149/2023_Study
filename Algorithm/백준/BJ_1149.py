N = int(input())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))   
    #split()/map(함수, 반복 가능한 자료형(리스트, 튜플 등))

dp = [[0 for j in range(3)] for i in range(N)]
dp[0][0] = A[0][0]
dp[0][1] = A[0][1]
dp[0][2] = A[0][2]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1] + A[i][0], dp[i-1][2] + A[i][0])
    dp[i][1] = min(dp[i-1][0] + A[i][1], dp[i-1][2] + A[i][1])
    dp[i][2] = min(dp[i-1][0] + A[i][2], dp[i-1][1] + A[i][2])

min = min(dp[N-1][0], dp[N-1][1], dp[N-1][2])
print(min)
