from itertools import combinations
import sys

n = int(sys.stdin.readline())
visited = [0]*n
member = list(i for i in range(n))
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
minValue = 10000

def sum_team(team):
    answer = 0
    for i in team:
        for j in team:
            if i!=j:
                answer += arr[i][j]
    return answer

# 멤버 조합
for i in range(1, n//2 + 1):
    member_comb = combinations(member, i)
    minVal = 10000

    for j in member_comb:
        start = list(j)
        link = list(set(member) - set(start))
        sumstart = sum_team(start)
        sumlink = sum_team(link)
        minValue = min(minValue, abs(sumstart-sumlink))
        
print(minValue)
#시간초과


