n = int(input())
d = list(map(int, input().split()))#n-1개 -> [n-2]
cost =  list(map(int, input().split()))#nro -> [n-1]
'''
pay = cost[0]*d[0]
for i in range(1, n-1):
    if cost[i-1] <= cost[i]:
        pay += cost[i-1]*d[i]
    else:
        pay += cost[i]*d[i]
print(pay)
#오름차순으로 비교
'''
pay = 0
tmp = cost[0]
for i in range(n-1):
    if cost[i] < tmp:
        tmp = cost[i]
    pay += tmp*d[i]
print(pay)