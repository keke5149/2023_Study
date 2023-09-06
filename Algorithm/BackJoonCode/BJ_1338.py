import sys
input = sys.stdin.readline
r1, r2 = map(int, input().split())
x, y = map(int, input().split())

count, flag = 0, 0
for i in range(r1, r2):
    if count == 1:
        print("Unknwon Number")
        flag = 1
        break

    if abs(i-y)%x == 0:
        count =1
        answer = i

if flag == 0 and count == 1:
    print(answer) 