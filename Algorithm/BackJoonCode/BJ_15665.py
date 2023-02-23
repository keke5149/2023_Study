import sys
n,m = map(int, input().split())
numbers = list(set(map(int, sys.stdin.readline().split())))
numbers.sort()
answer = []

def count():
    if len(answer) == m: #함수 한번 돌릴 때마다 길이 체크 -> 결과 리스트(answer) 프린트
        print(*answer)
        return
    for i in numbers: #정렬된 리스트 numbers에서 answer의 0번째 자리부터 하나씩 붙여나감
        answer.append(i)
        count()
        answer.pop()
count()
