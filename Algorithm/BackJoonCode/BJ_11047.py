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

#더 짧은 버전.. 근데 시간은 좀 더 오래 걸림 -> i<=k로 해서 조건세분화 안함
n, k = map(int, input().split())
cost = [0]*n
for i in range(n-1, -1, -1):
    cost[i] =int(input())
count = 0
for i in cost:
    if k >= 0:
        if i <= k:
            tmp = k//i
            count += tmp
            k -= i*tmp
    else:
        break
print(count)