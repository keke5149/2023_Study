k,n = map(int, input().split())
lanline = [0]*k
for i in range(k):
    lanline[i]=int(input())

start = 1
end = max(lanline)

while(start <= end):
    count = 0
    mid = (start+end)//2

    for i in lanline:#모든 랜선(k개)를 mid 길이로 잘랐을 때 나오는 랜선 개수 
        count += i//mid
    if count >= n:#n보다 많이 나오면 mid를 크게(start지점을 크게) -> 랜선의 길이가 길어짐
        start = mid + 1
    else:#n보다 적게 나오면 mid를 작게(end지점을 작게) -> 랜선의 길이가 짧아짐
        end = mid -1
print(end)