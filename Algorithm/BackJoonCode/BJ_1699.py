import math

N = int(input())
# 무조건 큰 수부터 내려가는 게 최소 제곱수가 아님.
# N 보다 작거나 같은 제곱수 안에서 최소 조합 찾기

dp = [0]*(N+1)

for i in range(1, N+1):
    dp[i] = i #1의 개수
for i in range(2, N+1):
    for j in range(2, int(math.sqrt(i))+1):
        # dp[i] = min(dp[i], dp[i-j*j]+1) //시간 2배 걸림
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i - j*j]+1

print(dp[N])