#입력
N = int(input())
cost = [0]*(N+1)
for i in range(1, N+1):
    cost[i] = int(input())
dp = [0]*(N+1)

if N == 1:
    print(cost[1])
elif N == 2:
    print(cost[1] + cost[2])
else:
    dp[1] = cost[1]
    dp[2] = cost[1] + cost[2]
    dp[3] = max(cost[2] + cost[3], cost[1] + cost[3])
    for i in range(4, N+1):
        dp[i] = max(dp[i-3] + cost[i] + cost[i-1], dp[i-2] + cost[i])

        '''
            for i in range(3, N+1):
            if dp[i-1] == 0:
                dp[i] = dp[i-2] + cost[i]
            else:
                if cost[i] > cost[i+1]:
                    dp[i] = dp[i-1] + cost[i]
                elif cost[i] < cost[i+1]:
                    dp[i+1] = dp[i-1] + cost[i+1]
                else:
                    if cost[i+1] < cost[i+2]:
                        dp[i+1] = dp[i-1] + cost[i+1]
                    else: 
                        dp[i] = dp[i-1] + cost[i]
        
        '''
    print("결과")
    print(dp[-1])