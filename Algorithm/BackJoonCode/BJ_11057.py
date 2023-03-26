# n 길이의 오름차순 수 개수/ 0으로 시작 가능
# 만들 수 있는 수 다 찾고 시작하면(product) 시간 초과
# dp/ 가장 큰 숫자를 제일 마지막에 오게 해서 횟수 세기//dp[7]: 가장 큰 숫자가 7
n = int(input())
dp = [1]*10 #길이 1의 수는 전부 1개 가능

for i in range(n-1): #n길이 수의 개수를 찾으려면 1~(n-1)길이의 수 개수를 누적해서 알고 있어야//(길이 - 1)번 반복
    for j in range(1, 10): #제일 큰 수가 0인 수는 길이가 얼마가 되든 항상 1개//0, 00, 000, ...
        dp[j] += dp[j-1]

print(sum(dp)%10007)

'''
#시간 초과
from itertools import product
n = int(input())
numbers = list(i for i in range(10))
perm = product(numbers, repeat = n)

count = 0
for p in perm:
    out = 0
    for i in range(n-1):
        if p[i] > p[i+1]:
            out = 1
            break
    if out == 0:
        count += 1
print(count % 10007) 
'''