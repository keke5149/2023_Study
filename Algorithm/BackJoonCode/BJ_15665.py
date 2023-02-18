import sys
n,m = map(int, input().split())
numbers = list(set(map(int, sys.stdin.readline().split())))
numbers.sort()
answer = []

def count(cnt):
    if len(answer) == m: #수열 길이 m 만족하면 출력
        print(*answer)
        return
    cnt +=  1
    for i in numbers:
        answer.append(i)
        count(cnt)
        answer.pop()
count(0)
