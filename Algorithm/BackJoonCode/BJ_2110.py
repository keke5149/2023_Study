#공유기 설치
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

#이진탐색
#mn 없는 거 520ms, 있는 거 668ms
start = 1
end = house[-1] - house[0] #거리
answer = 0
while start <= end:
    mid = (start + end)//2 #거리
    current = house[0]
    #mn = 9e10
    count = 1
    for i in range(1, n):
        if house[i] >= current + mid: #다음 공유기를 설치할 위치가 현재 공유기 설치 위치 + 현재 거리 보다 멀리 있을 때
            #mn = min(mn, house[i] - current)            
            current = house[i] #공유기 설치
            count += 1
    if count < c: #덜 설치함
        end = mid-1
    else:
        start = mid + 1
        answer = mid #answer = max(answer, mn)
print(answer)
'''
#조합 다 찾기 -> 시간초과
from itertools import combinations
routers = combinations(house, c)
answer = []
for router in routers:
    mn = 9e10
    for i in range(c-1):
        for j in range(i + 1, c):
            if mn > router[j] - router[i]:
                mn = router[j] - router[i]
    answer.append(mn)
print(max(answer))
'''