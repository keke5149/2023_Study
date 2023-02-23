import sys
n = int(input())
people = list(map(int, sys.stdin.readline().split()))
people.sort()
finish = [0]*n
finish[0] = people[0]
for i in range(1, n):
    finish[i] = finish[i-1] + people[i]
print(sum(finish))