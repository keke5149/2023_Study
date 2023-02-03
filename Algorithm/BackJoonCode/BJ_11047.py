n, result = map(int, input().split())
cost = [0] * n
for i in range(n, 0, -1):
    cost[i-1] = int(input())

count = 0
for i in range(n):
    if result != 0:
        if cost[i] > result:
            continue
        elif cost[i] == result:
            count += 1
            result -= cost[i]
        else:
            tmp = result//cost[i]
            count += tmp
            result -= cost[i]*tmp
    else:
        break
print(count)