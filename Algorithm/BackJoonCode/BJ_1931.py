#schedule 넣으면 런타임 에러남/스케줄 빼면 맞음
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

#런타임 에러 안 나는 버전
n = int(input())
time = []
for i in range(n):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

meeting = []
meeting.append(time[0])
m = 0 #meeting용 인덱스
t = 1 #time용 인덱스
for i in range(n-1): #n-1까지 하면(range(n)) t에서 에러
    if meeting[m][1] <=time[t][0]:
        meeting.append(time[t])
        m += 1
    t += 1

print(len(meeting))