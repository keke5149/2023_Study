#진실을 아는 사람이 없는 파티에서만 거짓말 하기
#파티별로 진실을 하는 사람 체크//교집합
#모든 파티 확인 후 파티 수 합산//교집합
import sys
n, m = map(int, input().split())
truth = list(sys.stdin.readline().split()[1:])
party = []
for i in range(m):
    party.append(list(sys.stdin.readline().split()[1:]))
count = 0

for i in range(m): #진실을 아는 사람이 갱신되므로 파티 하나 확인할 때마다 전체 파티 다시 확인
    for p in party:
        ist = 0
        for n in p:
            if n in truth:
                ist = 1
                break
        if ist == 1:
            for n in p:
                if n not in truth:
                    truth.append(n)
        else:
            continue

for p in party:
    if not set(p)&set(truth):
        count += 1
print(count)
'''
import sys
n, m = map(int, input().split())
truth = set(sys.stdin.readline().split()[1:])
party = []
for i in range(m):
    party.append(set(sys.stdin.readline().split()[1:]))
count = 0

for i in range(m):
    for p in party:
        if p & truth:
            truth = truth.union(p)

for p in party:
    if not p & truth:
        count += 1
print(count)
'''
