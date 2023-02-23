#멤버 조합 1명~n//2명
#mnv로 제일 적은 능력치차 유지
#함수
from itertools import combinations
import sys

n = int(sys.stdin.readline())
member = list(i for i in range(n))
arr = []
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
mnv = 10000

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
    for j in member_comb:
        start = list(j)
        link = list(set(member) - set(start))
        sumstart = sum_team(start)
        sumlink = sum_team(link)
        mnv = min(mnv, abs(sumstart-sumlink))
        
print(mnv)
#python3은 시간초과, pypy3은 통과


