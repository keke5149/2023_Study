n = int(input())

times = [0] * n
schedule = [0] * n
for i in range(n):
    times[i] = list(map(int, input().split()))

times.sort(key=lambda x:x[0])
times.sort(key=lambda x:x[1])

endtime = times[0][1]
schedule[0] = times[0]
count = 1
for i in range(1,n):
    if endtime <= times[i][0]:
        endtime = times[i][1]
        count += 1
        schedule[count-1] = times[i]
print(schedule)
print(count)

#schedule 넣으면 런타임 에러남...        