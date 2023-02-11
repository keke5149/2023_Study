n = int(input())
union = []
for i in range(n):
    union.append(int(input()))
union.sort()

xysum = set() #중복 제거
for x in union:
    for y in union:
        xysum.add(x+y)
answer = []
for i in range(n-1, -1, -1):#큰 것 부터, k
    for j in range(i+1):#k-z에서 z
        if union[i] - union[j] in xysum:
            answer.append(union[i])

max = max(answer)
print(max)